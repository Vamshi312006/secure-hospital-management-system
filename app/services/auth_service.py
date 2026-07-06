from sqlalchemy import or_
from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

from app.extensions import db
from app.models.user import User

ph = PasswordHasher()


def hash_password(password: str) -> str:
    return ph.hash(password)


def verify_password(hash_value: str, password: str) -> bool:
    try:
        return ph.verify(hash_value, password)
    except VerifyMismatchError:
        return False


def authenticate(username: str, password: str):

    user = User.query.filter(
        or_(
            User.username == username,
            User.email == username,
        )
    ).first()

    if user is None:
        return None

    if not user.is_active:
        return None

    if not verify_password(user.password_hash, password):
        user.failed_login_attempts += 1
        db.session.commit()
        return None

    user.failed_login_attempts = 0
    db.session.commit()

    return user
