from core import AbstractDiscovery, Constants, GatewayToCloudMessage
import logging
from target import TargetDiscovery
logger = logging.getLogger(__name__)

class DellPowerflexStoragePoolDiscovery(AbstractDiscovery):

      def discover(self, requestContext):
          try:
              logger.debug("DellPowerflexStoragePool discovery stared")
              try:
                resource_type = requestContext.context.get("resourceTypes")["Dell PowerFlex Storage Pool"]
              except Exception as KeyError:
                  resource_type = None
              DellPowerflexStoragePool_list,relation_list = TargetDiscovery().get_DellPowerflexStoragePool_data(requestContext, resource_type)

              logger.debug("DellPowerflexStoragePool discoverey json " + str(DellPowerflexStoragePool_list))
              logger.debug(" relationship json " + str(relation_list))

              if DellPowerflexStoragePool_list != None and resource_type != None and len(DellPowerflexStoragePool_list)>0:
                http_headers = requestContext.context.get('http_headers')
                http_headers['AM-App-Native-Type'] = "Dell PowerFlex Storage Pool"
                requestContext.context["http_headers"] = http_headers
                GatewayToCloudMessage.publish_resources(requestContext.context.get("http_headers"),  DellPowerflexStoragePool_list)

                if relation_list != None and len(relation_list)>0:
                    GatewayToCloudMessage.publish_relationships(requestContext.context.get("http_headers"),
                                                                relation_list)
              else:
                  logger.info("DellPowerflexStoragePool disocvery is null ")


          except Exception as e:
              raise Exception(str(e))