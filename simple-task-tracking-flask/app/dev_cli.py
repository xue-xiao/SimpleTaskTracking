import click
from flask.cli import with_appcontext

from app.db_instance import db
from app.model.department import Department
from app.model.role import Role
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
    create_roles()
    create_department()
    create_dev_users()
    click.echo('Initialized the database.')


def create_department():
    department = Department(name="Unspecified")
    db.session.add(department)
    db.session.commit()

def create_roles():
    admin_role = Role(name='admin')
    user_role = Role(name='user')
    db.session.add(admin_role)
    db.session.add(user_role)
    db.session.commit()


def create_dev_users():
    create_user(user_name='admin', email='admin@example.com', password="123", role_id=1, department_id=1)
    create_user(user_name='guest', email='guest@example.com', password="123", role_id=2, department_id=1)
