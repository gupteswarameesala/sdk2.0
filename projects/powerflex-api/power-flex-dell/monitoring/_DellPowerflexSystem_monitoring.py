from core import AbstractMonitoring,Constants,Time,GatewayToCloudMessage
from target import TargetMonitoring
import datetime
import requests
from httpclient import Url

import logging
logger = logging.getLogger(__name__)

class DellPowerflexSystemMonitoring(AbstractMonitoring):

      def monitor(self, requestContext):
          try:
              logger.debug("Collecting DellPowerflexSystem metrics")
              DellPowerflexSystem_metrics = TargetMonitoring().process_DellPowerflexSystem_metrics(requestContext)
              if DellPowerflexSystem_metrics != None and len(DellPowerflexSystem_metrics)>0:
                GatewayToCloudMessage.publish_metrics(requestContext.context["http_headers"], DellPowerflexSystem_metrics)
              else:
                logger.info("metrics json found null")
              logger.debug("DellPowerflexSystem monitoring json " + str(DellPowerflexSystem_metrics))
          except Exception as e:
              raise Exception(str(e))
        #self.process_host_metrics(requestContext)