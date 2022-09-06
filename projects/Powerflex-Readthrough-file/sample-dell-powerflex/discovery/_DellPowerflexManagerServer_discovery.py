from core import AbstractDiscovery, Constants, GatewayToCloudMessage
import logging
from target import TargetDiscovery
logger = logging.getLogger(__name__)

class DellPowerflexManagerServerDiscovery(AbstractDiscovery):

      def discover(self, requestContext):
          try:
              logger.debug("DellPowerflexManagerServer discovery stared")
              try:
                resource_type = requestContext.context.get("resourceTypes")["Dell PowerFlex Manager Server"]
              except Exception as KeyError:
                  resource_type = None
              DellPowerflexManagerServer_list,relation_list = TargetDiscovery().get_DellPowerflexManagerServer_data(requestContext, resource_type)

              logger.debug("DellPowerflexManagerServer discoverey json " + str(DellPowerflexManagerServer_list))
              logger.debug(" relationship json " + str(relation_list))

              if DellPowerflexManagerServer_list != None and resource_type != None:
                http_headers = requestContext.context.get('http_headers')
                http_headers['AM-App-Native-Type'] = "Dell PowerFlex Manager Server"
                requestContext.context["http_headers"] = http_headers
                GatewayToCloudMessage.publish_resources(requestContext.context.get("http_headers"),  DellPowerflexManagerServer_list)

                if relation_list != None:
                    GatewayToCloudMessage.publish_relationships(requestContext.context.get("http_headers"),
                                                                relation_list)
              else:
                  logger.info("DellPowerflexManagerServer disocvery is null ")


          except Exception as e:
              raise Exception(str(e))