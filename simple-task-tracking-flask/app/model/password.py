import hashlib
import uuid

from app.db_instance import db


class Password(db.Model):
    user_id = db.Column(db.String(36), primary_key=True)
    encryted_pw = db.Column(db.String(33), nullable=False)
    salt = db.Column(db.String(36), nullable=False)

    def __init__(self, user_id, password, **kwargs):
        super(Password, self).__init__(**kwargs)
        self.user_id = user_id
        self.salt = str(uuid.uuid4())
        self.encryted_pw = hashlib.md5((password + self.salt).encode('utf-8')).hexdigest()

    def __repr__(self):
        return '<Password of user id: %r>' % self.user_id

    def validate(self, password):
        input_encryted_pw = hashlib.md5((password + self.salt).encode('utf-8')).hexdigest()
        return self.encryted_pw == input_encryted_pw
