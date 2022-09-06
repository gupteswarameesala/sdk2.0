from core import AbstractMonitoring,Constants,Time,GatewayToCloudMessage
from target import TargetMonitoring
import datetime
import requests
from httpclient import Url

import logging
logger = logging.getLogger(__name__)

class DellPowerflexManagerServerMonitoring(AbstractMonitoring):

      def monitor(self, requestContext):
          try:
              logger.debug("Collecting DellPowerflexManagerServer metrics")
              DellPowerflexManagerServer_metrics = TargetMonitoring().process_DellPowerflexManagerServer_metrics(requestContext)
              if DellPowerflexManagerServer_metrics != None:
                GatewayToCloudMessage.publish_metrics(requestContext.context["http_headers"], DellPowerflexManagerServer_metrics)
              else:
                logger.info("metrics json found null")
              logger.debug("DellPowerflexManagerServer monitoring json " + str(DellPowerflexManagerServer_metrics))
          except Exception as e:
              raise Exception(str(e))
        #self.process_host_metrics(requestContext)