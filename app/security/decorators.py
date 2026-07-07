from functools import wraps

from flask import abort, session

from app.models.user import User
from app.security.rbac import has_permission


def permission_required(permission_name):

    def decorator(view):

        @wraps(view)
        def wrapped(*args, **kwargs):

            user_id = session.get("user_id")

            if not user_id:
                abort(401)

            user = User.query.get(user_id)

            if not user:
                abort(401)

            if not has_permission(user, permission_name):
                abort(403)

            return view(*args, **kwargs)

        return wrapped

    return decorator
