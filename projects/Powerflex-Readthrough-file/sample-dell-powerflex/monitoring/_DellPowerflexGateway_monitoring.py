from core import AbstractMonitoring,Constants,Time,GatewayToCloudMessage
from target import TargetMonitoring
import datetime
import requests
from httpclient import Url

import logging
logger = logging.getLogger(__name__)

class DellPowerflexGatewayMonitoring(AbstractMonitoring):

      def monitor(self, requestContext):
          try:
              logger.debug("Collecting DellPowerflexGateway metrics")
              DellPowerflexGateway_metrics = TargetMonitoring().process_DellPowerflexGateway_metrics(requestContext)
              if DellPowerflexGateway_metrics != None:
                GatewayToCloudMessage.publish_metrics(requestContext.context["http_headers"], DellPowerflexGateway_metrics)
              else:
                logger.info("metrics json found null")
              logger.debug("DellPowerflexGateway monitoring json " + str(DellPowerflexGateway_metrics))
          except Exception as e:
              raise Exception(str(e))
        #self.process_host_metrics(requestContext)