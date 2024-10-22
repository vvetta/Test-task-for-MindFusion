import hashlib


def hash_password(password: str) -> str:
    """Шифрует полученный пароль."""

    return hashlib.sha256(password.encode()).hexdigest()

