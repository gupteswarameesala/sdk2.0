from flask import Flask, request
from core import RequestContext
from .Process_config_msg import ProcessConfigMsg
from logger import Logger
from .response_util import *
import uuid
import logging
from core import Registery
from core import Constants

logger = logging.getLogger(__name__)

app = Flask(__name__)


# /api/v2/messages?action=DISCOVERY url = "http://" + serviceAdapter + ":" + strconv.Itoa(portNo) +
# "/api/v2/messages?action=" + appMessage.action + "&module=" + appMessage.messageMetaData.module + "&subType=" +
# appMessage.messageMetaData.subType
@app.route(Constants.SERVER_URL, methods=[Constants.GET, Constants.POST])
# Creating a context object and initiating Asynchronous task.
def handle_message():
    try:
        logger.debug("Message received")
        logger.debug(request.get_json())

        context = {Constants.HTTP_HEADERS: get_http_headers(request)}
        requestContext = RequestContext(uuid.uuid4(), request.get_json())
        requestContext.context = context

        task = ProcessConfigMsg(requestContext)
        task.start()
        return response_success(
            "Task with " + get_http_headers(request)[Constants.POLL_ID] + " is successfully created")

    except Exception as e:
        logger.exception(str(e))
        return response_generic_error("Request failed")


@app.route(Constants.DEBUG_URL, methods=[Constants.POST])
def handle_debug_message():
    try:
        logger.debug("Debug Message received")
        logger.debug(request.get_json())

        context = {}
        requestContext = RequestContext(uuid.uuid4(), request.get_json())
        requestContext.context = context

        response = processDebugMessage(requestContext)
        return response_success(response)

    except Exception as e:
        logger.exception(str(e))
        return response_generic_error("Request failed")


@app.route(Constants.LOG_URL, methods=[Constants.PUT])
def handle_log_message():
    try:
        logLevel = request.args.get(Constants.LEVEL)
        logger.debug("Log Query Param received")
        logger.debug(Constants.LOGLEVEL)
        Logger().modify_log_level(logLevel)
        return response_success("Log level modified successfully")

    except Exception as e:
        logger.exception(str(e))
        return response_generic_error("Request failed")


@app.route(Constants.LIVE_URL, methods=[Constants.GET])
def app_live():
    logger.debug("app live")
    try:
        return response_success(Constants.LIVE)
    except Exception as e:
        logger.exception(str(e))
        return response_generic_error("Request failed")


class Init:
    logger.debug("app initialised")

    def start_server(self):
        if self:
            logger.info('starting server 25000...')
            app.run(host='0.0.0.0', port=26000)


@app.route(Constants.READY_URL, methods=[Constants.GET])
def app_ready():
    logger.debug("app ready")
    try:
        return response_success(Constants.READY)
    except Exception as e:
        logger.exception(str(e))
        return response_generic_error("Request failed")


def get_http_headers(req):
    http_headers = {}
    headers = []
    for i in req.headers:
        headers.append(i)
    headers = dict(headers)

    for key, value in headers.items():
        if key.startswith("Am"):
            key = key.replace("Am", "AM")
            http_headers.update([(key, value)])

    return http_headers


def processDebugMessage(requestcontext):
    handlerClass = Registery.getDebugHandler(getDebugHandlerIdentity(requestcontext.get_request_data()["module"],
                                                                     requestcontext.get_request_data()["action"]))
    aa = handlerClass()
    response = aa.debug(requestcontext)
    return response


def getDebugHandlerIdentity(module, action):
    return module + Constants.UNDERSCORE + action


def getHandlerIdentity(module, subtype, action):
    return module + Constants.UNDERSCORE + subtype + Constants.UNDERSCORE + action
