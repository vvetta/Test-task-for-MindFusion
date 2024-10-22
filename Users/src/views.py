from fastapi import APIRouter
from src.schemas import CreateUser, ReadUser

router = APIRouter(prefix="users/", tags=["Users"])


@router.post('create_user/', response_model=ReadUser)
async def create_user(payload: CreateUser) -> ReadUser:
    """Создание пользователя."""
    pass


@router.get('read_user/', response_model=list(ReadUser))
async def read_user() -> list(ReadUser):
    """Возвращается список из одного пользователя или сразу множества."""
    pass


@router.put('update_user/', response_model=ReadUser)
async def update_user() -> ReadUser:
    """Обновление пользователя."""
    pass


@router.delete('delete_user/', response_model=ReadUser)
async def delete_user() -> ReadUser:
    """Удаление пользователя."""
    pass

