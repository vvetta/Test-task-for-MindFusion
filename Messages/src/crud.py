from sqlalchemy.ext.asyncio import AsyncSession

from src.schemas import ChatSchema, MessageSchema, ChatSchemaSmall


async def get_chats_db(
        session: AsyncSession,
        current_user):
    pass


async def create_message_db(
        session: AsyncSession,
        current_user):
    pass


async def create_chat_db(
        session: AsyncSession, 
        current_user,
        companion):
    pass


async def get_chat_db(session: AsyncSession, chat_id: int):
    pass
