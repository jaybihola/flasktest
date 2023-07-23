import os
from dotenv import load_dotenv
from flask import Flask
from flask_smorest import Api

from db import db
import models

from resources.item import blp as item_blueprint
from resources.store import blp as store_blueprint
from resources.tag import blp as tag_blueprint


def create_app(db_url = None):
    default_url = "sqlite:///data.db"
    load_dotenv()

    app = Flask(__name__)
    print(os.getenv("DATABASE_URL"))
    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "V1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", default_url)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.init_app(app)

    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(item_blueprint)
    api.register_blueprint(tag_blueprint)
    api.register_blueprint(store_blueprint)

    return app

