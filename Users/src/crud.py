from src.schemas import ReadUser, CreateUser
from src.utils import hash_password
from src.models import User

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession 


async def create_user_db(payload: CreateUser,
                         session: AsyncSession) -> ReadUser:
    """Создание пользователя."""

    new_user = User(**payload.model_dump())
    new_user.password = hash_password(payload.password)
    session.add(new_user)

    try:
        await session.commit()
        return ReadUser.from_orm(new_user)
    except Exception:
        await session.rollback()


async def read_users_db(session: AsyncSession) -> list(ReadUser):
    pass

