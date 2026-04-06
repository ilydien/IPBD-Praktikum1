from typing import Optional, List
from sqlmodel import Relationship, SQLModel, Field
from datetime import datetime
from sqlalchemy import func


class Blog(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=False)
    judul: str = Field(max_length=100)
    isi: str
    id_creator: int = Field(foreign_key="user.id", nullable=False)

    user: Optional["User"] = Relationship(back_populates="blog")


class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True, nullable=True)
    nama: str = Field(max_length=255)
    nim: str = Field(max_length=10)
    password_hashed: str
    created_at: datetime = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"server_default": func.now()}
    )

    blog: List["Blog"] = Relationship(back_populates="user")
