import json
import time
import logging
import requests

logger = logging.getLogger(__name__)


class Time:
    def get_current_time(self):
        if self:
            return str(int(time.time()))


class Credential:

    def get_cipher(self, cipher, key):
        if self:
            url = Constants.CRED_URL + key
            payload = cipher
            headers = {
                Constants.CONTENT_TYPE: Constants.CONTENT_TYPE_VALUE
            }
            response = requests.request(Constants.GET, url, headers=headers, data=payload)
            respon = json.loads(response.text)

            return respon


class Constants:
    STATUS_OK = 200
    DISCOVERY = "DISCOVERY"
    MONITORING = "MONITORING"
    DISCOVERY_HANDLER_IDENTITY = "Discovery-Configuration-Update"
    MONITORING_HANDLER_IDENTITY = "Monitoring-Configuration-Update"
    PRODUCTION = "production"
    DEVELOPMENT = "development"
    DEVICE_REACHABILITY = "Device-Reachability"
    CRED_URL = "http://localhost:25001/api/v2/credentials/decrypt?key="
    CONTENT_TYPE = 'Content-Type'
    CONTENT_TYPE_VALUE = 'text/plain'

    GET = "GET"
    POST = 'POST'
    PUT = 'PUT'

    SERVER_URL = '/api/v2/messages'
    DEBUG_URL = '/api/v1/debug'
    LIVE_URL = '/api/v1/live'
    LOG_URL = '/api/v1/log'
    READY_URL = '/api/v1/ready'
    ACK_SIDECAR_URL = "/api/v2/messages/"
    RESOURCE_SIDECAR_URL = "/api/v2/resources"
    RELATIONSHIP_SIDECAR_URL = "/api/v2/relationships"
    METRIC_SIDECAR_URL = "/api/v2/metrics?process=true"
    ALERT_PUBLISH_URL = "/api/v2/messages/outbound_channel/publish"

    MSG_ID = "AM-Message-Id"
    POLL_ID = "AM-Poll-Id"
    APP_NATIVE_TYPE = 'AM-App-Native-Type'
    ADK_SERVICE_URI = 'ADK_SERVICE_URI'
    APP_DATA = "app_data"
    PAYLOAD = "payload"
    NATIVE_TYPES = "nativeTypes"
    NATIVE_TYPE = "nativeType"
    RESOURCE_TYPES = "resourceTypes"
    HTTP_HEADERS = "http_headers"

    TEMPLATE_ID = "templateId"
    MONITOR_ID = "monitorId"
    APPCONFIG = "appConfig"
    METRICS = "metrics"
    RESOURCES = "resources"

    LOG_LEVEL = "LOG_LEVEL"
    LOGLEVEL = "logLevel"
    DATA = "data"

    INFO = "INFO"
    DEBUG = "DEBUG"
    ERROR = "ERROR"
    LEVEL = "level"
    LIVE = "Live"
    READY = "Ready"

    UNDERSCORE = "-"
    MESSAGE = "message"

    ERROR_CODE = "error_code"
    TRUE = "true"
    FALSE = "false"
    PROCESS_INVENTORY = "?processInventory="
