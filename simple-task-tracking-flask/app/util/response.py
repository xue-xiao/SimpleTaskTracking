from typing import Dict

from flask import json


def standard_json_response(success: bool, message: str) -> str:
    return json.jsonify(success=success, message=message)


def json_response_with_payload(success: bool, message: str, payload: Dict[str, str]) -> str:
    return json.jsonify(success=success, message=message, payload=payload)
