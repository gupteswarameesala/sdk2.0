from core import AbstractMonitoring,Constants,Time,GatewayToCloudMessage
from target import TargetMonitoring
import datetime
import requests
from httpclient import Url

import logging
logger = logging.getLogger(__name__)

class DellPowerflexSdsMonitoring(AbstractMonitoring):

      def monitor(self, requestContext):
          try:
              logger.debug("Collecting DellPowerflexSds metrics")
              DellPowerflexSds_metrics = TargetMonitoring().process_DellPowerflexSds_metrics(requestContext)
              if DellPowerflexSds_metrics != None and len(DellPowerflexSds_metrics)>0:
                GatewayToCloudMessage.publish_metrics(requestContext.context["http_headers"], DellPowerflexSds_metrics)
              else:
                logger.info("metrics json found null")
              logger.debug("DellPowerflexSds monitoring json " + str(DellPowerflexSds_metrics))
          except Exception as e:
              raise Exception(str(e))
        #self.process_host_metrics(requestContext)