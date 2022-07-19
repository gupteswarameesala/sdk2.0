package com.opsramp.gateway.app.actions.impl.discovery;

import java.util.Map;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import com.google.gson.Gson;
import com.opsramp.app.content.core.actions.Discovery;
import com.opsramp.app.content.core.handlers.context.RequestContext;
import com.opsramp.app.content.core.payload.DiscoveryPayload;
import com.opsramp.app.content.core.publisher.AppPublisher;
import com.opsramp.gateway.app.domain.TargetDiscovery;
import com.opsramp.gateway.app.util.AppConstants;

public class {{nativeType}}Discovery implements Discovery {

	private static final Logger LOG = LoggerFactory.getLogger({{nativeType}}Discovery.class);

	public {{nativeType}}Discovery() {

	}

	public void discover(RequestContext requestContext) throws Exception {
	LOG.debug("{{nativeType}} Discovery# discover# call started..");
	try {

		@SuppressWarnings("unchecked")
		Map<String,String> nativeTypeMap = (Map<String,String>) requestContext.getContext().get(AppConstants.NATIVETYPES);
		String resourceType = nativeTypeMap.get("{{ntName}}");

		LOG.debug(" CALLING TARGET {{nativeType}} DISCOVERY RequestContext {} , ResourceType {} " , requestContext , resourceType);

		DiscoveryPayload dp = new TargetDiscovery().get{{nativeType}}Data(requestContext, resourceType);
		String messageId = (String) requestContext.getContext().get(AppConstants.MESSAGEID);
		String configurationId = (String) requestContext.getContext().get(AppConstants.CONFIGURATIONID);

		//Relationship Filtering started
		DiscoveryUtil.getResourceFilteredResponse(dp, messageId, configurationId,"{{ntName}}");
		//Relationship Filtering ended

		//Relationship Filtering started
		DiscoveryUtil.getRelationshipFilteredResponse(dp, messageId);
		//Relationship Filtering ended


		if(dp != null) {
			LOG.debug("{{nativeType}} Discovery:{}", new Gson().toJson(dp));
			if(dp.getResource() != null) {
				AppPublisher.publishResources(requestContext, dp.getResource());

				if(dp.getRelationship() != null) {
					AppPublisher.publishRelationShip(requestContext, dp.getRelationship());
				}
			}
		}
		else {
				LOG.error("{{nativeType}} Discovery is null");
			}
			LOG.debug("{{nativeType}} Discovery# discover# call ended..");
		}
		catch (Exception e) {
			LOG.error("Failed to process get discovery data, Reason :{}", e);
			throw e;
		}
    }

}
