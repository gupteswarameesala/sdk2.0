from core import AbstractMonitoring,Constants,Time,GatewayToCloudMessage
from target import TargetMonitoring
import datetime
import requests
from httpclient import Url

import logging
logger = logging.getLogger(__name__)

class DellPowerflexVolumeMonitoring(AbstractMonitoring):

      def monitor(self, requestContext):
          try:
              logger.debug("Collecting DellPowerflexVolume metrics")
              DellPowerflexVolume_metrics = TargetMonitoring().process_DellPowerflexVolume_metrics(requestContext)
              if DellPowerflexVolume_metrics != None:
                GatewayToCloudMessage.publish_metrics(requestContext.context["http_headers"], DellPowerflexVolume_metrics)
              else:
                logger.info("metrics json found null")
              logger.debug("DellPowerflexVolume monitoring json " + str(DellPowerflexVolume_metrics))
          except Exception as e:
              raise Exception(str(e))
        #self.process_host_metrics(requestContext)