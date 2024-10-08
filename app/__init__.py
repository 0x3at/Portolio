from os import getenv

from flask import Flask
from dotenv import load_dotenv, find_dotenv

from app.extensions import blueprint

load_dotenv(find_dotenv())


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = getenv('SECRET_KEY')
    app.config['DEBUG'] = "False"
    blueprint.init_app(app)

    return app
