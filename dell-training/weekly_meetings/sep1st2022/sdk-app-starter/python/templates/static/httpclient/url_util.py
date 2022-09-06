import requests
import logging
import os
from core import Constants

logger = logging.getLogger(__name__)
base_adk_url = os.getenv(Constants.ADK_SERVICE_URI)


class Url:
    # Getting data from the request
    @staticmethod
    def get(url):
        r = requests.get(url)
        if r.status_code == Constants.STATUS_OK:
            return r.json()
        else:
            return None

    @staticmethod
    def putAck(url, http_headers):
        r = requests.put(url, headers=http_headers)
        if r.status_code == Constants.STATUS_OK:
            return Constants.STATUS_OK
        else:
            return None

    @staticmethod
    def put(url, data, http_headers):
        r = requests.put(url, data=data, headers=http_headers)
        logger.info("data>>>>>>>")
        logger.info(data)
        logger.info("headers>>>>>")
        logger.info(http_headers)
        if r.status_code == Constants.STATUS_OK:
            return Constants.STATUS_OK
        else:
            logger.info("Failed to post put request.......")
            logger.info(r.reason)
            return None

    @staticmethod
    def post(url, data, http_headers):
        r = requests.post(url, data=data, headers=http_headers)
        if r.status_code == Constants.STATUS_OK:
            return Constants.STATUS_OK
        else:
            return None
