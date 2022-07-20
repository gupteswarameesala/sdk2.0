from core import AbstractDiscovery, Constants, GatewayToCloudMessage
import logging
from target import TargetDiscovery
logger = logging.getLogger(__name__)

class DellPowerflexVtreeDiscovery(AbstractDiscovery):

      def discover(self, requestContext):
          try:
              logger.debug("DellPowerflexVtree discovery stared")
              try:
                resource_type = requestContext.context.get("resourceTypes")["Dell PowerFlex VTree"]
              except Exception as KeyError:
                  resource_type = None
              DellPowerflexVtree_list,relation_list = TargetDiscovery().get_DellPowerflexVtree_data(requestContext, resource_type)

              logger.debug("DellPowerflexVtree discoverey json " + str(DellPowerflexVtree_list))
              logger.debug(" relationship json " + str(relation_list))

              if DellPowerflexVtree_list != None and resource_type != None:
                http_headers = requestContext.context.get('http_headers')
                http_headers['AM-App-Native-Type'] = "Dell PowerFlex VTree"
                requestContext.context["http_headers"] = http_headers
                GatewayToCloudMessage.publish_resources(requestContext.context.get("http_headers"),  DellPowerflexVtree_list)

                if relation_list != None:
                    GatewayToCloudMessage.publish_relationships(requestContext.context.get("http_headers"),
                                                                relation_list)
              else:
                  logger.info("DellPowerflexVtree disocvery is null ")


          except Exception as e:
              raise Exception(str(e))