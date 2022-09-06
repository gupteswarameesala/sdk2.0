package com.opsramp.gateway.app.domain;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.opsramp.app.content.core.handlers.context.RequestContext;
import com.opsramp.app.content.core.payload.DiscoveryPayload;
import com.opsramp.app.content.core.payload.RelationShip;
import com.opsramp.app.content.core.payload.Resource;
import com.opsramp.app.content.core.publisher.HttpRequestUtil;
import com.opsramp.app.content.util.JsonUtil;
import com.opsramp.app.processor.handlers.DiscoveryHandler;

public class TargetDiscovery {
	private static final Logger LOG = LoggerFactory.getLogger(TargetDiscovery.class);
    {% for nt in nativeType %}
	public DiscoveryPayload get{{nt['nativeType'].title().replace(" ", "")}}Data(RequestContext requestContext,String resourceType) {
		return null;
	}
	{%endfor%}
}