from core import AbstractMonitoring,Constants,Time,GatewayToCloudMessage
from target import TargetMonitoring
import datetime
import requests
from httpclient import Url

import logging
logger = logging.getLogger(__name__)

class DellPowerflexMdmClusterMonitoring(AbstractMonitoring):

      def monitor(self, requestContext):
          try:
              logger.debug("Collecting DellPowerflexMdmCluster metrics")
              DellPowerflexMdmCluster_metrics = TargetMonitoring().process_DellPowerflexMdmCluster_metrics(requestContext)
              if DellPowerflexMdmCluster_metrics != None:
                GatewayToCloudMessage.publish_metrics(requestContext.context["http_headers"], DellPowerflexMdmCluster_metrics)
              else:
                logger.info("metrics json found null")
              logger.debug("DellPowerflexMdmCluster monitoring json " + str(DellPowerflexMdmCluster_metrics))
          except Exception as e:
              raise Exception(str(e))
        #self.process_host_metrics(requestContext)