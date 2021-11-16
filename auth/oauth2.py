from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer

from auth import token as token_helper

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="invalid credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    return token_helper.verify_token(token, credentials_exception)
