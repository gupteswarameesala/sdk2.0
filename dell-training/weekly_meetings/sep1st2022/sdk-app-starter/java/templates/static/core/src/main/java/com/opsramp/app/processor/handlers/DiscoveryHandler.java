package com.opsramp.app.processor.handlers;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.HashMap;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.google.gson.Gson;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.opsramp.app.content.core.actionhandler.AbstractActionHandler;
import com.opsramp.app.content.core.actionhandler.ResourceTypeRegistry;
import com.opsramp.app.content.core.actions.Discovery;
import com.opsramp.app.content.core.handlers.processors.RelationShipProcessor;
import com.opsramp.app.content.core.integration.ServiceFactory;
import com.opsramp.app.content.core.payload.PayloadFactory;
import com.opsramp.app.content.core.payload.RelationShip;
import com.opsramp.app.content.core.response.g2c.FinalCloudResponse;
import com.opsramp.app.content.util.JsonUtil;
import com.opsramp.gateway.app.util.AppConstants;

public class DiscoveryHandler extends AbstractActionHandler {
	private static final Logger LOG = LoggerFactory.getLogger(DiscoveryHandler.class);

	public DiscoveryHandler(String cloudRequest) {
		setRequestContext(cloudRequest);
	}

	public DiscoveryHandler() {
		LOG.debug(" CALLING DISCOVERY DEFAULT CONSTRRUCTOR ");
	}

	@Override
	public void perform() {
		try {
			// Get the nativeType associated with the registered class.
			LOG.debug("DiscoveryHandler# perform# discovery request call started");

			var discoveryRequest = new Gson().fromJson(this.requestContext.getRequest(), JsonElement.class);
			if (discoveryRequest == null || discoveryRequest.isJsonNull()) {
				LOG.error("Discovery Request payload should not be null or empty, discoveryRequest :{}",
						discoveryRequest);
				throw new Exception("Discovery Request payload should not be null or empty");
			}
			JsonObject discoveryRequestObject = discoveryRequest.getAsJsonObject();

			LOG.debug("Discovery Request : {}", discoveryRequestObject.toString());
			String configurationId = JsonUtil.getString(discoveryRequestObject, AppConstants.CONFIGURATIONID);
			String appName = JsonUtil.getString(discoveryRequestObject, AppConstants.APP);
			String appIntegrationId = JsonUtil.getString(discoveryRequestObject, AppConstants.APPINTEGRATIONID);
			String managementProfileId = JsonUtil.getString(discoveryRequestObject, AppConstants.MANAGEMENTPROFILEID);
			String messageId = JsonUtil.getString(discoveryRequestObject, AppConstants.MESSAGEID);

			this.requestContext.getContext().put(AppConstants.CONFIGURATIONID, configurationId);
			this.requestContext.getContext().put(AppConstants.APPNAME, appName);
			this.requestContext.getContext().put(AppConstants.APPINTEGRATIONID, appIntegrationId);
			this.requestContext.getContext().put(AppConstants.MANAGEMENTPROFILEID, managementProfileId);
			this.requestContext.getContext().put(AppConstants.MESSAGEID, messageId);
			JsonObject payloadObject = JsonUtil.getJson(discoveryRequestObject, AppConstants.PAYLOAD);
			LOG.debug(" payloadObject sdkapp{} ", payloadObject);

			Map<String, String> resourceTypeMap = new HashMap<String, String>();

			JsonObject nativeTypesObject = JsonUtil.getJson(payloadObject, AppConstants.NATIVETYPES);
			if (nativeTypesObject != null) {
				Set<Map.Entry<String, JsonElement>> nativeTypes = nativeTypesObject.entrySet();
				if (nativeTypes != null) {
					for (Map.Entry<String, JsonElement> nativeType : nativeTypes) {
						LOG.debug(" payloadObject nativeType {} ", nativeType);

						JsonElement nativeTypeJsonElement = nativeType.getValue();
						JsonObject nativeTypeJsonObject = nativeTypeJsonElement.getAsJsonObject();
						resourceTypeMap.put(nativeType.getKey(),
								JsonUtil.getString(nativeTypeJsonObject, AppConstants.RESOURCETYPE));
					}
				}
			}

			LOG.debug("  ResourceMap Details {} ", resourceTypeMap);
			this.requestContext.getContext().put(AppConstants.NATIVETYPES, resourceTypeMap);
			this.requestContext.getContext().put(AppConstants.CURRENT_RESOURCESET, new ArrayList<String>());
			this.requestContext.getContext().put(AppConstants.CURRENT_RELATIONSHIPSET, new ArrayList<RelationShip>());

			// loop sequentially through the resource type impls registered at app startup.
			Set<Class<? extends Discovery>> entities = ResourceTypeRegistry.getDiscoveryEntities();
			LOG.debug("entities {} ", entities.toString());

			for (Class<? extends Discovery> discoveryClass : entities) {
				try {
					Discovery discoveryObj = discoveryClass.getDeclaredConstructor().newInstance();
					discoveryObj.discover(this.requestContext);
				} catch (Exception e) {
					LOG.error(e.getMessage(), e);
				}
			}

			// Process RelationShips.
			processRelationShips(appName, configurationId, appIntegrationId, managementProfileId);
			// RelationShip Delta
			// Device Delta
			processDeviceDelta(appName, configurationId, appIntegrationId, managementProfileId, configurationId);

		} catch (Exception e) {
			LOG.error("Failed to perform Discovery Request, Reason : {}" + e.getMessage(), e);
		}
		LOG.debug("DiscoveryHandler# perform# discovery request call ended");
	}

