package com.opsramp.gateway.app.actions.impl.monitor;

import java.util.ArrayList;
import java.util.List;

import org.slf4j.LoggerFactory;

import com.opsramp.app.content.core.alerthandler.AlertData;
import com.opsramp.app.content.core.alerthandler.AlertUtils;
import com.opsramp.app.content.core.alerthandler.MetricResponse;
import com.opsramp.app.content.core.alerthandler.ResourceMetricData;
import com.opsramp.app.content.core.handlers.context.RequestContext;
import com.opsramp.app.content.core.payload.MetricPayload;
import com.opsramp.app.content.core.publisher.AppPublisher;
import com.opsramp.gateway.app.util.AppConstants;

public class MonitoringUtil {
	private static final org.slf4j.Logger LOG = LoggerFactory.getLogger(MonitoringUtil.class);

	/**
	 * @param requestContext
	 * @param metricPayloads
	 * @throws Exception
	 */
	public static void publishMetricsandAlerts(RequestContext requestContext, List<MetricPayload> metricPayloads)
			throws Exception {
		LOG.debug("MonitoringUtil# publishMetricsandAlerts# call started");
		try {
		String resourceType = (String) requestContext.getContext().get(AppConstants.NATIVE_TYPE);
		String templateId = (String) requestContext.getContext().get(AppConstants.TEMPLATEID);
		String monitorId = (String) requestContext.getContext().get(AppConstants.MONITORID);
		
		for(MetricPayload metricPayload: metricPayloads) {
			List<MetricResponse> metricResponseList = AlertUtils.publishAlerts(templateId, monitorId, resourceType, metricPayload.getId(), metricPayload.getData());
			List<ResourceMetricData> rmdList = new ArrayList<ResourceMetricData>();
			List<AlertData> adList = new ArrayList<AlertData>();
			for(MetricResponse metricResponse : metricResponseList) {
				rmdList.add(metricResponse.getMetricData());
				if(metricResponse.getAlertData() != null) {
					adList.add(metricResponse.getAlertData());
				}
			}
			
			MetricPayload finalMetricPayload = new MetricPayload();
			finalMetricPayload.setId(metricPayload.getId());
			finalMetricPayload.setData(rmdList);
			LOG.debug("finalMetricPayload :{}"+finalMetricPayload.toString());
			AppPublisher.publishMetrics(requestContext, finalMetricPayload);
			LOG.debug("alertdataList :{}"+adList.toString());
			AppPublisher.publishAlerts(requestContext, adList);
			LOG.debug("MonitoringUtil# publishMetricsandAlerts# call ended");

		}
		} catch (Exception e) {
			LOG.error("Failed to publish Metrics and Alerts, Reason :{}",e);
		}
	}

}
