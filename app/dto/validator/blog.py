from typing import Optional
from pydantic import BaseModel


class BlogBase(BaseModel):
    judul: str
    isi: str


class BlogResponse(BaseModel):
    id: int
    judul: str
    isi: str
    id_creator: int


class BlogCreate(BaseModel):
    judul: str
    isi: str


class BlogUpdate(BaseModel):
    judul: Optional[str]
    isi: Optional[str]

    class Config:
        from_atribute = True
