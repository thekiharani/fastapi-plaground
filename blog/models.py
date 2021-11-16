from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base


class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    body = Column(String)
    author_id = Column(Integer, ForeignKey('users.id', onupdate='CASCADE', ondelete='CASCADE'))

    author = relationship('User', back_populates='posts')
