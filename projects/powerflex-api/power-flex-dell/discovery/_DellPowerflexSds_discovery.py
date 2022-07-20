from core import AbstractDiscovery, Constants, GatewayToCloudMessage
import logging
from target import TargetDiscovery
logger = logging.getLogger(__name__)

class DellPowerflexSdsDiscovery(AbstractDiscovery):

      def discover(self, requestContext):
          try:
              logger.debug("DellPowerflexSds discovery stared")
              try:
                resource_type = requestContext.context.get("resourceTypes")["Dell PowerFlex SDS"]
              except Exception as KeyError:
                  resource_type = None
              DellPowerflexSds_list,relation_list = TargetDiscovery().get_DellPowerflexSds_data(requestContext, resource_type)

              logger.debug("DellPowerflexSds discoverey json " + str(DellPowerflexSds_list))
              logger.debug(" relationship json " + str(relation_list))

              if DellPowerflexSds_list != None and resource_type != None and len(DellPowerflexSds_list)>0:
                http_headers = requestContext.context.get('http_headers')
                http_headers['AM-App-Native-Type'] = "Dell PowerFlex SDS"
                requestContext.context["http_headers"] = http_headers
                GatewayToCloudMessage.publish_resources(requestContext.context.get("http_headers"),  DellPowerflexSds_list)

                if relation_list != None and len(relation_list)>0:
                    GatewayToCloudMessage.publish_relationships(requestContext.context.get("http_headers"),
                                                                relation_list)
              else:
                  logger.info("DellPowerflexSds disocvery is null ")


          except Exception as e:
              raise Exception(str(e))