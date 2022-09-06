from flask import jsonify
from core import Constants


def response_success(message):
    return jsonify({
        Constants.MESSAGE: message,
    })


def response_custom_error(error_code, message, http_error_code=500):
    return jsonify({
        Constants.ERROR_CODE: error_code,
        Constants.MESSAGE: message
    }), http_error_code


def response_generic_error(message):
    return jsonify({
        Constants.ERROR_CODE: 1,
        Constants.MESSAGE: message
    }), 500


def response_json(data):
    return jsonify(data)
