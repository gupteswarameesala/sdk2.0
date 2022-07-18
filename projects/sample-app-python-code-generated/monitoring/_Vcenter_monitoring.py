from core import AbstractMonitoring,Constants,Time,GatewayToCloudMessage
from target import TargetMonitoring
import datetime
import requests
from httpclient import Url

import logging
logger = logging.getLogger(__name__)

class VcenterMonitoring(AbstractMonitoring):

      def monitor(self, requestContext):
          try:
              logger.debug("Collecting Vcenter metrics")
              Vcenter_metrics = TargetMonitoring().process_Vcenter_metrics(requestContext)
              if Vcenter_metrics != None:
                GatewayToCloudMessage.publish_metrics(requestContext.context["http_headers"], Vcenter_metrics)
              else:
                logger.info("metrics json found null")
              logger.debug("Vcenter monitoring json " + str(Vcenter_metrics))
          except Exception as e:
              raise Exception(str(e))
        #self.process_host_metrics(requestContext)