from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session

from . import schemas, models
from .database import engine, SessionLocal

app = FastAPI()

models.Base.metadata.create_all(engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post('/blog', status_code=status.HTTP_201_CREATED)
def create_post(request: schemas.Blog, db: Session = Depends(get_db)):
    new_post = models.Blog(title=request.title, body=request.body)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@app.get('/blog', status_code=status.HTTP_200_OK)
def get_posts(db: Session = Depends(get_db)):
    posts = db.query(models.Blog).all()
    return posts


@app.get('/blog/{id}', status_code=status.HTTP_200_OK)
def post_details(post_id: int, db: Session = Depends(get_db)):
    post = db.query(models.Blog).filter(models.Blog.id == post_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='post not found')
    return post


@app.put('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_post(post_id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    post = db.query(models.Blog).filter(models.Blog.id == post_id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='post not found')

    post.update({'title': request.title, 'body': request.body}, synchronize_session=False)
    db.commit()
    return {'detail': 'updated'}


@app.delete('/blog/{id}', status_code=status.HTTP_202_ACCEPTED)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    post = db.query(models.Blog).filter(models.Blog.id == post_id)
    if not post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='post not found')

    post.delete(synchronize_session=False)
    db.commit()
    return {'detail': 'deleted'}
