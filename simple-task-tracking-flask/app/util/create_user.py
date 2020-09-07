import uuid

from app.db_instance import db
from app.model.password import Password
from app.model.user import User


def create_user(username, email, password):
    user = User(id=str(uuid.uuid4()), username=username, email=email)
    pw = Password(user_id=user.id, password=password)
    db.session.add(user)
    db.session.add(pw)
    db.session.commit()
