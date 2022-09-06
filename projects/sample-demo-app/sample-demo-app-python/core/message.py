import requests
import logging
import os
import json
import time
from httpclient import Url
from .util import Constants

logger = logging.getLogger(__name__)
base_adk_url = os.getenv('ADK_SERVICE_URI')
environment = "production"


class GatewayToCloudMessage:

    @staticmethod
    def post_acknowledge(http_headers, s):
        if environment == "production":
            url = base_adk_url + "/api/v2/messages/" + http_headers["AM-Message-Id"] + "?processInventory=" + s
            logger.info("acknowledgement with Poll Id " + http_headers["AM-Poll-Id"] + " is successful")
            status_code = Url.putAck(url, http_headers)
            if status_code == Constants.STATUS_OK:
                logger.info("Acknowledge posted successfully.")
            else:
                logger.info("Acknowledge posted failed.")
        else:
            pass

    @staticmethod
    def publish_resources(http_headers, resource_list):
        if environment == "production":
            url = base_adk_url + "/api/v2/resources"
            status_code = Url.put(url, json.dumps(resource_list), http_headers)
            if status_code == Constants.STATUS_OK:
                logger.info("resources posted " + str(resource_list) + " with Poll Id " + str(
                    http_headers["AM-Poll-Id"]))
        else:
            logger.info(json.dumps(resource_list))

    @staticmethod
    def publish_relationships(http_headers, relation_list):
        if environment == "production":
            url = base_adk_url + "/api/v2/relationships"
            status_code = Url.put(url, json.dumps(relation_list), http_headers)
            if status_code == Constants.STATUS_OK:
                logger.debug("relations posted " + str(relation_list) + " with Poll Id " + str(
                    http_headers["AM-Poll-Id"]))
        else:
            logger.info(json.dumps(relation_list))

    @staticmethod
    def publish_metrics(http_headers, metrics_list):
        if environment == "production":
            url = base_adk_url + "/api/v2/metrics?process=true"
            status_code = Url.post(url, json.dumps(metrics_list), http_headers)
            if status_code == Constants.STATUS_OK:
                logger.info("metrics posted" + str(metrics_list))
            else:
                logger.info("Acknowledge posted failed.")
                logger.info(str(status_code))
        else:
            logger.info(json.dumps(metrics_list))

    @staticmethod
    def publish_alerts(http_headers, alert):
        if environment == "production":
            url = base_adk_url + "/api/v2/messages/outbound_channel/publish"
            status_code = Url.post(url, json.dumps(alert), http_headers)
            if status_code == Constants.STATUS_OK:
                logger.info("alerts posted" + str(alert))
            else:
                logger.info("Acknowledge posted failed.")
                logger.info(str(status_code))
        else:
            logger.info(json.dumps(alert))