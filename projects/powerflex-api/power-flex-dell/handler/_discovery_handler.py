from core import AbstractHandler, Registery, Constants, GatewayToCloudMessage
import requests
import time
import logging

from httpclient import Url

logger = logging.getLogger(__name__)


class DiscoveryHandler(AbstractHandler):

    def __init__(self, requestContext):
        super().__init__(requestContext)
        # self.http_headers = http_headers

    def perform(self):
        try:

            rd = self.requestContext.get_request_data()
            logger.info("Discovery Message Recieved" + str(rd))
            # print(rd)
            payload = rd.get('payload')

            self.requestContext.context["app_data"] = self.requestContext.get_request_data()
            payload = self.requestContext.get_request_data()["payload"]

            native_types = payload.get('nativeTypes')
            native_types_list = [key for key, value in native_types.items()]

            resource_types_list = {key: value for key, value in native_types.items() for value in value.values()}

            self.requestContext.context["resourceTypes"] = resource_types_list
            self.requestContext.context["nativeTypes"] = native_types_list

            data = payload.get('data')
            self.requestContext.context["data"] = data

            des = Registery.getDiscoveryEntities()
            poll_id = self.requestContext.context.get('http_headers')['AM-Poll-Id']
            logger.info("Discovery with Poll Id " + str(poll_id) + " is  Started at " + str(time.time()))
            discovery_success = True

            for i in des:
                try:
                    aa = i()
                    aa.discover(self.requestContext)
                except Exception as e:
                    discovery_success = False
                    logger.exception("Couldn't discover resource" + str(e))
            if discovery_success:
                GatewayToCloudMessage.post_acknowledge(self.requestContext.context["http_headers"], "true")
            logger.info("Discovery with Poll Id " + str(poll_id) + " is ended  at" + str(time.time()))

        except Exception as e:
            logger.exception("Discovery with Poll Id " + str(poll_id) + "failed with error" + str(e))
        finally:
            self.requestContext.destroy()



