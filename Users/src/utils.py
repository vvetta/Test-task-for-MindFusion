import jwt
import hashlib

from fastapi import Request, HTTPException

from src.schemas import ReadUser
from src.settings import ALGORITHM, public_key


def hash_password(password: str) -> str:
    """Хэширует полученный пароль."""

    return hashlib.sha256(password.encode()).hexdigest()


def decode_jwt_token(token: str, public_key: str = public_key, 
                     algorithm: str = ALGORITHM) -> dict:
    """Декодирует jwt токен в словарь."""

    decode = jwt.decode(token, public_key, algorithms=[algorithm])
    return decode


def get_current_user(request: Request) -> ReadUser:
    """Получает данные из токена пользователя."""
    
    token = request.cookies.get("jwt_token")
    if not token:
        raise HTTPException(status_code=401,
                            detail="The user is not authorized")

    payload = decode_jwt_token(token)

    return ReadUser(**payload)

