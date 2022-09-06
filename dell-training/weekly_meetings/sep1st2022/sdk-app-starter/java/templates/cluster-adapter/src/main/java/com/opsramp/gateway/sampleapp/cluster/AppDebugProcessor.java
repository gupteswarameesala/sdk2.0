package com.opsramp.gateway.{{res}}.cluster;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.google.gson.Gson;
import com.opsramp.app.content.core.debug.handler.AbstractDebugHandler;
import com.opsramp.app.content.core.debug.handler.DebugRegistry;
import com.opsramp.app.content.core.debug.handler.DebugRequest;
import com.opsramp.app.content.core.debug.handler.DebugResponse;
import com.opsramp.gateway.common.core.GenericResponse;
import com.opsramp.gateway.common.listener.DebugProcessor;


public class AppDebugProcessor implements DebugProcessor{
	
	private static final Logger LOG = LoggerFactory.getLogger(AppDebugProcessor.class);

	@Override
	public String debug(String request) {

		DebugRequest cloudToGatewayRequest = new Gson().fromJson(request, DebugRequest.class);

		AbstractDebugHandler handler = null;
		DebugResponse response = null;
		try {
			handler = getActionHandler(cloudToGatewayRequest);
			if (handler != null) {
				response = handler.perform();
			}else {
				response = new DebugResponse(GenericResponse.ERROR, "No Debug handler found for this request");
			}
		}catch (Exception e) {
			LOG.error("Exception during debug request: {}", e);
			response = new DebugResponse(GenericResponse.ERROR, "Exception during debug request");
		} finally {
			handler.destroy();
		}
		return new Gson().toJson(response);
	}
	
	private AbstractDebugHandler getActionHandler(DebugRequest cloudToGatewayReq) throws Exception{
		String action = cloudToGatewayReq.getAction();
		Class<? extends AbstractDebugHandler> handlerClass = DebugRegistry.getHandler(action);
		AbstractDebugHandler discoveryObj = handlerClass.getDeclaredConstructor().newInstance();
		discoveryObj.setRequestContext(cloudToGatewayReq);
		return discoveryObj;
}

}
