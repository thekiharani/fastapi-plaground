from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from auth import models
from auth import token, hashing
from app.database import get_db

router = APIRouter(
    prefix='/auth',
    tags=['Authentication']
)


@router.post('/login')
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='invalid credentials')

    if not hashing.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='invalid credentials')

    # generate jwt
    access_token = token.create_access_token(
        data={"sub": user.email}
    )
    return {"access_token": access_token, "token_type": "bearer"}
