from core import AbstractMonitoring,Constants,Time,GatewayToCloudMessage
from target import TargetMonitoring
import datetime
import requests
from httpclient import Url

import logging
logger = logging.getLogger(__name__)

class {{nativeType}}Monitoring(AbstractMonitoring):

      def monitor(self, requestContext):
          try:
              logger.debug("Collecting {{nativeType}} metrics")
              {{nativeType}}_metrics = TargetMonitoring().process_{{nativeType}}_metrics(requestContext)
              if {{nativeType}}_metrics != None:
                GatewayToCloudMessage.publish_metrics(requestContext.context["http_headers"], {{nativeType}}_metrics)
              else:
                logger.info("metrics json found null")
              logger.debug("{{nativeType}} monitoring json " + str({{nativeType}}_metrics))
          except Exception as e:
              raise Exception(str(e))
        #self.process_host_metrics(requestContext)