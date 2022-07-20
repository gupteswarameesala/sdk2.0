from core import AbstractMonitoring,Constants,Time,GatewayToCloudMessage
from target import TargetMonitoring
import datetime
import requests
from httpclient import Url

import logging
logger = logging.getLogger(__name__)

class DellPowerflexStoragePoolMonitoring(AbstractMonitoring):

      def monitor(self, requestContext):
          try:
              logger.debug("Collecting DellPowerflexStoragePool metrics")
              DellPowerflexStoragePool_metrics = TargetMonitoring().process_DellPowerflexStoragePool_metrics(requestContext)
              if DellPowerflexStoragePool_metrics != None and len(DellPowerflexStoragePool_metrics)>0:
                GatewayToCloudMessage.publish_metrics(requestContext.context["http_headers"], DellPowerflexStoragePool_metrics)
              else:
                logger.info("metrics json found null")
              logger.debug("DellPowerflexStoragePool monitoring json " + str(DellPowerflexStoragePool_metrics))
          except Exception as e:
              raise Exception(str(e))
        #self.process_host_metrics(requestContext)