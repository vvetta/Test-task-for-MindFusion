import json

from fastapi import APIRouter, WebSocket, Depends, Request, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List 
from pydantic import EmailStr

from src.db import get_session
from src.crud import get_chats_db, create_message_db, create_chat_db, \
    get_chat_db
from src.utils import get_current_user, get_user
from src.schemas import MessageSchema, ChatSchemaSmall, ChatSchema


router = APIRouter(prefix="messages/", tags=["Messages"])



@router.get("chats/", response_model=List[ChatSchemaSmall])
async def get_chats(
                    session: AsyncSession = Depends(get_session),
                    request: Request) -> List[ChatSchemaSmall]:
    """Возвращает все чаты авторизованного пользователя."""

    current_user = await get_current_user(request)
    chats = await get_chats_db(session, current_user)

    return chats


@router.post("chats/", response_model=ChatSchema)
async def create_chat(
                      session: AsyncSession = Depends(get_session),
                      email: EmailStr, request: Request) -> ChatSchema:
    """Создает личный чат с пользователем."""

    current_user = await get_current_user(request=request)
    companion = await get_user(email) 
    chat = await create_chat_db(session, current_user, companion)

    return chat



@router.websocket("chats/{chat_id}")
async def messanger_endpoint(
                             websocket: WebSocket,
                             chat_id: int, request: Request,
                             session: AsyncSession = Depends(get_session)):
    """WebSocket соединение для отправки сообщений."""

    await websocket.accept()
    current_user = await get_current_user(request=request)

    try:
        # Проверяем является ли пользователь участником указанного чата.
        chat = await get_chat_db(session, chat_id)

        if current_user.id not in chat.members_id:
            raise HTTPException(status_code=403, detail="")

        while True:
            data = await websocket.receive_text()
            data = json.loads(data)

            message_content = data.get("message")

            await websocket.send_text(f"{current_user.email}: \
                {message_content}")
    except Exception as e:
        print(e)
    finally:
        await websocket.close()

