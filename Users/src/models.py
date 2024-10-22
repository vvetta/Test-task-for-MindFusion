from src.db import BaseModel

from sqlalchemy import String
from sqlalchemy.orm import mapped_column


class User(BaseModel):

    email = mapped_column(String(), nullable=False, unique=True)
    password = mapped_column(String(), nullable=False)

