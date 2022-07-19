package com.opsramp.gateway.app.actions.impl.discovery;

import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.google.gson.Gson;
import com.google.gson.JsonObject;
import com.google.gson.reflect.TypeToken;
import com.opsramp.app.content.core.integration.RelationshipFilter;
import com.opsramp.app.content.core.integration.ResourceFilter;
import com.opsramp.app.content.core.payload.DiscoveryPayload;
import com.opsramp.app.content.core.payload.RelationShip;
import com.opsramp.app.content.core.payload.Resource;

public class DiscoveryUtil {
	private static final Logger LOG = LoggerFactory.getLogger(DiscoveryUtil.class);

	/**
	 * @param dp
	 * @param messageId
	 * @param configurationId
	 * @param nativeType
	 */
	public static void getResourceFilteredResponse(DiscoveryPayload dp, String messageId, String configurationId,
			String nativeType) {
		LOG.debug("DiscoveryUtil# getResourceFilteredResponse# call started");
		try {
			List<Resource> resources = dp.getResource();

			// Resource Filtering started
			String resourceListString = new Gson().toJson(resources);
			TypeToken<List<JsonObject>> list = new TypeToken<List<JsonObject>>() {
			};
			List<JsonObject> resourceJsonObjList = new Gson().fromJson(resourceListString, list.getType());

			ResourceFilter resourceFilter = new ResourceFilter(messageId, configurationId, nativeType,
					resourceJsonObjList);

			List<JsonObject> listOfResourceWithFilters = resourceFilter.filter();
			TypeToken<List<Resource>> finalResourceList = new TypeToken<List<Resource>>() {
			};
			List<Resource> filteredResourceList = new Gson().fromJson(new Gson().toJson(listOfResourceWithFilters),
					finalResourceList.getType());
			dp.setResource(filteredResourceList);
			LOG.debug("DiscoveryUtil# getResourceFilteredResponse# call ended");

		} catch (Exception e) {
			LOG.error("Failed to get Resource Filtered Response, Reason :{}", e);
			throw e;
		}
	}
	
	/**
	 * @param dp
	 * @param messageId
	 */
	public static void getRelationshipFilteredResponse(DiscoveryPayload dp, String messageId) {
		LOG.debug("DiscoveryUtil# getRelationshipFilteredResponse# call started");
		try {
			List<RelationShip> listOfRelationShips = dp.getRelationship();
			String relationListString = new Gson().toJson(listOfRelationShips);
			TypeToken<List<JsonObject>> typeToken = new TypeToken<List<JsonObject>>() {
			};
			List<JsonObject> relationJsonObjList = new Gson().fromJson(relationListString, typeToken.getType());

			RelationshipFilter relationshipFilter = new RelationshipFilter(messageId, relationJsonObjList);
			List<JsonObject> listOfRelationshipFilters = relationshipFilter.filter();

			TypeToken<List<RelationShip>> finalRelationshipList = new TypeToken<List<RelationShip>>() {
			};
			List<RelationShip> filteredRelationshipList = new Gson()
					.fromJson(new Gson().toJson(listOfRelationshipFilters), finalRelationshipList.getType());
			dp.setRelationship(filteredRelationshipList);
			LOG.debug("DiscoveryUtil# getRelationshipFilteredResponse# call ended");

		} catch (Exception e) {
			LOG.error("Failed to get Relationship Filtered Response, Reason :{}", e);
			throw e;
		}
	}
	
}
