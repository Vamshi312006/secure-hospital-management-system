from flask import (
    Flask,
    flash,
    redirect,
    request,
    url_for,
)

from flask_limiter.errors import RateLimitExceeded

from app.config import Config
from app.extensions import db, migrate, limiter
from app.models import *

from app.routes import (
    home_bp,
    auth_bp,
    dashboard_bp,
    dev_bp,
    patient_bp,
    doctor_bp,
)


def create_app():

    app = Flask(
        __name__,
        template_folder="../templates",
        static_folder="../static",
    )

    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    limiter.init_app(app)

    @app.errorhandler(RateLimitExceeded)
    def handle_rate_limit(e):

        flash(
            "Too many login attempts. Please wait one minute and try again.",
            "danger",
        )

        return redirect(
            request.referrer or url_for("auth.login_page")
        )

    app.register_blueprint(home_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(dev_bp)
    app.register_blueprint(patient_bp)
    app.register_blueprint(doctor_bp)

    return app
