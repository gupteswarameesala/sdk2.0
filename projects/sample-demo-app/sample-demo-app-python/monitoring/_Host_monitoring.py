from core import AbstractMonitoring,Constants,Time,GatewayToCloudMessage
from target import TargetMonitoring
import datetime
import requests
from httpclient import Url

import logging
logger = logging.getLogger(__name__)

class HostMonitoring(AbstractMonitoring):

      def monitor(self, requestContext):
          try:
              logger.debug("Collecting Host metrics")
              Host_metrics = TargetMonitoring().process_Host_metrics(requestContext)
              if Host_metrics != None:
                GatewayToCloudMessage.publish_metrics(requestContext.context["http_headers"], Host_metrics)
              else:
                logger.info("metrics json found null")
              logger.debug("Host monitoring json " + str(Host_metrics))
          except Exception as e:
              raise Exception(str(e))
        #self.process_host_metrics(requestContext)