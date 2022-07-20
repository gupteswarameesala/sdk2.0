from core import AbstractDiscovery, Constants, GatewayToCloudMessage
import logging
from target import TargetDiscovery
logger = logging.getLogger(__name__)

class DellPowerflexVolumeDiscovery(AbstractDiscovery):

      def discover(self, requestContext):
          try:
              logger.debug("DellPowerflexVolume discovery stared")
              try:
                resource_type = requestContext.context.get("resourceTypes")["Dell PowerFlex Volume"]
              except Exception as KeyError:
                  resource_type = None
              DellPowerflexVolume_list,relation_list = TargetDiscovery().get_DellPowerflexVolume_data(requestContext, resource_type)

              logger.debug("DellPowerflexVolume discoverey json " + str(DellPowerflexVolume_list))
              logger.debug(" relationship json " + str(relation_list))

              if DellPowerflexVolume_list != None and resource_type != None:
                http_headers = requestContext.context.get('http_headers')
                http_headers['AM-App-Native-Type'] = "Dell PowerFlex Volume"
                requestContext.context["http_headers"] = http_headers
                GatewayToCloudMessage.publish_resources(requestContext.context.get("http_headers"),  DellPowerflexVolume_list)

                if relation_list != None:
                    GatewayToCloudMessage.publish_relationships(requestContext.context.get("http_headers"),
                                                                relation_list)
              else:
                  logger.info("DellPowerflexVolume disocvery is null ")


          except Exception as e:
              raise Exception(str(e))