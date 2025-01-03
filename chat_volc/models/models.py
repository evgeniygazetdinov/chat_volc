from sqlalchemy import (
    Column,
    String,
    Integer,
    ForeignKey,
    DateTime,
    Boolean,
    UniqueConstraint, func,
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
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    emotion = Column(String, nullable=True)
    chat = relationship("PrivateChat", back_populates="messages")
    user = relationship("User")

    @staticmethod
    def create_message(db, private_chat_id, data):
        user_id, text =  data.user_id, data.text
        current_chat =  db.query(PrivateChat).filter(PrivateChat.id == private_chat_id)
        current_user = db.query(User).filter(User.id == user_id)
        chat_exists = db.query(current_chat.exists()).scalar()
        user_exists = db.query(
            current_user.exists()
        ).scalar()
        if not chat_exists or not user_exists:
            raise Exception("chat or user id not exists")
        private_chat = current_chat.first()
        chat_users = [private_chat.user_one_id, private_chat.user_two_id]
        if user_id not in chat_users:
            raise Exception("chat or user id not exists")
        new_message = Message(chat_id=private_chat_id, user_id=user_id, text=text)
        db.add(new_message)
        db.commit()
        return new_message

