from core import AbstractDiscovery, Constants, GatewayToCloudMessage
import logging
from target import TargetDiscovery
logger = logging.getLogger(__name__)

class HostDiscovery(AbstractDiscovery):

      def discover(self, requestContext):
          try:
              logger.debug("Host discovery stared")
              try:
                resource_type = requestContext.context.get("resourceTypes")["host"]
              except Exception as KeyError:
                  resource_type = None
              Host_list,relation_list = TargetDiscovery().get_Host_data(requestContext, resource_type)

              logger.debug("Host discoverey json " + str(Host_list))
              logger.debug(" relationship json " + str(relation_list))

              if Host_list != None and resource_type != None:
                http_headers = requestContext.context.get('http_headers')
                http_headers['AM-App-Native-Type'] = "host"
                requestContext.context["http_headers"] = http_headers
                GatewayToCloudMessage.publish_resources(requestContext.context.get("http_headers"),  Host_list)

                if relation_list != None:
                    GatewayToCloudMessage.publish_relationships(requestContext.context.get("http_headers"),
                                                                relation_list)
              else:
                  logger.info("Host disocvery is null ")


          except Exception as e:
              raise Exception(str(e))