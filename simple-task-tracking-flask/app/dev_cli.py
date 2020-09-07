import uuid

import click
from flask.cli import with_appcontext

from app.db_instance import db
from app.model.password import Password
from app.model.user import User


@click.command('create-tables')
@with_appcontext
def create_tables():
    """Clear the existing data and create new tables."""
    db.drop_all()
    db.create_all()
    create_test_users()
    click.echo('Initialized the database.')


def create_test_users():
    admin = User(id=str(uuid.uuid4()), username='admin', email='admin@example.com')
    guest = User(id=str(uuid.uuid4()), username='guest', email='guest@example.com')
    admin_pw = Password(user_id=admin.id, password="123")
    guest_pw = Password(user_id=guest.id, password="123")

    db.session.add(admin)
    db.session.add(guest)
    db.session.add(admin_pw)
    db.session.add(guest_pw)
    db.session.commit()

