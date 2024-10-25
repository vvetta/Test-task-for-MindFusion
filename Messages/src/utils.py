import jwt
import aiohttp

from fastapi import Request, HTTPException
from pydantic import EmailStr

from src.settings import public_key, ALGORITHM


class User():

    def __init__(self, user_id: int, user_email: EmailStr):
        self.id = user_id
        self.email = user_email


def decode_jwt(token: str, public_key: str = public_key, algorithm: str = ALGORITHM) -> dict:

    decoded = jwt.decode(token, public_key, algorithms=[algorithm])

    return decoded


async def get_user(email: EmailStr):
    pass


async def get_current_user(request: Request) -> User:
    """Получает информацию о авторизованном пользователе"""

    token = request.cookies.get("jwt-token")

    if not token:
        raise HTTPException(status_code=401, detail="")

    current_user_payload = decode_jwt(token)

    current_user = User(
                        user_id=current_user_payload['user_id'], 
                        user_email=current_user_payload['email'])

    return current_user
