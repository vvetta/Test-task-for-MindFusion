from src.db import BaseModel

from sqlalchemy import Integer, Text, ForeignKey 
from sqlalchemy.orm import mapped_column, relationship


class Message(BaseModel):
    """Модель описывающая сообщение пользователей."""

    text = mapped_column(Text(), nullable=False)
    user_id = mapped_column(Integer(), nullable=False)
    chat_id = mapped_column(Integer(), ForeignKey("chat.id"))


class Chat(BaseModel):
    """Модель описывающая чаты пользователей."""

    first_user_id = mapped_column(Integer(), nullable=False)
    second_user_id = mapped_column(Integer(), nullable=False)
    messages = relationship("Message", backref="chat")

