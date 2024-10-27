from fastapi import APIRouter, HTTPException, Response, Request
from jwt.exceptions import InvalidTokenError

from src.schemas import AuthToken, LoginSchema
from src.utils import get_user, create_token_payload, encode_jwt, \
    hash_password, decode_jwt


router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("login/", response_model=AuthToken)
async def login(payload: LoginSchema, response: Response) -> AuthToken:
    """Эндпоинт для авторизации пользователя."""

    user = await get_user(email=payload.email)

    if not user or user.password != hash_password(payload.password):
        raise HTTPException(status_code=403, detail="User not found!")

    token_payload = create_token_payload(payload.model_dump())
    auth_token = encode_jwt(token_payload)
    
    response.set_cookie("jwt_token", auth_token)

    return AuthToken(token=auth_token)


@router.get("logout/")
async def logout(response: Response):
    """Эндпоинт для выхода из системы."""

    response.delete_cookie("jwt_token")



@router.get("check_token/")
async def check_token(
        request: Request, response: Response,
        token: AuthToken | None = None) -> dict:
    """Эндпоинт для проверки наличия и валидности jwt токена."""

    if not token:
        token_cookie = request.cookies.get("jwt_token", None)

        if not token_cookie:
            raise HTTPException(status_code=401, detail="You need to log in.")
        
        try:
            payload = decode_jwt(token_cookie)
            return payload
        except InvalidTokenError:
            response.delete_cookie("jwt_token")
            raise HTTPException(status_code=401,
                                detail="User authorization error.")
    try:
        payload = decode_jwt(token.token)
        return payload
    except InvalidTokenError:
        response.delete_cookie("jwt_token")
        raise HTTPException(status_code=401,
                            detail="User authorization error.")




