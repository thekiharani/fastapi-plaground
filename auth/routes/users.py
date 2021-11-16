from typing import List

from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from auth import schemas
from blog.schemas import UserPosts
from app.database import get_db
from auth.oauth2 import get_current_user
from auth.repository import users as user_repository

router = APIRouter(
    prefix='/users',
    tags=['Users']
)


@router.get('/', response_model=List[schemas.UserList])
def get_users(db: Session = Depends(get_db)):
    return user_repository.index(db)


@router.get('/profile', response_model=UserPosts)
def my_profile(db: Session = Depends(get_db), current_user: schemas.User = Depends(get_current_user)):
    return user_repository.find_by_email(current_user.email, db)


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.UserList)
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return user_repository.store(request, db)


@router.get('/{id}', response_model=UserPosts)
def user_details(user_id: int, db: Session = Depends(get_db)):
    return user_repository.show(user_id, db)
