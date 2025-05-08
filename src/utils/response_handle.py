from flask import jsonify


def api_response(success, message, data, status_code):
    response = {
        "success": success,
        "message": message,
        "data": data
    }
    return jsonify(response), status_code