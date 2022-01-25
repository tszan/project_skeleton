from flask import Flask, jsonify
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from .common.error import ExceptionBase
from endpoints import config


DB = SQLAlchemy()

def _register_global_context(flask_app):
    # global handlers
    @flask_app.errorhandler(ExceptionBase)
    def handle_custom_exception_error(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response


def create_app():
    flask_app = Flask(__name__)
    flask_app.secret_key = config.SECRET_KEY
    flask_app.config.from_object('endpoints.config')

    DB.init_app(flask_app)
    Migrate(flask_app, DB)
    _register_global_context(flask_app)

    return flask_app

APP =  create_app()
