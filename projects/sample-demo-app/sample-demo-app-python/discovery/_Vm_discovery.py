from core import AbstractDiscovery, Constants, GatewayToCloudMessage
import logging
from target import TargetDiscovery
logger = logging.getLogger(__name__)

class VmDiscovery(AbstractDiscovery):

      def discover(self, requestContext):
          try:
              logger.debug("Vm discovery stared")
              try:
                resource_type = requestContext.context.get("resourceTypes")["vm"]
              except Exception as KeyError:
                  resource_type = None
              Vm_list,relation_list = TargetDiscovery().get_Vm_data(requestContext, resource_type)

              logger.debug("Vm discoverey json " + str(Vm_list))
              logger.debug(" relationship json " + str(relation_list))

              if Vm_list != None and resource_type != None:
                http_headers = requestContext.context.get('http_headers')
                http_headers['AM-App-Native-Type'] = "vm"
                requestContext.context["http_headers"] = http_headers
                GatewayToCloudMessage.publish_resources(requestContext.context.get("http_headers"),  Vm_list)

                if relation_list != None:
                    GatewayToCloudMessage.publish_relationships(requestContext.context.get("http_headers"),
                                                                relation_list)
              else:
                  logger.info("Vm disocvery is null ")


          except Exception as e:
              raise Exception(str(e))