from app.models.user import User


def has_permission(user: User, permission_name: str) -> bool:
    """
    Return True if the given user has the requested permission.
    """

    if user is None:
        return False

    if user.role is None:
        return False

    return any(
        permission.name == permission_name
        for permission in user.role.permissions
    )
