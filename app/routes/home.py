from flask import Blueprint, render_template, session

home_bp = Blueprint("home", __name__)


@home_bp.route("/")
def home():
    if "user_id" not in session:
        return render_template("index.html", show_login=True)

    return render_template("index.html")


@home_bp.route("/index")
def index():
    return home()


@home_bp.route("/dashboard")
def dashboard():
    return "<h1>Dashboard Working ✅</h1>"
