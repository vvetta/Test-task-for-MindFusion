from src.schemas import ReadUser, CreateUser, UpdateUser
from src.utils import hash_password
from src.models import User

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession 
from pydantic import EmailStr
from fastapi import HTTPException
from typing import List


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


async def read_users_db(email: EmailStr | None, session: AsyncSession,
                        limit: int | None = 10, offset: int | None = 0) -> List[ReadUser]:
    """Читает пользователя или нескольких пользователей из базы данных."""

    if email:
        payload = await session.execute(select(User).where(User.email == email))
        payload = payload.fetchone()

        if not payload:
            raise HTTPException(status_code=403,
                                detail="The user with this email was not found.")
        user = payload.fetchone()[0]
        return list(ReadUser.from_orm(user))

    else:
        if limit and offset:
            payload = await session.execute(select(User).offset(offset).limit(limit))
            users = payload.scalars().all()
            return [ReadUser.from_orm(user) for user in users]
        else:
            raise HTTPException(status_code=403,
                                detail="The offset and limit parameters are required.")


async def update_user_db(current_user: ReadUser, payload: UpdateUser,
                         session: AsyncSession) -> ReadUser:
    """Обновление данных пользователя."""
    user_from_db = await session.execute(select(User)
                                        .where(User.email == current_user.email))
    user = user_from_db.fetchone()[0]

    for key, value in payload.model_dump().items():
        setattr(user, key, value)

    return ReadUser.from_orm(user)


async def delete_user_db(current_user: ReadUser, session: AsyncSession) -> ReadUser:
    """Удаление пользователя."""
    
    payload = await session.execute(select(User).where(User.email == current_user.email))
    user = payload.fetchone()[0]

    await session.delete(user)

    return ReadUser.from_orm(user)
