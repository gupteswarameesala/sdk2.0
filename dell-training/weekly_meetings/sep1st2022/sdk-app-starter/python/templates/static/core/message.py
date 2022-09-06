import logging
import os
import json
from httpclient import Url
from .util import Constants

logger = logging.getLogger(__name__)
base_adk_url = os.getenv(Constants.ADK_SERVICE_URI)
environment = Constants.PRODUCTION


class GatewayToCloudMessage:

    @staticmethod
    def post_acknowledge(http_headers, s):
        if environment == Constants.PRODUCTION:
            url = base_adk_url + Constants.ACK_SIDECAR_URL + http_headers[Constants.MSG_ID] + \
                  Constants.PROCESS_INVENTORY + s
            logger.info("acknowledgement with Poll Id " + http_headers[Constants.POLL_ID] + " is successful")
            status_code = Url.putAck(url, http_headers)
            if status_code == Constants.STATUS_OK:
                logger.info("Acknowledge posted successfully.")
            else:
                logger.info("Acknowledge posted failed.")
        else:
            pass

    @staticmethod
    def publish_resources(http_headers, resource_list):
        if environment == Constants.PRODUCTION:
            url = base_adk_url + Constants.RESOURCE_SIDECAR_URL
            status_code = Url.put(url, json.dumps(resource_list), http_headers)
            if status_code == Constants.STATUS_OK:
                logger.info("resources posted " + str(resource_list) + " with Poll Id " + str(
                    http_headers[Constants.POLL_ID]))
        else:
            logger.info(json.dumps(resource_list))

    @staticmethod
    def publish_relationships(http_headers, relation_list):
        if environment == Constants.PRODUCTION:
            url = base_adk_url + Constants.RELATIONSHIP_SIDECAR_URL
            status_code = Url.put(url, json.dumps(relation_list), http_headers)
            if status_code == Constants.STATUS_OK:
                logger.debug("relations posted " + str(relation_list) + " with Poll Id " + str(
                    http_headers[Constants.POLL_ID]))
        else:
            logger.info(json.dumps(relation_list))

    @staticmethod
    def publish_metrics(http_headers, metrics_list):
        if environment == Constants.PRODUCTION:
            url = base_adk_url + Constants.METRIC_SIDECAR_URL
            status_code = Url.post(url, json.dumps(metrics_list), http_headers)
            if status_code == Constants.STATUS_OK:
                logger.info("metrics posted" + str(metrics_list))
            else:
                logger.info("metrics posted failed.")
                logger.info(str(status_code))
        else:
            logger.info(json.dumps(metrics_list))

    @staticmethod
    def publish_alerts(http_headers, alert):
        if environment == Constants.PRODUCTION:

            url = base_adk_url + Constants.ALERT_PUBLISH_URL
            status_code = Url.post(url, json.dumps(alert), http_headers)
            if status_code == Constants.STATUS_OK:
                logger.info("alerts posted" + str(alert))
            else:
                logger.info("Acknowledge posted failed.")
                logger.info(str(status_code))
        else:
            logger.info(json.dumps(alert))
