from pydantic import BaseModel, EmailStr


class CreateUser(BaseModel):

    email: EmailStr
    password: str


class ReadUser(BaseModel):

    email: EmailStr
    
    class Config:
        from_attributes = True


class UpdateUser(BaseModel):

    username: str

