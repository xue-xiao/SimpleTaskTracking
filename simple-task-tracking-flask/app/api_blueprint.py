from flask import Blueprint

# Note: A Blueprint didn't add url_prefix by default.
api = Blueprint('api', __name__, url_prefix="/api")
