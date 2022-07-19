package com.opsramp.gateway.{{res}}.cluster;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.google.gson.Gson;
import com.google.gson.JsonElement;
import com.opsramp.app.content.core.actionhandler.AbstractActionHandler;
import com.opsramp.app.content.core.integration.FilteredResourceRegistry;
import com.opsramp.app.processor.handlers.GenericMessageHandler;
import com.opsramp.gateway.common.core.GenericResponse;
import com.opsramp.gateway.common.listener.Processor;
import com.opsramp.gateway.utils.JsonUtil;

public class ApplicationProcessor extends GenericMessageHandler implements Processor{
	private static final Logger LOG = LoggerFactory.getLogger(ApplicationProcessor.class);

	private static final String ACTION = "action";
	private static final String MESSAGE_ID = "messageId";
	private static final String MODULE = "module";
	private static final String SUBTYPE = "subtype";

	@Override
	public GenericResponse run(String queueName, String request) {
		//CloudToGatewayRequest cloudToGatewayRequest = new Gson().fromJson(request, CloudToGatewayRequest.class);

		/*if (cloudToGatewayRequest != null 
				&& cloudToGatewayRequest.getAction() != null
				&& !cloudToGatewayRequest.getAction().isBlank()) {*/
		var jsonElement = new Gson().fromJson(request, JsonElement.class);
		var jsonObj = jsonElement.getAsJsonObject();

		var module = JsonUtil.getString(jsonObj, MODULE);
		var subType = JsonUtil.getString(jsonObj, SUBTYPE);
		var action = JsonUtil.getString(jsonObj, ACTION);
		var messageUuid = JsonUtil.getString(jsonObj, MESSAGE_ID);
		
		// Ignoring Ack Message as part of SDK v2, Need to review with team and clear this message from cloud
//		if(action.equalsIgnoreCase("ACK")) {
//			return new GenericResponse(JsonUtil.getString(jsonObj, "id"), GenericResponse.OK);
//		}

		AbstractActionHandler handler = null;
		try {
			handler = getActionHandler(module, subType, action, request);
			if(handler == null) {
				LOG.error("Handler not found for Module:{}, SubType:{}, Action:{}", module,subType,action);
				return new GenericResponse(messageUuid, GenericResponse.ERROR);
			}
			if (handler != null) {
				handler.perform();
				return new GenericResponse(messageUuid, GenericResponse.OK);
			} 
		}catch (Exception e) {
			e.printStackTrace();
			LOG.error("{} {}", e, e.getMessage());
			LOG.error("Exception in handler Module:{}, SubType:{}, Action:{}", module,subType,action);
			return new GenericResponse(messageUuid, GenericResponse.ERROR);
		} finally {
			if(handler != null) {
				handler.destroy();
				if(module.equalsIgnoreCase("Discovery") && subType.equalsIgnoreCase("Configuration") && action.equalsIgnoreCase("Update")) {
					FilteredResourceRegistry.getInstance().remove(messageUuid);
				}
			}
		}
		//}

		//should replace null object
		return new GenericResponse(messageUuid, GenericResponse.OK);
	}
}
