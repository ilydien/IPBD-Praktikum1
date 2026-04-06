from fastapi import FastAPI
from app.routes import blog, user

app = FastAPI()

app.include_router(blog.router, prefix="/api")
app.include_router(user.router, prefix="/api")
