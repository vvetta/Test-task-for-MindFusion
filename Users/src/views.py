from fastapi import APIRouter, Depends, Request
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from pydantic import EmailStr

from src.schemas import CreateUser, ReadUser, UpdateUser
from src.crud import create_user_db, read_users_db, update_user_db, delete_user_db
from src.utils import get_current_user
from src.db import get_session


router = APIRouter(prefix="users/", tags=["Users"])


@router.post('create_user/', response_model=ReadUser)
async def create_user(payload: CreateUser, 
                      session: AsyncSession = Depends(get_session)) -> ReadUser:
    """Создание пользователя."""
    
    user = await create_user_db(payload, session)
    return user


@router.get('read_user/', response_model=List[ReadUser])
async def read_user(email: EmailStr | None, limit: int | None, offset: int | None,
                    session: AsyncSession = Depends(get_session)) -> List[ReadUser]:
    """Возвращается список из одного пользователя или сразу множества."""
    
    users = await read_users_db(email=email, offset=offset,
                                limit=limit, session=session)
    return users


@router.put('update_user/', response_model=ReadUser)
async def update_user(payload: UpdateUser,
                      session: AsyncSession = Depends(get_session),
                      current_user: ReadUser = Depends(get_current_user(Request))) -> ReadUser:
    """Обновление пользователя."""
    
    user = await update_user_db(payload=payload, session=session,
                                current_user=current_user)
    return user


@router.delete('delete_user/', response_model=ReadUser)
async def delete_user(session: AsyncSession = Depends(get_session),
                      current_user: ReadUser = Depends(get_current_user(Request))) -> ReadUser:
    """Удаление пользователя."""
    
    user = await delete_user_db(session=session, current_user=current_user)
    return user

