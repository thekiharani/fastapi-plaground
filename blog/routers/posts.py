from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from blog import schemas
from auth.schemas import User
from app.database import get_db
from auth.oauth2 import get_current_user
from blog.repository import posts as post_repository

router = APIRouter(
	prefix='/posts',
	tags=['Posts']
)


@router.get('/', response_model=List[schemas.PostsAuthor])
def get_posts(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
	return post_repository.index(db)


@router.post('/', status_code=status.HTTP_201_CREATED)
def create_post(request: schemas.Post, db: Session = Depends(get_db)):
	return post_repository.store(request, db)


@router.get('/{id}', response_model=schemas.PostsAuthor)
def post_details(post_id: int, db: Session = Depends(get_db)):
	return post_repository.show(post_id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update_post(post_id: int, request: schemas.Post, db: Session = Depends(get_db)):
	return post_repository.update(post_id, request, db)


@router.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
def delete_post(post_id: int, db: Session = Depends(get_db)):
	return post_repository.destroy(post_id, db)
