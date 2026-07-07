from flask import Blueprint, redirect, session

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def home():
    if session.get("user_id"):
        return redirect("/dashboard")
    return redirect("/login")