	/**
	 * @param appName
	 * @param configurationId
	 * @param appIntegrationId
	 * @param managementProfileId
	 */
	@SuppressWarnings("unchecked")
	private void processRelationShips(String appName, String configurationId, String appIntegrationId,
			String managementProfileId) {
		try {

			List<String> toBeDeletedSet = new ArrayList<String>();
			List<RelationShip> currentRelationshipKeys = ((ArrayList<RelationShip>) requestContext.getContext()
					.get("currentRelationshipSet"));

			String dbRelationships = ServiceFactory.getCacheStore()
					.get(appName + "_" + "realtionships" + "_" + configurationId, configurationId);
			LOG.debug("DB Relationships:{}", dbRelationships);
			String[] dbRelationshipsArray = null;
			if (dbRelationships != null && !dbRelationships.isEmpty()) {
				dbRelationshipsArray = dbRelationships.split("@,@");
			}

			List<String> dbRelationshipKeys = new ArrayList<String>();

			if (dbRelationshipsArray != null && dbRelationshipsArray.length > 0) {
				dbRelationshipKeys = Arrays.asList(dbRelationshipsArray);
			}

			Set<String> convertedCurrentRelationshipKeys = new HashSet<String>();
			List<RelationShip> toBeAddedRelationship = new ArrayList<RelationShip>();
			if (currentRelationshipKeys != null) {
				LOG.debug("Current Relationships:{}", new Gson().toJson(currentRelationshipKeys));
				for (RelationShip currentRelationshipKey : currentRelationshipKeys) {
					convertedCurrentRelationshipKeys.add(currentRelationshipKey.getSourceMoId() + "@_@"
							+ currentRelationshipKey.getType() + "@_@" + currentRelationshipKey.getTargetMoId());
					if (!dbRelationshipKeys.contains(currentRelationshipKey.getSourceMoId() + "_"
							+ currentRelationshipKey.getType() + "_" + currentRelationshipKey.getTargetMoId())) {
						toBeAddedRelationship.add(currentRelationshipKey);
					}
				}
			}

			if (dbRelationshipKeys != null && dbRelationshipKeys.size() > 0) {
				for (String dbRelationshipKey : dbRelationshipKeys) {
					if (!convertedCurrentRelationshipKeys.contains(dbRelationshipKey)) {
						toBeDeletedSet.add(dbRelationshipKey);
					}
				}
			}

			if (toBeAddedRelationship != null && !toBeAddedRelationship.isEmpty()) {
				LOG.debug("To be Added relationships :{}", new Gson().toJson(toBeAddedRelationship));
				RelationShipProcessor.getInstance().submit(appName, configurationId, appIntegrationId,
						managementProfileId, toBeAddedRelationship);
			}

			if (toBeDeletedSet != null && !toBeDeletedSet.isEmpty()) {
				Set<RelationShip> toBeDeletedRelationshipKeys = new HashSet<RelationShip>();
				for (String toBeDeleted : toBeDeletedSet) {
					String[] toBeDeletedArray = toBeDeleted.split("@_@");
					RelationShip relationship = new RelationShip();
					relationship.setSourceMoId(toBeDeletedArray[0]);
					relationship.setType(toBeDeletedArray[1]);
					relationship.setTargetMoId(toBeDeletedArray[2]);
					toBeDeletedRelationshipKeys.add(relationship);
				}

				FinalCloudResponse relationPayload = PayloadFactory.deleteRelationShipPayload(requestContext,
						new Gson().toJson(toBeDeletedRelationshipKeys));
				LOG.debug("final delete relationship response:{}", new Gson().toJson(toBeDeletedRelationshipKeys));
				ServiceFactory.getMessagePublisher().publish(new Gson().toJson(relationPayload));
			}

			if (convertedCurrentRelationshipKeys != null && !convertedCurrentRelationshipKeys.isEmpty()) {
				LOG.debug("Current Relationships:{}", convertedCurrentRelationshipKeys);
				ServiceFactory.getCacheStore().put(appName + "_" + "realtionships" + "_" + configurationId,
						configurationId, String.join("@,@", convertedCurrentRelationshipKeys));
			}
		} catch (Exception e) {
			LOG.error(e.getMessage(), e);
		}
	}

