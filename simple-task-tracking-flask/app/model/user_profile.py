from flask_login import UserMixin

from app.db_instance import db


class UserProfile(db.Model):
    user_id = db.Column(db.String(36), primary_key=True)
    role_id = db.Column(db.Integer, unique=False, nullable=False)
    department_id = db.Column(db.Integer, unique=False, nullable=False)

    # Nullables:
    first_name = db.Column(db.String(50), unique=False, nullable=True)
    last_name = db.Column(db.String(50), unique=False, nullable=True)
    avatar = db.Column(db.String(300), unique=False, nullable=True)
    gender = db.Column(db.Boolean, nullable=True, comment="T for Male, F for Female", default=None)

    def __repr__(self):
        return f'<User: {self.first_name} {self.last_name}>'
