from flask import Flask
from flask_cors import CORS

from app.api_blueprint import api
from app.db_instance import db as sqlalchemy
from app.dev_cli import create_tables
from app.login import login_manager


def create_app(stage='dev'):
    app = Flask(
        __name__,
        instance_relative_config=True,
        static_url_path='',

    )

    if stage == 'dev':
        app.config.from_pyfile('dev_config.py')
        # CLI: flask create-tables
        app.cli.add_command(create_tables)

        # Enable Cross Origin Resource Sharing for all domain:port and all routes
        CORS(app, supports_credentials=True)

    else:
        app.config.from_pyfile('prod_config.py')

    # initialize SQLAlchemy
    sqlalchemy.init_app(app)

    # initialize LoginManager
    login_manager.init_app(app)

    # Register blueprints
    app.register_blueprint(api)

    @app.route('/ping')
    def ping():
        return 'OK'

    @app.route('/')
    def index():
        return app.send_static_file('index.html')

    # We need a catch-all routing rule so that all requests go to Vue single-page-app
    # the actual routing will be done by vue-router.
    # Ref: https://router.vuejs.org/guide/essentials/history-mode.html#example-server-configurations
    @app.errorhandler(404)
    def catch_all(path):
        print(path)
        return app.send_static_file('index.html')

    return app