	/**
	 * @param appName
	 * @param configurationId
	 * @param appIntegrationId
	 * @param managementProfileId
	 * @param configurationId2
	 */
	@SuppressWarnings("unchecked")
	private void processDeviceDelta(String appName, String configurationId, String appIntegrationId,
			String managementProfileId, String configurationId2) {
		try {

			String dbResources = ServiceFactory.getCacheStore().get(appName + "_" + "resource" + "_" + configurationId,
					configurationId);
			LOG.debug("Existing DB Resources :{}", dbResources);
			List<String> currentResourceKeys = ((ArrayList<String>) requestContext.getContext()
					.get("currentResourceSet"));
			List<String> toBeDeletedSet = new ArrayList<String>();
			LOG.debug("Existing DB currentResourceKeys List :{}", currentResourceKeys.toString());

			if (dbResources != null) {
				String[] dbResourcesArray = dbResources.split("@,@");
				List<String> dbResourcesKeys = Arrays.asList(dbResourcesArray);
				LOG.debug("Existing DB dbResourcesKeys List :{}", dbResourcesKeys.toString());

				for (String dbResourceKey : dbResourcesKeys) {
					if (!currentResourceKeys.contains(dbResourceKey)) {
						toBeDeletedSet.add(dbResourceKey);
					}
				}
			}

			LOG.debug("To be deleted count :{}", toBeDeletedSet.size());

			if (toBeDeletedSet.size() > 0) {
				// send delete
				List<FinalCloudResponse> deleteResponse = PayloadFactory.newDeviceDeletePayload(appName,
						configurationId, appIntegrationId, managementProfileId, toBeDeletedSet);
				final Gson gson = new Gson();
				LOG.debug("deleteResponse ::" + deleteResponse.toString());
				deleteResponse.forEach(r -> {
					try {
						LOG.debug("gson.toJson(r) ::" + gson.toJson(r));
						ServiceFactory.getMessagePublisher().publish(gson.toJson(r));
					} catch (Exception e) {
						LOG.error(e.getMessage(), e);
					}
				});
			}

			if (currentResourceKeys != null && !currentResourceKeys.isEmpty()) {
				LOG.debug("Current Resources :{}", String.join("@,@", currentResourceKeys));
				ServiceFactory.getCacheStore().put(appName + "_" + "resource" + "_" + configurationId, configurationId,
						String.join("@,@", currentResourceKeys));
			}
		} catch (Exception e) {
			LOG.error(e.getMessage(), e);
		}

	}

}
