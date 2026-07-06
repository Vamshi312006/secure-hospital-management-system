import hashlib
import secrets


def generate_session_token() -> str:
    return secrets.token_urlsafe(64)


def hash_session_token(token: str) -> str:
    return hashlib.sha256(token.encode()).hexdigest()


def compare_session_hash(token: str, stored_hash: str) -> bool:
    return hash_session_token(token) == stored_hash
