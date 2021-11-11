from pydantic import BaseModel
from typing import List, Optional


class Post(BaseModel):
    title: str
    body: str


class PostList(Post):
    class Config:
        orm_mode = True


class User(BaseModel):
    name: str
    email: str
    password: str


class UserList(BaseModel):
    name: str
    email: str

    class Config:
        orm_mode = True


class UserPosts(UserList):
    posts: List[PostList]


class PostsAuthor(Post):
    author: UserList

    class Config:
        orm_mode = True


class Login(BaseModel):
    username: str
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None
