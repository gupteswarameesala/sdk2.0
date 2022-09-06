from core import AbstractHandler, Registery, Constants, GatewayToCloudMessage
import time
import logging


logger = logging.getLogger(__name__)


class DiscoveryHandler(AbstractHandler):

    def __init__(self, requestcontext):
        super().__init__(requestcontext)
        # self.http_headers = http_headers

    def perform(self):
        try:
            rd = self.requestcontext.get_request_data()
            logger.debug("Discovery Message Received" + str(rd))

            self.requestcontext.context[Constants.APP_DATA] = self.requestcontext.get_request_data()
            payload = self.requestcontext.get_request_data()[Constants.PAYLOAD]

            native_types = payload.get(Constants.NATIVE_TYPES)
            native_types_list = [key for key, value in native_types.items()]

            resource_types_list = {key: value for key, value in native_types.items() for value in value.values()}

            self.requestcontext.context[Constants.RESOURCE_TYPES] = resource_types_list
            self.requestcontext.context[Constants.NATIVE_TYPES] = native_types_list

            data = payload.get(Constants.DATA)
            self.requestcontext.context[Constants.DATA] = data

            des = Registery.getDiscoveryEntities()
            poll_id = self.requestcontext.context.get(Constants.HTTP_HEADERS)[Constants.POLL_ID]
            logger.info("Discovery with Poll Id " + str(poll_id) + " is  Started at " + str(time.time()))
            discovery_success = True

            for i in des:
                try:
                    aa = i()
                    aa.discover(self.requestcontext)
                except Exception as e:
                    discovery_success = False
                    logger.exception("Couldn't discover resource" + str(e))
            if discovery_success:
                GatewayToCloudMessage.post_acknowledge(self.requestcontext.context[Constants.HTTP_HEADERS],
                                                       Constants.TRUE)
            logger.info("Discovery with Poll Id " + str(poll_id) + " is ended  at" + str(time.time()))

        except Exception as e:
            poll_id = self.requestcontext.context.get(Constants.HTTP_HEADERS)[Constants.POLL_ID]
            logger.exception("Discovery with Poll Id " + str(poll_id) + "failed with error" + str(e))
        finally:
            self.requestcontext.destroy()
