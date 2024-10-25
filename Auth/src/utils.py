import jwt
import hashlib
import aiohttp

from pydantic import EmailStr
from datetime import datetime, timedelta
from aiohttp.client_exceptions import ClientError

from src.schemas import LoginSchema
from src.settings import ACCESS_TOKEN_LIFE_TIME_MINUTES, ALGORITHM, \
    private_key, public_key, USERS_SERVICE_URL


async def get_user(email: EmailStr) -> LoginSchema:
    """Отправляет get запрос на получение пользователя \
    из сервиса пользователей."""
    
    async with aiohttp.ClientSession() as session:
        async with session.get(USERS_SERVICE_URL+email) as response:
            if 300 > response.status > 200:
                resp_body = await response.json()
                return LoginSchema(
                    email=resp_body.email, 
                    password=resp_body.password)
            else:
                raise ClientError
    

def create_token_payload(payload: dict) -> dict:
    new_payload = {}
    
    for key, value in payload:
        new_payload[key] = value
    
    new_payload["sub"] = payload.get("username", None)

    return new_payload


def encode_jwt(payload: dict, private_key: str = private_key,
               algorithm: str = ALGORITHM,
               expire_minutes: int = ACCESS_TOKEN_LIFE_TIME_MINUTES) -> str:

    now = datetime.utcnow()
    expire = now + timedelta(minutes=expire_minutes)
    payload.update(exp=expire, iat=now)
    encoded = jwt.encode(payload, private_key, algorithm)

    return encoded


def decode_jwt(token: str, public_key: str = public_key,
               algorithm: str = ALGORITHM) -> dict:

    decoded = jwt.decode(token, public_key, algorithms=[algorithm])

    return decoded


def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()

