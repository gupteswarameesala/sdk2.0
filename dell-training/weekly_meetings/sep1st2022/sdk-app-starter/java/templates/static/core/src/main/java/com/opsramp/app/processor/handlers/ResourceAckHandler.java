package com.opsramp.app.processor.handlers;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.opsramp.app.content.core.actionhandler.AbstractActionHandler;
import com.opsramp.app.content.util.MoIdUtil;
import com.opsramp.gateway.app.util.AppConstants;

public class ResourceAckHandler extends AbstractActionHandler {

	private static final Logger LOG = LoggerFactory.getLogger(ResourceAckHandler.class);

	public ResourceAckHandler(String cloudRequest) {
		setRequestContext(cloudRequest);
	}

	public ResourceAckHandler() {
		LOG.debug(" CALLING RESOURCEACK DEFAULT CONSTRRUCTOR ");
	}

	@Override
	public void perform() {
		LOG.debug("ResourceAckHandler# perform# call started");
		LOG.debug("Received ResourceAckHandler Message Request {} ", this.requestContext.getRequest());

		try {
			var jsonElement = new Gson().fromJson((String) this.requestContext.getRequest(), JsonElement.class);
			JsonObject ackJsonObject = jsonElement.getAsJsonObject();
			String configId = ackJsonObject.get(AppConstants.CONFIGID).getAsString();
			JsonArray payloadJsonArray = ackJsonObject.get(AppConstants.PAYLOAD).getAsJsonArray();
			for (int i = 0; i < payloadJsonArray.size(); i++) {
				JsonObject ackObj = payloadJsonArray.get(i).getAsJsonObject();
				String resourceUUID = ackObj.get(AppConstants.RESOURCEUUID).getAsString();
				String moId = ackObj.get(AppConstants.MOID).getAsString();
				LOG.debug("received ack. {}", ackObj.toString());
				// ServiceFactory.getCacheStore().put("RESOURCE_ACK_STORE", moId, resourceUUID);
				MoIdUtil.saveMoId(configId, moId, resourceUUID);
				// MoIdUtil.getResourceId(moId);
				// MoIdUtil.removeMoId(moId);
			}
			LOG.debug("ResourceAckHandler# perform# call ended");
		} catch (Exception e) {
			LOG.error("Failed to save resource uuids in cache, Reason :{}", e);
		}
	}

}