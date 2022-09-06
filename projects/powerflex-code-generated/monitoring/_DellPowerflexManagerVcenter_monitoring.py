from core import AbstractMonitoring,Constants,Time,GatewayToCloudMessage
from target import TargetMonitoring
import datetime
import requests
from httpclient import Url

import logging
logger = logging.getLogger(__name__)

class DellPowerflexManagerVcenterMonitoring(AbstractMonitoring):

      def monitor(self, requestContext):
          try:
              logger.debug("Collecting DellPowerflexManagerVcenter metrics")
              DellPowerflexManagerVcenter_metrics = TargetMonitoring().process_DellPowerflexManagerVcenter_metrics(requestContext)
              if DellPowerflexManagerVcenter_metrics != None:
                GatewayToCloudMessage.publish_metrics(requestContext.context["http_headers"], DellPowerflexManagerVcenter_metrics)
              else:
                logger.info("metrics json found null")
              logger.debug("DellPowerflexManagerVcenter monitoring json " + str(DellPowerflexManagerVcenter_metrics))
          except Exception as e:
              raise Exception(str(e))
        #self.process_host_metrics(requestContext)