from pydantic import EmailStr, BaseModel


class LoginSchema(BaseModel):

    email: EmailStr
    password: str


class AuthToken(BaseModel):

    token: str
