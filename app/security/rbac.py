from app.models.user import User


def has_permission(user: User, permission_name: str) -> bool:
    """
    Return True if the user's role contains the given permission.
    """

    if user is None:
        return False

    if user.role is None:
        return False

    permissions = {
        permission.name
        for permission in user.role.permissions
    }

    return permission_name in permissions
