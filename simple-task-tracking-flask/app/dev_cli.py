import click
from flask.cli import with_appcontext

from app.db_instance import db
from app.util.create_user import create_user

# CLI: flask create-tables
# Note: Only enable CLI for dev environment.
#       Production database should be created only once.
@click.command('create-tables')
@with_appcontext
def create_tables():
    """Clear the existing data and create new tables."""
    db.drop_all()
    db.create_all()
    create_dev_users()
    click.echo('Initialized the database.')


def create_dev_users():
    create_user(username='admin', email='admin@example.com', password="123")
    create_user(username='guest', email='guest@example.com', password="123")
