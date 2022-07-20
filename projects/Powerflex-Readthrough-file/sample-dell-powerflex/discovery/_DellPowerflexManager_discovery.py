from core import AbstractDiscovery, Constants, GatewayToCloudMessage
import logging
from target import TargetDiscovery
logger = logging.getLogger(__name__)

class DellPowerflexManagerDiscovery(AbstractDiscovery):

      def discover(self, requestContext):
          try:
              logger.debug("DellPowerflexManager discovery stared")
              try:
                resource_type = requestContext.context.get("resourceTypes")["Dell PowerFlex Manager"]
              except Exception as KeyError:
                  resource_type = None
              DellPowerflexManager_list,relation_list = TargetDiscovery().get_DellPowerflexManager_data(requestContext, resource_type)

              logger.debug("DellPowerflexManager discoverey json " + str(DellPowerflexManager_list))
              logger.debug(" relationship json " + str(relation_list))

              if DellPowerflexManager_list != None and resource_type != None:
                http_headers = requestContext.context.get('http_headers')
                http_headers['AM-App-Native-Type'] = "Dell PowerFlex Manager"
                requestContext.context["http_headers"] = http_headers
                GatewayToCloudMessage.publish_resources(requestContext.context.get("http_headers"),  DellPowerflexManager_list)

                if relation_list != None:
                    GatewayToCloudMessage.publish_relationships(requestContext.context.get("http_headers"),
                                                                relation_list)
              else:
                  logger.info("DellPowerflexManager disocvery is null ")


          except Exception as e:
              raise Exception(str(e))