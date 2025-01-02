from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    DateTime,
    Boolean,
    UniqueConstraint,
)
from sqlalchemy.orm import relationship
from datetime import datetime

import uuid
from chat_volc.settings import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    uid = Column(String, unique=True, default=str(uuid.uuid4()))
    username = Column(String, index=True)

    def __repr__(self):
        return f"<User(uid='{self.uid}', username='{self.username}')>"


class PrivateChat(Base):
    __tablename__ = "private_chats"

    id = Column(Integer, primary_key=True, index=True)
    user_one_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user_two_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    messages = relationship("Message", back_populates="chat")

    def create_chat(db, user_one_id, user_two_id):
        existing_chat = (
            db.query(PrivateChat)
            .filter(
                (
                    (PrivateChat.user_one_id == user_one_id)
                    & (PrivateChat.user_two_id == user_two_id)
                )
                | (
                    (PrivateChat.user_one_id == user_two_id)
                    & (PrivateChat.user_two_id == user_one_id)
                )
            )
            .first()
        )

        if existing_chat:
            raise Exception("Chat already exists between these two users.")

        new_chat = PrivateChat(user_one_id=user_one_id, user_two_id=user_two_id)
        db.add(new_chat)
        db.commit()
        return new_chat


class Message(Base):
    __tablename__ = "messages"
    """
    id: Уникальный идентификатор сообщения.
    chat_id: Внешний ключ, указывающий на чат, к которому относится сообщение.
    user_id: Внешний ключ, указывающий на пользователя, который отправил сообщение.
    text: Текст сообщения.

    """

    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(Integer, ForeignKey("private_chats.id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    text = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    emotion = Column(String, nullable=True)
    chat = relationship("PrivateChat", back_populates="messages")
    user = relationship("User")
