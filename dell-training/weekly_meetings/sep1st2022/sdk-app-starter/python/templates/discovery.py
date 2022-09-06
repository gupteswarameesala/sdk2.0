from core import AbstractDiscovery, Constants, GatewayToCloudMessage
import logging
from target import TargetDiscovery
logger = logging.getLogger(__name__)


class {{nativeType}}Discovery(AbstractDiscovery):

    def discover(self, requestcontext):
        try:
            logger.debug("{{nativeType}} discovery stared")
            resource_type = requestcontext.context.get(Constants.RESOURCE_TYPES).get("{{ntName}}")
            {{nativeType}}_list, relation_list = TargetDiscovery(

            ).get_{{nativeType.lower()}}_data(requestcontext, resource_type)
            logger.debug("{{nativeType}} discovery json " + str({{nativeType}}_list))
            logger.debug(" relationship json " + str(relation_list))

            if {{nativeType}}_list is not None and resource_type is not None and len(
                    {{nativeType}}_list) > 0:
                http_headers = requestcontext.context.get(Constants.HTTP_HEADERS)
                http_headers[Constants.APP_NATIVE_TYPE] = "{{ntName}}"
                requestcontext.context[Constants.HTTP_HEADERS] = http_headers
                GatewayToCloudMessage.publish_resources(requestcontext.context.get(Constants.HTTP_HEADERS),
                                                        {{nativeType}}_list)

                if relation_list is not None and len(relation_list) > 0:
                    GatewayToCloudMessage.publish_relationships(requestcontext.context.get(Constants.HTTP_HEADERS),
                                                                relation_list)
            else:
                logger.info("{{nativeType}} discovery json not found ")
        except Exception as e:
            raise Exception(str(e))

