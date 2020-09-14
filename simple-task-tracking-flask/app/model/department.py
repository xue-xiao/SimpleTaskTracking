from flask_login import UserMixin

from app.db_instance import db


class Department(db.Model):
    id = db.Column(db.Integer(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

    def __repr__(self):
        return f'<Department: {self.name}>'
