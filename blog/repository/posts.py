from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from blog import models, schemas


def index(db: Session):
    posts = db.query(models.Post).all()
    return posts


def store(request: schemas.Post, db: Session):
    new_post = models.Post(title=request.title, body=request.body, author_id=1)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def show(post_id: int, db: Session):
    post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='post not found')
    return post


def update(post_id: int, request: schemas.Post, db: Session):
    post = db.query(models.Post).filter(models.Post.id == post_id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='post not found')

    post.update({'title': request.title, 'body': request.body}, synchronize_session=False)
    db.commit()
    return {'detail': 'updated'}


def destroy(post_id: int, db: Session):
    post = db.query(models.Post).filter(models.Post.id == post_id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='post not found')

    post.delete(synchronize_session=False)
    db.commit()
    return {'detail': 'deleted'}
