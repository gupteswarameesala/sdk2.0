from core import AbstractDiscovery, Constants, GatewayToCloudMessage
import logging
from target import TargetDiscovery
logger = logging.getLogger(__name__)

class DellPowerflexManagerVcenterDiscovery(AbstractDiscovery):

      def discover(self, requestContext):
          try:
              logger.debug("DellPowerflexManagerVcenter discovery stared")
              try:
                resource_type = requestContext.context.get("resourceTypes")["Dell PowerFlex Manager VCenter"]
              except Exception as KeyError:
                  resource_type = None
              DellPowerflexManagerVcenter_list,relation_list = TargetDiscovery().get_DellPowerflexManagerVcenter_data(requestContext, resource_type)

              logger.debug("DellPowerflexManagerVcenter discoverey json " + str(DellPowerflexManagerVcenter_list))
              logger.debug(" relationship json " + str(relation_list))

              if DellPowerflexManagerVcenter_list != None and resource_type != None:
                http_headers = requestContext.context.get('http_headers')
                http_headers['AM-App-Native-Type'] = "Dell PowerFlex Manager VCenter"
                requestContext.context["http_headers"] = http_headers
                GatewayToCloudMessage.publish_resources(requestContext.context.get("http_headers"),  DellPowerflexManagerVcenter_list)

                if relation_list != None:
                    GatewayToCloudMessage.publish_relationships(requestContext.context.get("http_headers"),
                                                                relation_list)
              else:
                  logger.info("DellPowerflexManagerVcenter disocvery is null ")


          except Exception as e:
              raise Exception(str(e))