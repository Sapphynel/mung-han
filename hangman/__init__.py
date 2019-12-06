import random
import os

from flask import Flask, render_template
from hangman import main, auth
from hangman.extensions import db, login_manager, migrate

def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)
    return None

def register_blueprints(app):
    app.register_blueprint(main.views.blueprint)
    app.register_blueprint(auth.views.blueprint)
    return None

def create_app(test_config = None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile("config.py")

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    register_extensions(app)
    register_blueprints(app)

    return app
