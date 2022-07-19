package com.opsramp.app.processor.handlers;

import java.util.HashMap;
import java.util.Map;
import java.util.Set;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.opsramp.app.content.core.actionhandler.AbstractActionHandler;
import com.opsramp.app.content.core.actionhandler.ActionRegistry;
import com.opsramp.app.content.core.actionhandler.ConfigurationCache;
import com.opsramp.app.content.core.actionhandler.ConfigurationLoader;
import com.opsramp.app.content.core.actionhandler.ResourceTypeRegistry;
import com.opsramp.app.content.core.alert.NativeTypeMetricLoader;
import com.opsramp.app.content.core.debug.handler.DebugRegistry;
import com.opsramp.app.content.util.JsonUtil;
import com.opsramp.app.processor.handlers.debug.DeviceReachability;
{% for i in dm_dic["discovery"].split(",") %}
import com.opsramp.gateway.app.actions.impl.discovery.{{ i }};
{% endfor %}
{% for i in dm_dic["monitoring"].split(",") %}
import com.opsramp.gateway.app.actions.impl.monitor.{{ i }};
{% endfor %}
import com.opsramp.gateway.app.util.AppConstants;

public class GenericMessageHandler {

	private static final Logger LOG = LoggerFactory.getLogger(GenericMessageHandler.class);

	private static final String ACTION = "action";
	private static final String MODULE = "module";
	private static final String SUBTYPE = "subtype";

	/**
	 * @param module
	 * @param subType
	 * @param action
	 * @param cloudToGatewayReq
	 * @return
	 * @throws Exception
	 */
	public AbstractActionHandler getActionHandler(String module, String subType, String action,
			String cloudToGatewayReq) throws Exception {
		var handler = String.format("%s-%s-%s", module, subType, action);

		LOG.info("Recieved app message :{}, {}", handler, cloudToGatewayReq);
		LOG.debug("GenericMessageHandler# getActionHandler# call started.. handler :{} ", handler);
		try {
			Class<? extends AbstractActionHandler> handlerClass = ActionRegistry.getHandler(handler);
			AbstractActionHandler handlerObject = handlerClass.getDeclaredConstructor().newInstance();

			if (module.equalsIgnoreCase(AppConstants.MONITORING) && subType.equalsIgnoreCase(AppConstants.CONFIGURATION)
					&& action.equalsIgnoreCase(AppConstants.UPDATE)) {
				var jsonElement = new Gson().fromJson(cloudToGatewayReq, JsonElement.class);
				var jsonObj = jsonElement.getAsJsonObject();

				LOG.debug("Monitoring message recieved :{}", jsonElement.toString());
				JsonObject payloadObject = JsonUtil.getJson(jsonObj, AppConstants.PAYLOAD);
				String templateID = JsonUtil.getString(payloadObject, AppConstants.TEMPLATEID);
				String templateShaValue = JsonUtil.getString(payloadObject,  AppConstants.TEMPLATESHAVALUE);
				String monitorId = JsonUtil.getString(payloadObject,  AppConstants.MONITORID);

				String templateObject = ConfigurationLoader.load(ConfigurationCache.MONITORING, templateID,
						templateShaValue);
				var templateJsonElement = new Gson().fromJson(templateObject, JsonElement.class);

				// Construct App Monitoring Request
				String monitoringPayload = constructAppMonitoringRequest(jsonObj, templateID, monitorId,
						templateJsonElement);
				handlerObject.setRequestContext(monitoringPayload);

				// Load Alert Definitions
				NativeTypeMetricLoader.getInstance().loadMetricConfiguration(templateID, monitorId, templateShaValue,
						templateJsonElement);

			} else if (module.equalsIgnoreCase(AppConstants.DISCOVERY) && subType.equalsIgnoreCase(AppConstants.CONFIGURATION)
					&& action.equalsIgnoreCase(AppConstants.UPDATE)) {
				LOG.debug("Discovery message recieved  :{}", cloudToGatewayReq);
				handlerObject.setRequestContext(injectCredentialObject(cloudToGatewayReq));
			} else {
				LOG.debug("Message recieved with module:{},subtype:{},Action:{} ", module, subType, action);
				handlerObject.setRequestContext(cloudToGatewayReq);
			}
			LOG.debug("GenericMessageHandler# getActionHandler# call ended.. handlerObject :{} ", handlerObject);
			return handlerObject;

		} catch (Exception e) {
			// TODO: handle exception
			LOG.error(" Unable to process Action Handler, Reason :{}", e);
			throw e;
		}
	}

