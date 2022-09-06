from core import AbstractDiscovery, Constants, GatewayToCloudMessage
import logging
from target import TargetDiscovery
logger = logging.getLogger(__name__)

class DellPowerflexDeviceDiscovery(AbstractDiscovery):

      def discover(self, requestContext):
          try:
              logger.debug("DellPowerflexDevice discovery stared")
              try:
                resource_type = requestContext.context.get("resourceTypes")["Dell PowerFlex Device"]
              except Exception as KeyError:
                  resource_type = None
              DellPowerflexDevice_list,relation_list = TargetDiscovery().get_DellPowerflexDevice_data(requestContext, resource_type)

              logger.debug("DellPowerflexDevice discoverey json " + str(DellPowerflexDevice_list))
              logger.debug(" relationship json " + str(relation_list))

              if DellPowerflexDevice_list != None and resource_type != None:
                http_headers = requestContext.context.get('http_headers')
                http_headers['AM-App-Native-Type'] = "Dell PowerFlex Device"
                requestContext.context["http_headers"] = http_headers
                GatewayToCloudMessage.publish_resources(requestContext.context.get("http_headers"),  DellPowerflexDevice_list)

                if relation_list != None:
                    GatewayToCloudMessage.publish_relationships(requestContext.context.get("http_headers"),
                                                                relation_list)
              else:
                  logger.info("DellPowerflexDevice disocvery is null ")


          except Exception as e:
              raise Exception(str(e))