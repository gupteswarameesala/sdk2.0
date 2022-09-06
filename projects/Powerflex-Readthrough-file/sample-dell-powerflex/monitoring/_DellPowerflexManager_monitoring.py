from core import AbstractMonitoring,Constants,Time,GatewayToCloudMessage
from target import TargetMonitoring
import datetime
import requests
from httpclient import Url

import logging
logger = logging.getLogger(__name__)

class DellPowerflexManagerMonitoring(AbstractMonitoring):

      def monitor(self, requestContext):
          try:
              logger.debug("Collecting DellPowerflexManager metrics")
              DellPowerflexManager_metrics = TargetMonitoring().process_DellPowerflexManager_metrics(requestContext)
              if DellPowerflexManager_metrics != None:
                GatewayToCloudMessage.publish_metrics(requestContext.context["http_headers"], DellPowerflexManager_metrics)
              else:
                logger.info("metrics json found null")
              logger.debug("DellPowerflexManager monitoring json " + str(DellPowerflexManager_metrics))
          except Exception as e:
              raise Exception(str(e))
        #self.process_host_metrics(requestContext)