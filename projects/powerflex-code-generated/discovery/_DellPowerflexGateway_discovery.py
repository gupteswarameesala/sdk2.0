from core import AbstractDiscovery, Constants, GatewayToCloudMessage
import logging
from target import TargetDiscovery
logger = logging.getLogger(__name__)

class DellPowerflexGatewayDiscovery(AbstractDiscovery):

      def discover(self, requestContext):
          try:
              logger.debug("DellPowerflexGateway discovery stared")
              try:
                resource_type = requestContext.context.get("resourceTypes")["Dell PowerFlex Gateway"]
              except Exception as KeyError:
                  resource_type = None
              DellPowerflexGateway_list,relation_list = TargetDiscovery().get_DellPowerflexGateway_data(requestContext, resource_type)

              logger.debug("DellPowerflexGateway discoverey json " + str(DellPowerflexGateway_list))
              logger.debug(" relationship json " + str(relation_list))

              if DellPowerflexGateway_list != None and resource_type != None:
                http_headers = requestContext.context.get('http_headers')
                http_headers['AM-App-Native-Type'] = "Dell PowerFlex Gateway"
                requestContext.context["http_headers"] = http_headers
                GatewayToCloudMessage.publish_resources(requestContext.context.get("http_headers"),  DellPowerflexGateway_list)

                if relation_list != None:
                    GatewayToCloudMessage.publish_relationships(requestContext.context.get("http_headers"),
                                                                relation_list)
              else:
                  logger.info("DellPowerflexGateway disocvery is null ")


          except Exception as e:
              raise Exception(str(e))