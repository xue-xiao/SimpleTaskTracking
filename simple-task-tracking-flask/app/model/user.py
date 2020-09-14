from flask_login import UserMixin

from app.db_instance import db


class User(db.Model, UserMixin):
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False, index=True)
    is_active = db.Column(db.Boolean, default=True)

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)

    def __repr__(self):
        return '<User %r>' % self.name

    def get_id(self):
        return self.id