	/**
	 * @param jsonObj
	 * @param templateID
	 * @param monitorId
	 * @param templateJsonElement
	 * @return
	 */
	public String constructAppMonitoringRequest(JsonObject jsonObj, String templateID, String monitorId,
			JsonElement templateJsonElement) {
          LOG.debug("GenericMessageHandler# constructAppMonitoringRequest# method started");
		try {
			JsonObject payloadObject = JsonUtil.getJson(jsonObj, AppConstants.PAYLOAD);

			JsonArray newResourceJsonArray = new JsonArray();

			JsonElement appConfigRequestElement = JsonUtil.getElement(payloadObject, AppConstants.APPCONFIG);
			var appConfigRequestJsonObject = appConfigRequestElement.getAsJsonObject();

			String resourceAppConfigId = JsonUtil.getString(appConfigRequestJsonObject, AppConstants.APPCONFIGID);
			String resourceAppConfigIdShaValue = JsonUtil.getString(appConfigRequestJsonObject, AppConstants.APPCONFIGSHAVAL);

			Map<String, String> resourceAppConfigCredentialMap = new HashMap<String, String>();

			JsonElement resourceAppConfigCredentialElement = JsonUtil.getElement(appConfigRequestJsonObject,
					 AppConstants.CREDENTIAL);
			if (resourceAppConfigCredentialElement != null) {
				JsonArray resourceAppConfigCredentialJsonArray = resourceAppConfigCredentialElement.getAsJsonArray();
				if (resourceAppConfigCredentialJsonArray != null && resourceAppConfigCredentialJsonArray.size() > 0) {
					for (JsonElement resourceAppConfigCredential : resourceAppConfigCredentialJsonArray) {
						JsonObject resourceAppConfigCredentialJsonObject = resourceAppConfigCredential
								.getAsJsonObject();
						resourceAppConfigCredentialMap.put(
								JsonUtil.getString(resourceAppConfigCredentialJsonObject,  AppConstants.CREDENTIALID),
								JsonUtil.getString(resourceAppConfigCredentialJsonObject, AppConstants.SHAVALUE));
					}
				}
			}

			// Loading Discovery Configuration with Credentials
			String discoveryConfigurationObj = ConfigurationLoader.load(ConfigurationCache.DISCOVERY,
					resourceAppConfigId, resourceAppConfigIdShaValue);
			JsonObject discoveryConfigurationJsonObject = null;
			if (discoveryConfigurationObj != null) {
				var discoveryConfigurationElement = new Gson().fromJson(discoveryConfigurationObj, JsonElement.class);
				discoveryConfigurationJsonObject = discoveryConfigurationElement.getAsJsonObject();

				JsonObject dbDiscoveryConfigurationPayloadJsonObject = JsonUtil
						.getJson(discoveryConfigurationJsonObject, AppConstants.PAYLOAD);
				JsonObject discoveryConfigurationDataJsonObject = JsonUtil
						.getJson(dbDiscoveryConfigurationPayloadJsonObject, AppConstants.DATA);
				JsonElement credentialElement = JsonUtil.getElement(discoveryConfigurationDataJsonObject,
						AppConstants.CREDENTIALID);

				if (credentialElement != null) {
					JsonArray newCredentialJsonArray = new JsonArray();

					JsonArray credentialJsonArray = credentialElement.getAsJsonArray();
					if (credentialJsonArray != null && credentialJsonArray.size() > 0) {
						for (JsonElement credentialArray : credentialJsonArray) {
							String credentialId = credentialArray.getAsString();

							JsonObject newCredentialJsonObject = new JsonObject();
							newCredentialJsonObject.addProperty(AppConstants.CREDENTIALID, credentialId);

							String credentialConfigurationObj = ConfigurationLoader.load(ConfigurationCache.CREDENTIAL,
									credentialId, resourceAppConfigCredentialMap.get(credentialId));
							if (credentialConfigurationObj != null) {
								var newcredentialConfigurationObjElement = new Gson()
										.fromJson(credentialConfigurationObj, JsonElement.class);
								var newcredentialConfigurationJsonObj = newcredentialConfigurationObjElement
										.getAsJsonObject();
								newCredentialJsonObject.add(AppConstants.CREDENTIALVALUE,
										JsonUtil.getJson(newcredentialConfigurationJsonObj, AppConstants.PAYLOAD));
							}
							newCredentialJsonArray.add(newCredentialJsonObject);
						}
					}
					discoveryConfigurationDataJsonObject.remove(AppConstants.CREDENTIALID);
					discoveryConfigurationDataJsonObject.add(AppConstants.CREDENTIAL, newCredentialJsonArray);
				}
			}

			// Loading Resource Objects
			JsonElement resourceElement = JsonUtil.getElement(payloadObject,  AppConstants.RESOURCES);

			if (resourceElement != null) {
				JsonArray resourceArrayJson = resourceElement.getAsJsonArray();
				if (resourceArrayJson != null && resourceArrayJson.size() > 0) {
					for (JsonElement resourceArray : resourceArrayJson) {

						JsonObject resourceJsonObject = resourceArray.getAsJsonObject();
						String resourceId = JsonUtil.getString(resourceJsonObject,  AppConstants.RESOURCEID);
						String resourceShaValue = JsonUtil.getString(resourceJsonObject, AppConstants.RESOURCESHAVALUE);

						// Scheduler Resource Credential Payload
						Map<String, String> resourceCredentialMap = new HashMap<String, String>();
						JsonElement resourceCredentialElement = JsonUtil.getElement(resourceJsonObject, AppConstants.CREDENTIAL);
						if (resourceCredentialElement != null) {
							JsonArray resourceCredentialJsonArray = resourceCredentialElement.getAsJsonArray();
							if (resourceCredentialJsonArray != null && resourceCredentialJsonArray.size() > 0) {
								for (JsonElement resourceCredential : resourceCredentialJsonArray) {
									JsonObject resourceCredentialJsonObject = resourceCredential.getAsJsonObject();
									resourceCredentialMap.put(
											JsonUtil.getString(resourceCredentialJsonObject, AppConstants.CREDENTIALID),
											JsonUtil.getString(resourceCredentialJsonObject, AppConstants.SHAVALUE));
								}
							}
						}

						String resourceObject = ConfigurationLoader.load(ConfigurationCache.RESOURCE, resourceId,
								resourceShaValue);

						if (resourceObject != null) {
							var resourceObjectElement = new Gson().fromJson(resourceObject, JsonElement.class);
							var resourceDbJsonObject = resourceObjectElement.getAsJsonObject();

							JsonObject dbPayloadObject = JsonUtil.getJson(resourceDbJsonObject, AppConstants.PAYLOAD);
							JsonObject dbResourcesObject = JsonUtil.getJson(dbPayloadObject, AppConstants.RESOURCES);
							// Loading Resource Credentials
							JsonElement dbResourceCredentialElement = JsonUtil.getElement(dbResourcesObject,
									AppConstants.CREDENTIALID);

							if (dbResourceCredentialElement != null) {
								JsonArray newResourceCredentialJsonArray = new JsonArray();

								JsonArray dbResourceCredentialJsonArray = dbResourceCredentialElement.getAsJsonArray();
								if (dbResourceCredentialJsonArray != null && dbResourceCredentialJsonArray.size() > 0) {
									for (JsonElement dbCredentialArray : dbResourceCredentialJsonArray) {
										String credentialId = dbCredentialArray.getAsString();

										JsonObject newResourceCredentialJsonObject = new JsonObject();
										newResourceCredentialJsonObject.addProperty(AppConstants.CREDENTIALID, credentialId);

										String resourceCredentialConfigurationObj = ConfigurationLoader.load(
												ConfigurationCache.CREDENTIAL, credentialId,
												resourceCredentialMap.get(credentialId));
										if (resourceCredentialConfigurationObj != null) {
											var newResourceCredentialConfigurationObjElement = new Gson()
													.fromJson(resourceCredentialConfigurationObj, JsonElement.class);
											var newResourceCredentialConfigurationJsonObj = newResourceCredentialConfigurationObjElement
													.getAsJsonObject();
											newResourceCredentialJsonObject.add(AppConstants.CREDENTIALVALUE, JsonUtil
													.getJson(newResourceCredentialConfigurationJsonObj, AppConstants.PAYLOAD));
										}
										newResourceCredentialJsonArray.add(newResourceCredentialJsonObject);
									}
								}
								dbResourcesObject.remove(AppConstants.CREDENTIALID);
								dbResourcesObject.add(AppConstants.CREDENTIAL, newResourceCredentialJsonArray);
							}
							// newResourceJsonArray.add(resourceDbJsonObject);
							newResourceJsonArray.add(dbPayloadObject);
						}
					}
				}
			}

			var templateJsonObject = templateJsonElement.getAsJsonObject();
			var templatePayloadObject = JsonUtil.getJson(templateJsonObject, AppConstants.PAYLOAD);

			String nativeType = JsonUtil.getString(templatePayloadObject, AppConstants.NATIVE_TYPE);

			JsonArray metricJsonArray = new JsonArray();

			var monitorObject = JsonUtil.getJson(templatePayloadObject, AppConstants.MONITORS);
			if (monitorObject != null) {
				Set<Map.Entry<String, JsonElement>> monitors = monitorObject.entrySet();
				if (monitors != null && monitors.size() > 0) {
					for (Map.Entry<String, JsonElement> monitor : monitors) {
						// String monitorName = monitor.getKey();
						JsonElement monitorValue = monitor.getValue();
						var monitorJsonObject = monitorValue.getAsJsonObject();

						String monId = JsonUtil.getString(monitorJsonObject, AppConstants.UUID);
						if (monitorId.equalsIgnoreCase(monId)) {
							JsonObject metricsJsonObject = JsonUtil.getJson(monitorJsonObject, AppConstants.METRICS);

							Set<Map.Entry<String, JsonElement>> metrics = metricsJsonObject.entrySet();
							for (Map.Entry<String, JsonElement> metric : metrics) {
								metricJsonArray.add(metric.getKey());
							}
						}
					}
				}
			}

			JsonObject appRequestObject = new JsonObject();

			appRequestObject.addProperty(AppConstants.MESSAGEID, JsonUtil.getString(jsonObj, AppConstants.MESSAGEID));
			appRequestObject.addProperty(MODULE, JsonUtil.getString(jsonObj, MODULE));
			appRequestObject.addProperty(SUBTYPE, JsonUtil.getString(jsonObj, SUBTYPE));
			appRequestObject.addProperty(ACTION, JsonUtil.getString(jsonObj, ACTION));
			appRequestObject.addProperty(AppConstants.APPINTEGRATIONID,
					JsonUtil.getString(discoveryConfigurationJsonObject, AppConstants.APPINTEGRATIONID));
			appRequestObject.addProperty(AppConstants.CONFIGURATIONID,
					JsonUtil.getString(discoveryConfigurationJsonObject, AppConstants.CONFIGURATIONID));
			appRequestObject.addProperty(AppConstants.CONFIGURATIONNAME,
					JsonUtil.getString(discoveryConfigurationJsonObject, AppConstants.CONFIGURATIONNAME));
			appRequestObject.addProperty(AppConstants.MANAGEMENTPROFILEID,
					JsonUtil.getString(discoveryConfigurationJsonObject, AppConstants.MANAGEMENTPROFILEID));

			JsonObject appRequestPayloadObject = new JsonObject();

			appRequestPayloadObject.add(AppConstants.TEMPLATE, templateJsonElement);
			appRequestPayloadObject.addProperty(AppConstants.TEMPLATEID, templateID);
			appRequestPayloadObject.addProperty(AppConstants.MONITORID, monitorId);
			appRequestPayloadObject.add(AppConstants.APPCONFIG, JsonUtil.getJson(discoveryConfigurationJsonObject, AppConstants.PAYLOAD));

			JsonObject nativeTypeObjectValue = new JsonObject();
			nativeTypeObjectValue.add(nativeType, metricJsonArray);

			appRequestPayloadObject.add(AppConstants.NATIVE_TYPE, nativeTypeObjectValue);
			appRequestPayloadObject.add(AppConstants.RESOURCES, newResourceJsonArray);

			appRequestObject.add("payload", appRequestPayloadObject);
	        LOG.debug("GenericMessageHandler# constructAppMonitoringRequest# method ended");
			return appRequestObject.toString();
		} catch (Exception e) {
			LOG.error("Unable to construct App Monitoring Request , Reason :{}", e);
			throw e;
		}
	}

