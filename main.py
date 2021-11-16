from fastapi import FastAPI

from blog import models
from app.database import engine
from blog.routers import posts
from auth.routes import auth, users

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(auth.router)
app.include_router(users.router)
app.include_router(posts.router)
