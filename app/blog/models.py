from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String)
    author_id = Column(Integer, ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'))

    author = relationship('User', back_populates='posts')


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True)
    password = Column(String)

    posts = relationship('Post', back_populates='author')