	/**
	 * @param cloudToGatewayReq
	 * @return
	 */
	private String injectCredentialObject(String cloudToGatewayReq) {
        LOG.debug("GenericMessageHandler# injectCredentialObject# method started");
      try {
		var jsonElement = new Gson().fromJson(cloudToGatewayReq, JsonElement.class);
		var jsonObj = jsonElement.getAsJsonObject();

		String configurationId = JsonUtil.getString(jsonObj, AppConstants.CONFIGURATIONID);
		String sha = JsonUtil.getString(jsonObj, "sha");
		ConfigurationLoader.load(ConfigurationCache.DISCOVERY, configurationId, sha);

		JsonObject payloadObject = JsonUtil.getJson(jsonObj, AppConstants.PAYLOAD);
		var dataObj = JsonUtil.getJson(payloadObject, AppConstants.DATA);

		JsonElement credentialIdElement = JsonUtil.getElement(dataObj, AppConstants.CREDENTIAL);
		if (credentialIdElement != null) {
			JsonArray modifiedCredential = new JsonArray();

			JsonArray credentialArray = credentialIdElement.getAsJsonArray();
			if (credentialArray != null && credentialArray.size() > 0) {
				for (JsonElement credentialArr : credentialArray) {
					JsonObject credentialJsonObject = credentialArr.getAsJsonObject();
					String credentialId = JsonUtil.getString(credentialJsonObject, AppConstants.CREDENTIALID);
					String shaValue = JsonUtil.getString(credentialJsonObject, AppConstants.SHAVALUE);

					String dbCredentialObject = ConfigurationLoader.load(ConfigurationCache.CREDENTIAL, credentialId,
							shaValue);
					var dbCredentialJsonElement = new Gson().fromJson(dbCredentialObject, JsonElement.class);
					var dbCredentialJsonObject = dbCredentialJsonElement.getAsJsonObject();

					JsonObject newCredentialJsonObject = new JsonObject();
					newCredentialJsonObject.addProperty(AppConstants.CREDENTIALID, credentialId);
					newCredentialJsonObject.add(AppConstants.CREDENTIALVALUE, JsonUtil.getJson(dbCredentialJsonObject, AppConstants.PAYLOAD));

					modifiedCredential.add(newCredentialJsonObject);
				}
			}
			if (modifiedCredential != null && modifiedCredential.size() > 0) {
				dataObj.remove(AppConstants.CREDENTIALID);
				dataObj.add(AppConstants.CREDENTIAL, modifiedCredential);
			}
		}
        LOG.debug("GenericMessageHandler# injectCredentialObject# method ended");
		return jsonElement.toString();
      }catch (Exception e) {
		LOG.error("Failed to inject Credential Object, Reason :{}",e);
		throw e;
	}
	}

