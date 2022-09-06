import time

from core import AbstractHandler, Registery, GatewayToCloudMessage, Constants
import logging

logger = logging.getLogger(__name__)


class MonitoringHandler(AbstractHandler):

    def __init__(self, requestcontext):
        super().__init__(requestcontext)

    def perform(self):
        try:
            logger.debug("Monitoring Message Received" + str(self.requestcontext.get_request_data()))

            self.requestcontext.context[Constants.APP_DATA] = self.requestcontext.get_request_data()
            payload = self.requestcontext.get_request_data()[Constants.PAYLOAD]

            nativeType = None
            for nativeTypeKey in payload[Constants.NATIVE_TYPE].keys():
                nativeType = nativeTypeKey

            self.requestcontext.context[Constants.NATIVE_TYPE] = nativeType
            self.requestcontext.context[Constants.TEMPLATE_ID] = payload[Constants.TEMPLATE_ID]
            self.requestcontext.context[Constants.MONITOR_ID] = payload[Constants.MONITOR_ID]

            appConfig = payload.get(Constants.APPCONFIG)
            appConfigPayloadData = appConfig.get(Constants.DATA)
            self.requestcontext.context[Constants.DATA] = appConfigPayloadData

            resources = payload.get(Constants.RESOURCES)
            self.requestcontext.context[Constants.RESOURCES] = resources

            metrics = payload.get(Constants.NATIVE_TYPE).get(list(payload.get(Constants.NATIVE_TYPE).keys())[0])
            self.requestcontext.context[Constants.METRICS] = metrics

            monitoringClass = Registery.getMonitoringEntity(nativeType)

            poll_id = self.requestcontext.context.get(Constants.HTTP_HEADERS)[Constants.POLL_ID]
            logger.info("Monitoring with Poll Id " + str(poll_id) + " is  Started at " + str(time.time()))

            aa = monitoringClass()
            aa.monitor(self.requestcontext)

            GatewayToCloudMessage.post_acknowledge(self.requestcontext.context[Constants.HTTP_HEADERS], Constants.FALSE)
            logger.info("Monitoring with Poll Id " + str(poll_id) + " ended  at " + str(time.time()))

        except Exception as e:
            poll_id = self.requestcontext.context.get(Constants.HTTP_HEADERS)[Constants.POLL_ID]
            logger.exception("Monitoring with Poll Id " + str(poll_id) + " failed with error " + str(e))
        finally:
            self.requestcontext.destroy()
