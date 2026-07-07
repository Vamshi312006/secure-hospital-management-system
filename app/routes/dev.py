from flask import Blueprint, render_template

dev_bp = Blueprint("dev", __name__)

@dev_bp.route("/dev/forms")
def forms():
    return render_template("dev/forms.html")
