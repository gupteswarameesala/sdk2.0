from core import AbstractMonitoring,Constants,Time,GatewayToCloudMessage
from target import TargetMonitoring
import datetime
import requests
from httpclient import Url

import logging
logger = logging.getLogger(__name__)

class DellPowerflexSdcMonitoring(AbstractMonitoring):

      def monitor(self, requestContext):
          try:
              logger.debug("Collecting DellPowerflexSdc metrics")
              DellPowerflexSdc_metrics = TargetMonitoring().process_DellPowerflexSdc_metrics(requestContext)
              if DellPowerflexSdc_metrics != None:
                GatewayToCloudMessage.publish_metrics(requestContext.context["http_headers"], DellPowerflexSdc_metrics)
              else:
                logger.info("metrics json found null")
              logger.debug("DellPowerflexSdc monitoring json " + str(DellPowerflexSdc_metrics))
          except Exception as e:
              raise Exception(str(e))
        #self.process_host_metrics(requestContext)