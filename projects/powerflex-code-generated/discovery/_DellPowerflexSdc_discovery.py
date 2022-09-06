from core import AbstractDiscovery, Constants, GatewayToCloudMessage
import logging
from target import TargetDiscovery
logger = logging.getLogger(__name__)

class DellPowerflexSdcDiscovery(AbstractDiscovery):

      def discover(self, requestContext):
          try:
              logger.debug("DellPowerflexSdc discovery stared")
              try:
                resource_type = requestContext.context.get("resourceTypes")["Dell PowerFlex SDC"]
              except Exception as KeyError:
                  resource_type = None
              DellPowerflexSdc_list,relation_list = TargetDiscovery().get_DellPowerflexSdc_data(requestContext, resource_type)

              logger.debug("DellPowerflexSdc discoverey json " + str(DellPowerflexSdc_list))
              logger.debug(" relationship json " + str(relation_list))

              if DellPowerflexSdc_list != None and resource_type != None:
                http_headers = requestContext.context.get('http_headers')
                http_headers['AM-App-Native-Type'] = "Dell PowerFlex SDC"
                requestContext.context["http_headers"] = http_headers
                GatewayToCloudMessage.publish_resources(requestContext.context.get("http_headers"),  DellPowerflexSdc_list)

                if relation_list != None:
                    GatewayToCloudMessage.publish_relationships(requestContext.context.get("http_headers"),
                                                                relation_list)
              else:
                  logger.info("DellPowerflexSdc disocvery is null ")


          except Exception as e:
              raise Exception(str(e))