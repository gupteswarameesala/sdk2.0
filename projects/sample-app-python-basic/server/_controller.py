from flask import Flask, request, jsonify
from handler import process_message
from logger import modify_log_level
import logging

logger = logging.getLogger(__name__)

app = Flask(__name__)

def start_server():
    app.run(host='0.0.0.0',port=25000,debug=True)

@app.route('/api/v1/live', methods=['GET'])
def app_live():
    logger.info("Live")
    return response_success("Live")

@app.route('/api/v2/messages', methods=['POST'])
def handle_message():
    cloud_message = request.get_json()
    http_headers = get_http_headers(request)
    logger.info(http_headers)
    process_message(cloud_message, http_headers)
    
    return response_success("Messages")

@app.route('/api/v1/ready', methods=['GET'])
def app_ready():
    logger.info("Ready")
    return response_success("Ready")

@app.route('/api/v1/log', methods=['PUT'])
def handle_log_message():
    logLevel = request.args.get('level')
    print("Log Query Param recieved")
    print(logLevel)
    modify_log_level(logLevel)
    return response_success("Log level modified successfully")

@app.route('/api/v1/debug', methods=['POST'])
def handle_debug_message():
    logger.info(request.get_json())
    return response_success(request.get_json())

def response_success(message):
    return jsonify({"message":message})

def response_json(data):
    return jsonify(data)

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