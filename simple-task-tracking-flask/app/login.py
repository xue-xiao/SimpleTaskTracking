from typing import Dict

import flask_login
from flask import request
from flask_login import LoginManager, login_required, logout_user, login_user

from app import api
from app.model.department import Department
from app.model.password import Password
from app.model.role import Role
from app.model.user import User
from app.model.user_profile import UserProfile
from app.util.response import standard_json_response, json_response_with_payload

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
            user_info_payload = get_user_info(user)
            return json_response_with_payload(True, "Login successfully.", user_info_payload)
        else:
            return standard_json_response(False, "Incorrect username or password.")


@api.route("/user_info", methods=["GET"])
def user_info():
    user: User = flask_login.current_user
    if not user.is_authenticated:
        return standard_json_response(False, "User not logged in. ")
    user_info_payload = get_user_info(user)
    return json_response_with_payload(True, "", user_info_payload)


@api.route("/logout", methods=["GET"])
@login_required
def logout():
    logout_user()
    return '{"success": true}'


def get_user_info(user: User) -> Dict[str, str]:
    profile: UserProfile = UserProfile.query.get(user.get_id())
    role: Role = Role.query.get(profile.role_id)
    department: Department = Department.query.get(profile.department_id) if profile.department_id else None
    user_info_payload = {
        "displayName": " ".join([profile.first_name, profile.last_name]) if profile.first_name else user.name,
        "userName": user.name,
        "email": user.email,
        "avatarUrl": profile.avatar,
        "gender": "M" if profile.gender else "F",
        "role": role.name,
        "department": department.name
    }
    return user_info_payload
