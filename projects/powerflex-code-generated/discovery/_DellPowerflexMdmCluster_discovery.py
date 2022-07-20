from core import AbstractDiscovery, Constants, GatewayToCloudMessage
import logging
from target import TargetDiscovery
logger = logging.getLogger(__name__)

class DellPowerflexMdmClusterDiscovery(AbstractDiscovery):

      def discover(self, requestContext):
          try:
              logger.debug("DellPowerflexMdmCluster discovery stared")
              try:
                resource_type = requestContext.context.get("resourceTypes")["Dell PowerFlex MDM Cluster"]
              except Exception as KeyError:
                  resource_type = None
              DellPowerflexMdmCluster_list,relation_list = TargetDiscovery().get_DellPowerflexMdmCluster_data(requestContext, resource_type)

              logger.debug("DellPowerflexMdmCluster discoverey json " + str(DellPowerflexMdmCluster_list))
              logger.debug(" relationship json " + str(relation_list))

              if DellPowerflexMdmCluster_list != None and resource_type != None:
                http_headers = requestContext.context.get('http_headers')
                http_headers['AM-App-Native-Type'] = "Dell PowerFlex MDM Cluster"
                requestContext.context["http_headers"] = http_headers
                GatewayToCloudMessage.publish_resources(requestContext.context.get("http_headers"),  DellPowerflexMdmCluster_list)

                if relation_list != None:
                    GatewayToCloudMessage.publish_relationships(requestContext.context.get("http_headers"),
                                                                relation_list)
              else:
                  logger.info("DellPowerflexMdmCluster disocvery is null ")


          except Exception as e:
              raise Exception(str(e))