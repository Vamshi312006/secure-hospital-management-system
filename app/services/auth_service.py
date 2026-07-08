from sqlalchemy import or_
from argon2 import PasswordHasher

from app.extensions import db
from app.models.user import User

ph = PasswordHasher()

# Dummy hash used to reduce username enumeration timing differences.
DUMMY_HASH = ph.hash("SecureHealthcarePlatformDummyPassword")


def hash_password(password: str) -> str:
    return ph.hash(password)


def verify_password(hash_value: str, password: str) -> bool:

    try:
        return ph.verify(hash_value, password)

    except Exception:
        return False


def authenticate(username: str, password: str):

    user = User.query.filter(
        or_(
            User.username == username,
            User.email == username,
        )
    ).first()

    if user is None:

        verify_password(
            DUMMY_HASH,
            password,
        )

        return None

    if not user.is_active:

        verify_password(
            user.password_hash,
            password,
        )

        return None

    if not verify_password(
        user.password_hash,
        password,
    ):

        user.failed_login_attempts += 1

        db.session.commit()

        return None

    if ph.check_needs_rehash(
        user.password_hash,
    ):

        user.password_hash = hash_password(
            password,
        )

    user.failed_login_attempts = 0

    db.session.commit()

    return user
