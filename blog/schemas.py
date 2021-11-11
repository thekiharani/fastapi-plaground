from pydantic import BaseModel
from typing import List


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
