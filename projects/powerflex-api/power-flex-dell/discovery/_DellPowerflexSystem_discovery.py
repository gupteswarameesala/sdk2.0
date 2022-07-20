from core import AbstractDiscovery, Constants, GatewayToCloudMessage
import logging
from target import TargetDiscovery
logger = logging.getLogger(__name__)

class DellPowerflexSystemDiscovery(AbstractDiscovery):

      def discover(self, requestContext):
          try:
              logger.debug("DellPowerflexSystem discovery stared")
              try:
                resource_type = requestContext.context.get("resourceTypes")["Dell PowerFlex System"]
              except Exception as KeyError:
                  resource_type = None
              DellPowerflexSystem_list,relation_list = TargetDiscovery().get_DellPowerflexSystem_data(requestContext, resource_type)

              logger.debug("DellPowerflexSystem discoverey json " + str(DellPowerflexSystem_list))
              logger.debug(" relationship json " + str(relation_list))

              if DellPowerflexSystem_list != None and resource_type != None and len(DellPowerflexSystem_list)>0:
                http_headers = requestContext.context.get('http_headers')
                http_headers['AM-App-Native-Type'] = "Dell PowerFlex System"
                requestContext.context["http_headers"] = http_headers
                GatewayToCloudMessage.publish_resources(requestContext.context.get("http_headers"),  DellPowerflexSystem_list)

                if relation_list != None and len(relation_list)>0:
                    GatewayToCloudMessage.publish_relationships(requestContext.context.get("http_headers"),
                                                                relation_list)
              else:
                  logger.info("DellPowerflexSystem disocvery is null ")


          except Exception as e:
              raise Exception(str(e))