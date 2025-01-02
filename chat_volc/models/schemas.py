
from pydantic import BaseModel
from typing import List, Optional

class UserCreate(BaseModel):
    user_id: Optional[int] = None
    # email: str

class UserResponse(BaseModel):
    id: int
    username: str
    # email: str

    class Config:
        from_attributes = True
        # orm_mode = True


class PrivateChatBase(BaseModel):
    user_one_id: int
    user_two_id: int

class PrivateChatCreate(PrivateChatBase):
    pass

class PrivateChat(PrivateChatBase):
    id: int
    messages: List[int]  # Список идентификаторов сообщений, связанных с чатом

    class Config:
        from_attributes = True

class MessageBase(BaseModel):
    chat_id: int
    user_id: int
    text: str

class MessageCreate(MessageBase):
    pass

class Message(MessageBase):
    id: int

    class Config:
        from_attributes = True