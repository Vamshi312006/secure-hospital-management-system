from functools import wraps

from flask import abort, session

from app.extensions import db
from app.models.user import User
from app.security.rbac import has_permission


def permission_required(permission_name: str):

    def decorator(view):

        @wraps(view)
        def wrapped(*args, **kwargs):

            user_id = session.get("user_id")

            if user_id is None:
                abort(401)

            user = db.session.get(User, user_id)

            if user is None:
                abort(401)

            if not has_permission(user, permission_name):
                abort(403)

            return view(*args, **kwargs)

        return wrapped

    return decorator
