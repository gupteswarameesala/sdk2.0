from core import AbstractDiscovery, Constants, GatewayToCloudMessage
import logging
from target import TargetDiscovery
logger = logging.getLogger(__name__)

class VcenterDiscovery(AbstractDiscovery):

      def discover(self, requestContext):
          try:
              logger.debug("Vcenter discovery stared")
              try:
                resource_type = requestContext.context.get("resourceTypes")["vcenter"]
              except Exception as KeyError:
                  resource_type = None
              Vcenter_list,relation_list = TargetDiscovery().get_Vcenter_data(requestContext, resource_type)

              logger.debug("Vcenter discoverey json " + str(Vcenter_list))
              logger.debug(" relationship json " + str(relation_list))

              if Vcenter_list != None and resource_type != None:
                http_headers = requestContext.context.get('http_headers')
                http_headers['AM-App-Native-Type'] = "vcenter"
                requestContext.context["http_headers"] = http_headers
                GatewayToCloudMessage.publish_resources(requestContext.context.get("http_headers"),  Vcenter_list)

                if relation_list != None:
                    GatewayToCloudMessage.publish_relationships(requestContext.context.get("http_headers"),
                                                                relation_list)
              else:
                  logger.info("Vcenter disocvery is null ")


          except Exception as e:
              raise Exception(str(e))