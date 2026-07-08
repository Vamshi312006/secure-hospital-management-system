from functools import wraps
from datetime import datetime

from flask import (
    Blueprint,
    flash,
    redirect,
    render_template,
    request,
    session,
    url_for,
)

from app.extensions import db, limiter
from app.services.auth_service import authenticate

auth_bp = Blueprint("auth", __name__)


def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user_id" not in session:
            return redirect(url_for("auth.login_page"))
        return f(*args, **kwargs)
    return wrapper


@auth_bp.route("/login", methods=["GET"])
def login_page():
    return render_template("auth/login.html")


@auth_bp.route("/login", methods=["POST"])
@limiter.limit("5 per minute")
def login():

    username = request.form.get("username")
    password = request.form.get("password")

    if not username or not password:
        flash("Username and password are required.")
        return redirect(url_for("auth.login_page"))

    user = authenticate(username, password)

    if user is None:
        flash("Invalid username or password.")
        return redirect(url_for("auth.login_page"))

    user.last_login = datetime.utcnow()
    db.session.commit()

    session.clear()

    session["user_id"] = user.id
    session["username"] = user.username
    session["role"] = user.role.name

    flash("Login successful.")

    return redirect(url_for("dashboard.dashboard"))


@auth_bp.route("/logout")
def logout():

    session.clear()

    flash("Logged out successfully.")

    return redirect(url_for("auth.login_page"))
