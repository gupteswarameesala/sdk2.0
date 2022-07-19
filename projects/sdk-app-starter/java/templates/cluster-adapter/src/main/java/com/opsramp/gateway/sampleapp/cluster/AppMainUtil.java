package com.opsramp.gateway.{{res}}.cluster;

import java.io.FileReader;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.google.gson.Gson;
import com.opsramp.app.content.core.alerthandler.MetricResponse;
import com.opsramp.app.content.core.alerthandler.ResourceMetricData;
import com.opsramp.app.content.core.integration.CacheStore;
import com.opsramp.app.content.core.integration.MessagePublisher;
import com.opsramp.app.content.core.integration.ServiceFactory;
import com.opsramp.app.processor.handlers.GenericMessageHandler;
import com.opsramp.gateway.common.cache.DatastoreClient;
import com.opsramp.gateway.common.configuration.AppConfiguration;
import com.opsramp.gateway.common.configuration.ApplicationConfig;
import com.opsramp.gateway.common.configuration.ApplicationInfo;
import com.opsramp.gateway.common.core.ApplicationRegistry;
import com.opsramp.gateway.common.enums.Services;
import com.opsramp.gateway.common.publisher.queue.ApplicationPublisher;


public class AppMainUtil {
	private static final Logger LOG = LoggerFactory.getLogger(AppMainUtil.class.getName());

	private AppMainUtil() {
		// Ignore
	}
	
	public static AppConfiguration appBuilderProcess() throws Exception {
		LOG.trace("AppMainUtil started.");

		AppConfiguration appConfiguration = null;
		try {
			Gson gson = new Gson();

			ApplicationInfo info = gson.fromJson(new FileReader("/opt/app/info.json"), ApplicationInfo.class);
			LOG.trace("info.json file Read successfully.");

			ApplicationConfig config = null;
			config = gson.fromJson(new FileReader("/opt/app/config/config.json"), ApplicationConfig.class);
			LOG.trace("config.json file Read successfully.");

			String[] dependencies = gson.fromJson(new FileReader("/opt/app/config/dependencies.json"), String[].class);
			LOG.trace("dependencies.json file Read successfully.");

			CacheStore cacheStore = new CacheStore() {
				@Override
				public String get(String store, String key) throws Exception {
					return DatastoreClient.get(store, key);
				}

				@Override
				public boolean put(String store, String key, String value) throws Exception {
					return DatastoreClient.put(store, key, value);
				}

				@Override
				public boolean remove(String store, String key) throws Exception {
					return DatastoreClient.remove(store, key);
				}

				@Override
                public String gget(String store, String key) throws Exception {
                        return DatastoreClient.gget(store, key);
                }

			};

			// Configuring the message publisher
			MessagePublisher publisher = new MessagePublisher() {
				@Override
				public void publish(String message) throws Exception {
					ApplicationPublisher.publish(Services.OUTBOUND_CHANNEL, message);
				}

				@Override
				public void publish(String topic, String message) throws Exception {
					ApplicationPublisher.publish(topic, message);
				}

				@Override
				public void publishMetrics(String configId, String metricDef, String monitorjsonStr,
						String resourceType) throws Exception {
					//AlertsDataProcessUtil.publishMetricsAndAlert(configId, metricDef, monitorjsonStr, resourceType);
				}

				@Override
				public List<MetricResponse> publishAlerts(String templateId, String monitorId, String resourceType, String resourceId, List<ResourceMetricData> metricData) throws Exception {
					LOG.debug("AppMainUtil# publishAlerts# templateId :::"+templateId+" monitorId:: "+monitorId+" metricData size::"+metricData.size());
					return  null;
				}
			};

			// Set store and publisher for the app to use
			ServiceFactory.init(cacheStore, publisher);

			appConfiguration = new AppConfiguration.Builder(info, config).setDependency(dependencies).setDebugProcessor(new AppDebugProcessor()).setProcessor(new ApplicationProcessor()).build();
			LOG.error(" IN JAVA-CODE GENERATOR ALTRA LATEST CLUSTERED APP ");
			ApplicationRegistry.setLogProcessor(new AppLogProcessor());

			GenericMessageHandler.registerActions();
			
		} catch (Exception e) {
			LOG.error("Failed to register message-sorter service", e);
			throw e;
		}
		LOG.trace("AppMainUtil Ended..");
		return appConfiguration;
	}
}