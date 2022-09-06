from core import AbstractDiscovery, Constants, GatewayToCloudMessage
import logging
from target import TargetDiscovery
logger = logging.getLogger(__name__)

class DellPowerflexProtectionDomainDiscovery(AbstractDiscovery):

      def discover(self, requestContext):
          try:
              logger.debug("DellPowerflexProtectionDomain discovery stared")
              try:
                resource_type = requestContext.context.get("resourceTypes")["Dell PowerFlex Protection Domain"]
              except Exception as KeyError:
                  resource_type = None
              DellPowerflexProtectionDomain_list,relation_list = TargetDiscovery().get_DellPowerflexProtectionDomain_data(requestContext, resource_type)

              logger.debug("DellPowerflexProtectionDomain discoverey json " + str(DellPowerflexProtectionDomain_list))
              logger.debug(" relationship json " + str(relation_list))

              if DellPowerflexProtectionDomain_list != None and resource_type != None and len(DellPowerflexProtectionDomain_list)>0:
                http_headers = requestContext.context.get('http_headers')
                http_headers['AM-App-Native-Type'] = "Dell PowerFlex Protection Domain"
                requestContext.context["http_headers"] = http_headers
                GatewayToCloudMessage.publish_resources(requestContext.context.get("http_headers"),  DellPowerflexProtectionDomain_list)

                if relation_list != None and len(relation_list)>0:
                    GatewayToCloudMessage.publish_relationships(requestContext.context.get("http_headers"),
                                                                relation_list)
              else:
                  logger.info("DellPowerflexProtectionDomain disocvery is null ")


          except Exception as e:
              raise Exception(str(e))