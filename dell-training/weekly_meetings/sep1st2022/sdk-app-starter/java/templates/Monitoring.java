package com.opsramp.gateway.app.actions.impl.monitor;

import java.util.List;

import com.opsramp.app.content.core.actions.Monitoring;
import com.opsramp.app.content.core.handlers.context.RequestContext;
import com.opsramp.app.content.core.payload.MetricPayload;
import com.opsramp.gateway.app.domain.TargetMonitoring;

public class {{nativeType}}Monitor implements Monitoring {

	public void monitor(RequestContext requestContext) throws Exception {
		List<MetricPayload> metricPayloads = new TargetMonitoring().process{{nativeType}}Metrics(requestContext);
		MonitoringUtil.publishMetricsandAlerts(requestContext, metricPayloads);
	}
}
