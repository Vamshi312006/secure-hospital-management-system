from functools import wraps

from flask import flash, redirect, session, url_for


def login_required(f):
    @wraps(f)
    def wrapped(*args, **kwargs):
        if "user_id" not in session:
            flash("Please login first.")
            return redirect(url_for("home") + "#login")
        return f(*args, **kwargs)

    return wrapped
