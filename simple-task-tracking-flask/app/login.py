from flask import request
from flask_login import LoginManager, login_required, logout_user, login_user, current_user

from app import api
from app.model.password import Password
from app.model.user import User
from app.util.response import standard_json_response

login_manager = LoginManager()


@login_manager.user_loader
def load_user(user_id):
    #  It will return None if the ID is not valid.
    return User.query.get(user_id)


@api.route("/login", methods=["POST"])
def login():
    cred = request.get_json()
    if cred is None:
        return standard_json_response(False, "Invalid json or missing 'Content-Type: application/json'.")
    elif "email" not in cred or "password" not in cred:
        return standard_json_response(False, "Missing email or password in request.")
    else:
        user: User = User.query.filter_by(email=cred['email']).first()
        if user is not None and Password.query.get(user.get_id()).validate(cred['password']):
            login_user(user, remember=cred.get('remember', False))
            return standard_json_response(True, "Login successfully.")
        else:
            return standard_json_response(False, "Incorrect username or password.")


@api.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return '{"success": true}'
