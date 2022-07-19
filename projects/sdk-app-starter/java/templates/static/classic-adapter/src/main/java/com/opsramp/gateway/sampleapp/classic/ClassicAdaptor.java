package com.opsramp.gateway.{{res}}.classic;

import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.google.gson.Gson;
import com.google.gson.JsonElement;
import com.opsramp.app.content.core.actionhandler.AbstractActionHandler;
import com.opsramp.app.content.core.alerthandler.MetricResponse;
import com.opsramp.app.content.core.alerthandler.ResourceMetricData;
import com.opsramp.app.content.core.integration.CacheStore;
import com.opsramp.app.content.core.integration.FilteredResourceRegistry;
import com.opsramp.app.content.core.integration.MessagePublisher;
import com.opsramp.app.content.core.integration.ServiceFactory;
import com.opsramp.app.processor.handlers.GenericMessageHandler;
import com.opsramp.gateway.content.core.CloudMessagePublisher;
import com.opsramp.gateway.content.core.Content;
import com.opsramp.gateway.content.core.DatastoreClient;
import com.opsramp.gateway.utils.JsonUtil;


public class ClassicAdaptor extends GenericMessageHandler implements Content {
    private static final Logger LOG = LoggerFactory.getLogger(ClassicAdaptor.class);

    private static final String APP_NAME = "{{appName}}";
    private static final String ACTION = "action";
	private static final String MESSAGE_ID = "messageId";
	private static final String MODULE = "module";
	private static final String SUBTYPE = "subtype";

    public void init() {
    	LOG.error(" Invoking ClassicAdapter Init ");
    	final Content app = this;
    	
    	CacheStore cacheStore = new CacheStore() {

			@Override
			public String get(String store, String key) throws Exception {
				return DatastoreClient.get(app, store, key);
			}

			@Override
			public String gget(String store, String key) throws Exception {
				return DatastoreClient.get(app, store, key);
			}

			@Override
			public boolean put(String store, String key, String value) throws Exception {
				return DatastoreClient.put(app, store, key, value);
			}

			@Override
			public boolean remove(String store, String key) throws Exception {
				return DatastoreClient.remove(app, store, key);
			}

    	};
    	
        MessagePublisher publisher = new MessagePublisher() {
            @Override
            public void publish(String message) throws Exception {
                CloudMessagePublisher.publish(message);
            }

            @Override
            public void publish(String topic, String message) throws Exception {
                CloudMessagePublisher.publish(message);
            }

            @Override
            public void publishMetrics(String configId, String metricDef, String message, String resourceType) throws Exception {
                CloudMessagePublisher.publishMetrics(configId, metricDef, message);
            }

			@Override
			public List<MetricResponse> publishAlerts(String templateId, String monitorId, String resourceType, String resourceId, List<ResourceMetricData> metricData) throws Exception {
				return null;
				//return CloudMessagePublisher.publishAlerts(templateId, monitorId, resourceType, resourceId, metricData);
			}

            
        };

        ServiceFactory.init(cacheStore, publisher);
        
        GenericMessageHandler.registerActions();
        
        LOG.error("Initiation of cachestore and publisher starting  CacheStore {} , Publisher{} , app{} " , cacheStore , publisher , app.getName());
    }

    public String getName() {
        return APP_NAME;
    }

	public void messageRecived(String cloudToGatewayMessage) {
		try {
			var jsonElement = new Gson().fromJson(cloudToGatewayMessage, JsonElement.class);
			var jsonObj = jsonElement.getAsJsonObject();

			var module = JsonUtil.getString(jsonObj, MODULE);
			var subType = JsonUtil.getString(jsonObj, SUBTYPE);
			var action = JsonUtil.getString(jsonObj, ACTION);
			var messageUuid = JsonUtil.getString(jsonObj, MESSAGE_ID);

			AbstractActionHandler handler = null;
			try {
				handler = getActionHandler(module, subType, action, cloudToGatewayMessage);
				if(handler == null) {
					LOG.error("Handler not found for Module:{}, SubType:{}, Action:{}", module,subType,action);
				}
				if (handler != null) {
					handler.perform();
				} 
			}catch (Exception e) {
				e.printStackTrace();
				LOG.error("{} {}", e, e.getMessage());
				LOG.error("Exception in handler Module:{}, SubType:{}, Action:{}", module,subType,action);
			} finally {
				if(handler != null) {
					handler.destroy();
					if(module.equalsIgnoreCase("Discovery") && subType.equalsIgnoreCase("Configuration") && action.equalsIgnoreCase("Update")) {
						FilteredResourceRegistry.getInstance().remove(messageUuid);
					}
				}
			}
		} catch (Exception e) {
			LOG.error(e.getMessage(), e);
		}
	}
}