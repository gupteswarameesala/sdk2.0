from flask import jsonify

def response_success(message):
    return jsonify({
              "message": message,
         })

def response_custom_error(errorCode, message, http_error_code = 500):
    return jsonify({
              "error_code": errorCode,
              "message": message
         }), http_error_code

def response_generic_error(message):
    return jsonify({
              "error_code": 1,
              "message": message
         }), 500

def response_json(data):
    return jsonify(data)