package com.opsramp.app.processor.handlers;

import java.util.Set;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.google.gson.Gson;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.opsramp.app.content.core.actionhandler.AbstractActionHandler;
import com.opsramp.app.content.core.actionhandler.ResourceTypeRegistry;
import com.opsramp.app.content.core.actions.Monitoring;
import com.opsramp.app.content.util.JsonUtil;
import com.opsramp.gateway.app.util.AppConstants;

public class MonitoringHandler extends AbstractActionHandler {
	private static final Logger LOG = LoggerFactory.getLogger(MonitoringHandler.class);
	public MonitoringHandler(String cloudRequest) {
		setRequestContext(cloudRequest);
	}
	
	public MonitoringHandler() {
		LOG.debug(" CALLING MONITOR DEFAULT CONSTRRUCTOR ");
	}
	
	@Override
	public void perform() {
		LOG.debug("MonitoringHandler# perform# Monitoring request started.. ");
		try {
			var monitoringRequest = new Gson().fromJson(this.requestContext.getRequest(), JsonElement.class);
			var monitoringRequestObject = monitoringRequest.getAsJsonObject();
			var monitoringPayloadObject = JsonUtil.getJson(monitoringRequestObject, AppConstants.PAYLOAD);

			String configurationId = JsonUtil.getString(monitoringRequestObject.getAsJsonObject(), AppConstants.CONFIGURATIONID);
			String appIntegrationId = JsonUtil.getString(monitoringRequestObject.getAsJsonObject(), AppConstants.APPINTEGRATIONID);
			String managementProfileId = JsonUtil.getString(monitoringRequestObject.getAsJsonObject(),
					AppConstants.MANAGEMENTPROFILEID);
			JsonObject templatePayload = JsonUtil.getJson(monitoringPayloadObject.getAsJsonObject(), AppConstants.TEMPLATE);
			String appName = JsonUtil.getString(templatePayload, AppConstants.APP);

			this.requestContext.getContext().put(AppConstants.CONFIGURATIONID, configurationId);
			this.requestContext.getContext().put(AppConstants.APPNAME, appName);
			this.requestContext.getContext().put(AppConstants.APPINTEGRATIONID, appIntegrationId);
			this.requestContext.getContext().put(AppConstants.MANAGEMENTPROFILEID, managementProfileId);

			JsonObject nativeTypeObject = JsonUtil.getJson(monitoringPayloadObject, AppConstants.NATIVE_TYPE);
			LOG.debug("nativeTypeObject : {}", nativeTypeObject);
			String nativeType = null;
			if (nativeTypeObject != null) {
				Set<String> nativeTypes = nativeTypeObject.keySet();
				if (nativeTypes != null) {
					nativeType = nativeTypes.iterator().next();
				}
			}
			LOG.debug("nativeType : {}", nativeType);
			this.requestContext.getContext().put(AppConstants.NATIVE_TYPE, nativeType);
			this.requestContext.getContext().put(AppConstants.TEMPLATEID,
					JsonUtil.getString(monitoringPayloadObject, AppConstants.TEMPLATEID));
			this.requestContext.getContext().put(AppConstants.MONITORID, JsonUtil.getString(monitoringPayloadObject, AppConstants.MONITORID));

			Class<? extends Monitoring> monitoringEntity = ResourceTypeRegistry.getMonitoringEntity(nativeType);

			Monitoring monitorObj = monitoringEntity.getDeclaredConstructor().newInstance();
			monitorObj.monitor(this.requestContext);
		} catch (Exception e) {
			LOG.error("Failed to process monitor request, Reason :{}", e);
		}
		LOG.debug("MonitoringHandler# perform# Monitoring request ended.. ");
	}
}
