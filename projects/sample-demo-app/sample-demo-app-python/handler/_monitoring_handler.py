import time

from core import AbstractHandler, Registery, GatewayToCloudMessage
import logging

logger = logging.getLogger(__name__)

class MonitoringHandler(AbstractHandler):

    def __init__(self, requestContext):
        super().__init__(requestContext)
        
    
    def perform(self):
        try:
            logger.debug("Monitoring Message Recieved"+str(self.requestContext.get_request_data()))
            #logger.info(self.requestContext.get_request_data())
            payload = self.requestContext.get_request_data()["payload"]

            self.requestContext.context["app_data"] = self.requestContext.get_request_data()
            payload = self.requestContext.get_request_data()["payload"]

            nativeType = None
            for nativeTypeKey in payload["nativeType"].keys():
                nativeType = nativeTypeKey

            self.requestContext.context["nativeType"] = nativeType
            self.requestContext.context["templateId"] = payload["templateId"]
            self.requestContext.context["monitorId"] = payload["monitorId"]

            appConfig = payload.get('appConfig')
            appConfigPayloadData = appConfig.get('data')
            self.requestContext.context["data"] = appConfigPayloadData

            resources = payload.get('resources')
            self.requestContext.context["resources"] = resources

            metrics = payload.get("nativeType").get(list(payload.get("nativeType").keys())[0])
            self.requestContext.context["metrics"] = metrics

            monitoringClass = Registery.getMonitoringEntity(nativeType)

            poll_id = self.requestContext.context.get('http_headers')['AM-Poll-Id']
            logger.info("Monitoring with Poll Id " + str(poll_id) + " is  Started at " + str(time.time()))

            aa = monitoringClass()
            aa.monitor(self.requestContext)

            GatewayToCloudMessage.post_acknowledge(self.requestContext.context["http_headers"], "false")
            logger.info("Monitoring with Poll Id " + str(poll_id) + " ended  at " + str(time.time()))

        except Exception as e:
            logger.exception("Monitoring with Poll Id " + str(poll_id) + " failed with error "+str(e))
        finally:
            self.requestContext.destroy()
