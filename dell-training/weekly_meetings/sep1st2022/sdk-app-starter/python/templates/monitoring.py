from core import AbstractMonitoring, GatewayToCloudMessage
from target import TargetMonitoring


import logging
logger = logging.getLogger(__name__)


class {{nativeType}}Monitoring(AbstractMonitoring):

    def monitor(self, requestcontext):
        try:
            logger.debug("Collecting {{nativeType}} metrics")
            {{nativeType}}_metrics = TargetMonitoring().process_{{nativeType.lower()}}_metrics(requestcontext)
            if {{nativeType}}_metrics is not None and len({{nativeType}}_metrics) > 0:
                GatewayToCloudMessage.publish_metrics(requestcontext.context["http_headers"],
                                                      {{nativeType}}_metrics)
            else:
                logger.info("metrics json not found")
                logger.debug("{{nativeType}} monitoring json " + str({{nativeType}}_metrics))
        except Exception as e:
            raise Exception(str(e))

