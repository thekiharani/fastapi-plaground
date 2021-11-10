from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get('/')
def index():
    return {'blogs': 'Blog List'}


@app.get('/blog')
def blog(limit: int = 10, published: bool = True, sort: Optional[str] = None):
    if published:
        return {'blogs': f'{limit} published blogs from DB'}
    return {'blogs': f'{limit} mixed blogs from DB'}


@app.get('/blog/unpublished')
def unpublished():
    return {'blog': 'all unpublished blogs'}


@app.get('/blog/{blog_id}')
def about(blog_id: int):
    return {'blog': blog_id}


@app.get('/blog/{blog_id}/comments')
def comments(blog_id: int, limit: int = 10):
    return {'comments': {'1', '2', limit}}


class Blog(BaseModel):
    title: str
    body: str
    published: Optional[bool]


@app.post('/blog')
def create_blog(blog: Blog):
    return {'created': blog}
