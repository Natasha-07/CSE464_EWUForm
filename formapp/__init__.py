from flask import Flask

from .extensions import mongo
from .main.routes import main


def create_app():
    app = Flask(__name__)

    app.config['UPLOAD_FOLDER'] = "static/images"
    app.config['MONGO_URI'] = 'mongodb://localhost:27017/ewu_db'

    mongo.init_app(app)
    app.register_blueprint(main)

    return app
