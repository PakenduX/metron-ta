import os
from dotenv import load_dotenv
from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from datetime import timedelta

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()


def create_app(test_config=None):
    app = Flask(__name__)
    load_dotenv()
    app.config.from_mapping(
        SQLALCHEMY_DATABASE_URI=os.environ.get("SQLALCHEMY_DATABASE_URI"),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        JWT_SECRET_KEY=os.environ.get("JWT_SECRET_KEY"),
        JWT_ACCESS_TOKEN_EXPIRES=timedelta(
            days=int(os.environ.get("JWT_ACCESS_TOKEN_EXPIRES"))
        ),
    )
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    if test_config is not None:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI"
        )

    app.register_blueprint(managers)
    app.register_blueprint(auth)
    app.register_blueprint(sites)
    app.register_blueprint(assets)

    return app


from app.controllers.managerController import managers
from app.controllers.authController import auth
from app.controllers.siteController import sites
from app.controllers.assetController import assets
