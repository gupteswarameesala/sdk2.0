from core import AbstractMonitoring,Constants,Time,GatewayToCloudMessage
from target import TargetMonitoring
import datetime
import requests
from httpclient import Url

import logging
logger = logging.getLogger(__name__)

class VmMonitoring(AbstractMonitoring):

      def monitor(self, requestContext):
          try:
              logger.debug("Collecting Vm metrics")
              Vm_metrics = TargetMonitoring().process_Vm_metrics(requestContext)
              if Vm_metrics != None:
                GatewayToCloudMessage.publish_metrics(requestContext.context["http_headers"], Vm_metrics)
              else:
                logger.info("metrics json found null")
              logger.debug("Vm monitoring json " + str(Vm_metrics))
          except Exception as e:
              raise Exception(str(e))
        #self.process_host_metrics(requestContext)