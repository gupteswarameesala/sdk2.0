from core import AbstractDiscovery, Constants, GatewayToCloudMessage
import logging
from target import TargetDiscovery
logger = logging.getLogger(__name__)

class {{nativeType}}Discovery(AbstractDiscovery):

      def discover(self, requestContext):
          try:
              logger.debug("{{nativeType}} discovery stared")
              try:
                resource_type = requestContext.context.get("resourceTypes")["{{ntName}}"]
              except Exception as KeyError:
                  resource_type = None
              {{nativeType}}_list,relation_list = TargetDiscovery().get_{{nativeType}}_data(requestContext, resource_type)

              logger.debug("{{nativeType}} discoverey json " + str({{nativeType}}_list))
              logger.debug(" relationship json " + str(relation_list))

              if {{nativeType}}_list != None and resource_type != None:
                http_headers = requestContext.context.get('http_headers')
                http_headers['AM-App-Native-Type'] = "{{ntName}}"
                requestContext.context["http_headers"] = http_headers
                GatewayToCloudMessage.publish_resources(requestContext.context.get("http_headers"),  {{nativeType}}_list)

                if relation_list != None:
                    GatewayToCloudMessage.publish_relationships(requestContext.context.get("http_headers"),
                                                                relation_list)
              else:
                  logger.info("{{nativeType}} disocvery is null ")


          except Exception as e:
              raise Exception(str(e))