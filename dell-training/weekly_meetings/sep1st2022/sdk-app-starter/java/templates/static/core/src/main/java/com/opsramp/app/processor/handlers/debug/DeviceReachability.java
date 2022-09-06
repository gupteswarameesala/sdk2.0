package com.opsramp.app.processor.handlers.debug;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.google.gson.Gson;
import com.opsramp.app.content.core.debug.handler.AbstractDebugHandler;
import com.opsramp.app.content.core.debug.handler.DebugRequest;
import com.opsramp.app.content.core.debug.handler.DebugResponse;

public class DeviceReachability extends  AbstractDebugHandler{
	
	private static final Logger LOG = LoggerFactory.getLogger(DeviceReachability.class);
	
	public DeviceReachability() {
		
	}

	@Override
	public DebugResponse perform() {
		DebugRequest dr = this.debugContext.getRequest();
		LOG.error("Debug Request:{}", new Gson().toJson(dr));
		
		DebugResponse drr = null;
		if(dr.getApiVersion().equals("1.0.0")) {
			drr = new DebugResponse(200, "Device Reached");
		}else if (dr.getApiVersion().equals("2.0.0")) {
			drr = new DebugResponse(500, "Device Not Reachable");
		}
		return drr;
	}

}
