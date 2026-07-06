from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError

ph = PasswordHasher()


def hash_password(password: str) -> str:
    return ph.hash(password)


def verify_password(hash_value: str, password: str) -> bool:
    try:
        return ph.verify(hash_value, password)
    except VerifyMismatchError:
        return False
