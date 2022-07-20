from flask import Flask, request
from core import RequestContext
from .Process_config_msg import ProcessConfigMsg
from logger import Logger
from .response_util import *
import uuid
import logging
from core import Registery

logger = logging.getLogger(__name__)

app = Flask(__name__)


# /api/v2/messages?action=DISCOVERY
# url = "http://" + serviceAdapter + ":" + strconv.Itoa(portNo) + "/api/v2/messages?action=" + appMessage.action + "&module=" + appMessage.messageMetaData.module + "&subType=" + appMessage.messageMetaData.subType
@app.route('/api/v2/messages', methods=['GET', 'POST'])
# Creating a context object and initiating Asynchronous task.
def handle_message():
    try:
        logger.debug("Message recieved")
        logger.debug(request.get_json())

        context ={}
        context["http_headers"] = get_http_headers(request)
        requestContext = RequestContext(uuid.uuid4(), request.get_json())
        requestContext.context = context

        task = ProcessConfigMsg(requestContext)
        task.start()
        return response_success("Task with " + get_http_headers(request)["AM-Poll-Id"] + " is successfully created")

    except Exception as e:
        logger.exception(str(e))
        return response_generic_error("Request failed")

@app.route('/api/v1/debug', methods=['POST'])
def handle_debug_message():
    try:
        logger.debug("Debug Message recieved")
        logger.debug(request.get_json())

        context ={}
        requestContext = RequestContext(uuid.uuid4(), request.get_json())
        requestContext.context = context

        response = processDebugMessage(requestContext)
        requestContext = None
        return response_success(response)

    except Exception as e:
        logger.exception(str(e))
        return response_generic_error("Request failed")

@app.route('/api/v1/log', methods=['PUT'])
def handle_log_message():
    try:
        logLevel = request.args.get('level')
        logger.debug("Log Query Param recieved")
        logger.debug("logLevel")
        Logger().modify_log_level(logLevel)
        return response_success("Log level modified successfully")

    except Exception as e:
        logger.exception(str(e))
        return response_generic_error("Request failed")


@app.route('/api/v1/live', methods=['GET'])
def app_live():
    logger.debug("app live")
    try:
        return response_success("Live")
    except Exception as e:
        logger.exception(str(e))
        return response_generic_error("Request failed")


@app.route('/api/v1/ready', methods=['GET'])
def app_ready():
    logger.debug("app ready")
    try:
        return response_success("Ready")
    except Exception as e:
        logger.exception(str(e))
        return response_generic_error("Request failed")


class Init:
    logger.debug("app initialised")
    def start_server(self):
        logger.info('starting server 25000...')
        app.run(host='0.0.0.0', port=25000)

def get_http_headers(request):
        http_headers = {}
        headers = []
        for i in request.headers:
            headers.append(i)
        headers = dict(headers)

        for key, value in headers.items():
            if key.startswith("Am"):
                key = key.replace("Am", "AM")
                http_headers.update([(key, value)])

        return http_headers

def processDebugMessage(requestContext):
    handlerClass = Registery.getDebugHandler(getDebugHandlerIdentity(requestContext.get_request_data()["module"], requestContext.get_request_data()["action"]))
    aa = handlerClass()
    response = aa.debug(requestContext)
    return response

def getDebugHandlerIdentity(module,action):
    return module + "-"  + action

def getHandlerIdentity(module, subtype, action):
    return module + "-" + subtype + "-" + action
