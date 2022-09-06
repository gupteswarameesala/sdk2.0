from core import AbstractMonitoring,Constants,Time,GatewayToCloudMessage
from target import TargetMonitoring
import datetime
import requests
from httpclient import Url

import logging
logger = logging.getLogger(__name__)

class DellPowerflexVtreeMonitoring(AbstractMonitoring):

      def monitor(self, requestContext):
          try:
              logger.debug("Collecting DellPowerflexVtree metrics")
              DellPowerflexVtree_metrics = TargetMonitoring().process_DellPowerflexVtree_metrics(requestContext)
              if DellPowerflexVtree_metrics != None:
                GatewayToCloudMessage.publish_metrics(requestContext.context["http_headers"], DellPowerflexVtree_metrics)
              else:
                logger.info("metrics json found null")
              logger.debug("DellPowerflexVtree monitoring json " + str(DellPowerflexVtree_metrics))
          except Exception as e:
              raise Exception(str(e))
        #self.process_host_metrics(requestContext)