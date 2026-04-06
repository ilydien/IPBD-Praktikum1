from pydantic import BaseModel
from datetime import datetime


class UserRegister(BaseModel):
    nama: str
    nim: str
    password_hashed: str


class UserCreate(BaseModel):
    nama: str
    nim: str
    password: str


class UserLogin(BaseModel):
    nim: str
    password: str


class UserResponse(BaseModel):
    id: int
    nama: str
    nim: str
    created_at: datetime


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

    class Config:
        from_atribute = True
