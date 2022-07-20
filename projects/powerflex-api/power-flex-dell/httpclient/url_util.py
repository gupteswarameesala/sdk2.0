import json

import requests
import logging
import os
import time

from PyPowerFlex import PowerFlexClient

from core import Constants

logger = logging.getLogger(__name__)
base_adk_url = os.getenv('ADK_SERVICE_URI')


class Url:
    # Getting data from the request
    def get(self, url):
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

    # Constructing the base url
    def construct_base_url(self, request_data):
        server_protocol = request_data.get('protocol')
        server_address = request_data.get('ipAddress')
        server_port = request_data.get('port')
        url = server_protocol + "://" + server_address + ":" + server_port + "/"
        return url







