package com.opsramp.gateway.app.domain;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.Set;

import com.google.gson.Gson;
import com.google.gson.JsonArray;
import com.google.gson.JsonElement;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;
import com.opsramp.app.content.core.alerthandler.ResourceMetricData;
import com.opsramp.app.content.core.handlers.context.RequestContext;
import com.opsramp.app.content.core.payload.Metric;
import com.opsramp.app.content.core.payload.MetricPayload;
import com.opsramp.app.content.core.publisher.HttpRequestUtil;
import com.opsramp.app.content.util.JsonUtil;

public class TargetMonitoring {
    {% for nt in nativeType %}
	public List<MetricPayload> process{{nt['name'].title().replace(" ", "")}}Metrics(RequestContext requestContext) throws Exception {

		return null;
	}
	{%endfor%}
}
