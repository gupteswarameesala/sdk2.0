from core import AbstractDiscovery, Constants, GatewayToCloudMessage
import logging
from target import TargetDiscovery
logger = logging.getLogger(__name__)

class DellPowerflexManagerSwitchDiscovery(AbstractDiscovery):

      def discover(self, requestContext):
          try:
              logger.debug("DellPowerflexManagerSwitch discovery stared")
              try:
                resource_type = requestContext.context.get("resourceTypes")["Dell PowerFlex Manager Switch"]
              except Exception as KeyError:
                  resource_type = None
              DellPowerflexManagerSwitch_list,relation_list = TargetDiscovery().get_DellPowerflexManagerSwitch_data(requestContext, resource_type)

              logger.debug("DellPowerflexManagerSwitch discoverey json " + str(DellPowerflexManagerSwitch_list))
              logger.debug(" relationship json " + str(relation_list))

              if DellPowerflexManagerSwitch_list != None and resource_type != None:
                http_headers = requestContext.context.get('http_headers')
                http_headers['AM-App-Native-Type'] = "Dell PowerFlex Manager Switch"
                requestContext.context["http_headers"] = http_headers
                GatewayToCloudMessage.publish_resources(requestContext.context.get("http_headers"),  DellPowerflexManagerSwitch_list)

                if relation_list != None:
                    GatewayToCloudMessage.publish_relationships(requestContext.context.get("http_headers"),
                                                                relation_list)
              else:
                  logger.info("DellPowerflexManagerSwitch disocvery is null ")


          except Exception as e:
              raise Exception(str(e))