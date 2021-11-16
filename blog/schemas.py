from typing import List

from pydantic import BaseModel

from auth.schemas import UserList


class Post(BaseModel):
	title: str
	body: str


class PostList(Post):
	class Config:
		orm_mode = True


class PostsAuthor(Post):
	author: UserList

	class Config:
		orm_mode = True


class UserPosts(UserList):
	posts: List[PostList]
