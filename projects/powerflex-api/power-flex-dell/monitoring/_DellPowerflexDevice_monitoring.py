from core import AbstractMonitoring,Constants,Time,GatewayToCloudMessage
from target import TargetMonitoring
import datetime
import requests
from httpclient import Url

import logging
logger = logging.getLogger(__name__)

class DellPowerflexDeviceMonitoring(AbstractMonitoring):

      def monitor(self, requestContext):
          try:
              logger.debug("Collecting DellPowerflexDevice metrics")
              DellPowerflexDevice_metrics = TargetMonitoring().process_DellPowerflexDevice_metrics(requestContext)
              if DellPowerflexDevice_metrics != None and len(DellPowerflexDevice_metrics)>0:
                GatewayToCloudMessage.publish_metrics(requestContext.context["http_headers"], DellPowerflexDevice_metrics)
              else:
                logger.info("metrics json found null")
              logger.debug("DellPowerflexDevice monitoring json " + str(DellPowerflexDevice_metrics))
          except Exception as e:
              raise Exception(str(e))
        #self.process_host_metrics(requestContext)