from flask import Flask

from app.config import Config
from app.extensions import db, migrate
from app.models import *

from app.routes import home_bp, auth_bp


def create_app():
    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static",
    )

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)

    return app
