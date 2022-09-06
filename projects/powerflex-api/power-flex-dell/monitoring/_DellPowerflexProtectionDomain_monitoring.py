from core import AbstractMonitoring,Constants,Time,GatewayToCloudMessage
from target import TargetMonitoring
import datetime
import requests
from httpclient import Url

import logging
logger = logging.getLogger(__name__)

class DellPowerflexProtectionDomainMonitoring(AbstractMonitoring):

      def monitor(self, requestContext):
          try:
              logger.debug("Collecting DellPowerflexProtectionDomain metrics")
              DellPowerflexProtectionDomain_metrics = TargetMonitoring().process_DellPowerflexProtectionDomain_metrics(requestContext)
              if DellPowerflexProtectionDomain_metrics != None and len(DellPowerflexProtectionDomain_metrics)>0:
                GatewayToCloudMessage.publish_metrics(requestContext.context["http_headers"], DellPowerflexProtectionDomain_metrics)
              else:
                logger.info("metrics json found null")
              logger.debug("DellPowerflexProtectionDomain monitoring json " + str(DellPowerflexProtectionDomain_metrics))
          except Exception as e:
              raise Exception(str(e))
        #self.process_host_metrics(requestContext)