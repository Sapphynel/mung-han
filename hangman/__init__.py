import random
import os

from flask import Flask, render_template
from hangman import main
from hangman.extensions import db, login_manager

def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)
    return None

def register_blueprints(app):
    app.register_blueprint(main.views.blueprint)
    return None

def create_app(test_config = None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hangman.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

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
