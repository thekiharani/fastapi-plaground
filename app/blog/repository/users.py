from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from .. import models, schemas, hashing


def index(db: Session):
    users = db.query(models.User).all()
    return users


def store(request: schemas.User, db: Session):
    new_user = models.User(name=request.name, email=request.email, password=hashing.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def show(user_id: int, db: Session):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='user not found')
    return user


def find_by_email(email: str, db: Session):
    user = db.query(models.User).filter(models.User.email == email).first()
    return user
