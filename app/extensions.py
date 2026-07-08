from flask import request

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_limiter import Limiter

db = SQLAlchemy()
migrate = Migrate()


def login_rate_limit_key():

    ip = request.remote_addr or "unknown"

    username = (
        request.form.get("username", "")
        .strip()
        .lower()
    )

    return f"{ip}:{username}"


limiter = Limiter(
    key_func=login_rate_limit_key,
    default_limits=[],
)
