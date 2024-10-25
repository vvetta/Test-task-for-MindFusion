from typing import List 
from pydantic import BaseModel


class MessageSchema(BaseModel):
    
    text: str


class ChatSchemaSmall(BaseModel):

    members: str


class ChatSchema(ChatSchemaSmall):

    messages: List[MessageSchema]
