import uuid

from app.db_instance import db
from app.model.password import Password
from app.model.user import User
from app.model.user_profile import UserProfile


def create_user(user_name, email, password, role_id, department_id):
    user = User(id=str(uuid.uuid4()), name=user_name, email=email)
    pw = Password(user_id=user.id, password=password)
    profile = UserProfile(user_id=user.id, role_id=role_id, department_id=department_id)
    db.session.add(user)
    db.session.add(pw)
    db.session.add(profile)
    db.session.commit()
