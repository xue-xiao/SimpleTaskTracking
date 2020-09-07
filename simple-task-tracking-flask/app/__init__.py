from flask import Flask

from app.api_blueprint import api
from app.login import login_manager
from app.db_instance import db as sqlalchemy
from app.dev_cli import create_tables
from flask_cors import CORS

def create_app(stage='dev'):
    app = Flask(__name__, instance_relative_config=True)
    if stage == 'dev':
        app.config.from_pyfile('dev_config.py')
        # CLI: flask create-tables
        app.cli.add_command(create_tables)


    else:
        app.config.from_pyfile('prod_config.py')

    # initialize SQLAlchemy
    sqlalchemy.init_app(app)

    # initialize LoginManager
    login_manager.init_app(app)

    # Register blueprints
    app.register_blueprint(api)

    # Enable Cross Origin Resource Sharing for all domain:port and all routes
    CORS(app, supports_credentials=True)

    @app.route('/ping')
    def ping():
        return 'OK'

    return app