	public static String getDiscoveryIdentity() {
		return String.format("%s-%s-%s", AppConstants.DISCOVERY, AppConstants.CONFIGURATION, AppConstants.UPDATE);
	}

	public static String getMonitoringIdentity() {
		return String.format("%s-%s-%s", AppConstants.MONITORING, AppConstants.CONFIGURATION, AppConstants.UPDATE);
	}

	public static String getResourceAckIdentity() {
		return String.format("%s-%s-%s", "App", "RESOURCE", AppConstants.ACK);
	}

	public static void registerActions() {
		ActionRegistry.registerAction(GenericMessageHandler.getDiscoveryIdentity(), DiscoveryHandler.class);
		ActionRegistry.registerAction(GenericMessageHandler.getMonitoringIdentity(), MonitoringHandler.class);
		ActionRegistry.registerAction(GenericMessageHandler.getResourceAckIdentity(), ResourceAckHandler.class);

		DebugRegistry.registerAction("Reachability", DeviceReachability.class);

		ResourceTypeRegistry.registerDiscoveryEntites({{dm_dic["discoveryclass"]}});
		{% for key,val in dm_dic["monitoringmap"].items()%}
		ResourceTypeRegistry.registerMonitoringEntity("{{key}}", {{val}}.class);
		{%endfor%}
	}

}
