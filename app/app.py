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

if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=8000)