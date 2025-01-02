from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
import uuid

Base = declarative_base()

class User(Base):
    __tablename__ = 'users' 

    id = Column(Integer, primary_key=True, index=True) 
    uid = Column(String, unique=True, default=str(uuid.uuid4()))  
    username = Column(String, index=True)

    def __repr__(self):
        return f"<User(uid='{self.uid}', username='{self.username}')>"


