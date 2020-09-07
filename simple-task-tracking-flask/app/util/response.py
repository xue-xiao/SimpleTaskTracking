from flask import json

def standard_json_response(success: bool, message: str) -> str:
    return json.jsonify(success=success, message=message)

