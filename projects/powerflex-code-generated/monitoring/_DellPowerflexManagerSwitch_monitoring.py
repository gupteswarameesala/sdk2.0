from core import AbstractMonitoring,Constants,Time,GatewayToCloudMessage
from target import TargetMonitoring
import datetime
import requests
from httpclient import Url

import logging
logger = logging.getLogger(__name__)

class DellPowerflexManagerSwitchMonitoring(AbstractMonitoring):

      def monitor(self, requestContext):
          try:
              logger.debug("Collecting DellPowerflexManagerSwitch metrics")
              DellPowerflexManagerSwitch_metrics = TargetMonitoring().process_DellPowerflexManagerSwitch_metrics(requestContext)
              if DellPowerflexManagerSwitch_metrics != None:
                GatewayToCloudMessage.publish_metrics(requestContext.context["http_headers"], DellPowerflexManagerSwitch_metrics)
              else:
                logger.info("metrics json found null")
              logger.debug("DellPowerflexManagerSwitch monitoring json " + str(DellPowerflexManagerSwitch_metrics))
          except Exception as e:
              raise Exception(str(e))
        #self.process_host_metrics(requestContext)