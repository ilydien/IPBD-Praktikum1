from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select
from app.database.session import get_session
from app.database.model.schema import Blog
from app.dto.validator.blog import BlogCreate, BlogUpdate, BlogResponse
from app.core.deps import get_current_user

router = APIRouter(prefix="/blogs", tags=["Blogs"])


@router.post("/", response_model=BlogResponse)
def create_blog(
    data: BlogCreate, db: Session = Depends(get_session), user=Depends(get_current_user)
):
    blog = Blog(judul=data.judul, isi=data.isi, id_creator=user.id)

    db.add(blog)
    db.commit()
    db.refresh(blog)

    return blog


@router.get("/", response_model=list[BlogResponse])
def get_all_blogs(db: Session = Depends(get_session)):
    return db.exec(select(Blog)).all()


@router.put("/{blog_id}", response_model=BlogResponse)
def update_blog(
    blog_id: int,
    data: BlogUpdate,
    db: Session = Depends(get_session),
    user=Depends(get_current_user),
):
    blog = db.get(Blog, blog_id)

    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    if blog.id_creator != user.id:
        raise HTTPException(status_code=403, detail="Not your blog")

    update_data = data.dict(exclude_unset=True)

    for key, value in update_data.items():
        setattr(blog, key, value)

    db.add(blog)
    db.commit()
    db.refresh(blog)

    return blog


@router.delete("/{blog_id}")
def delete_blog(
    blog_id: int, db: Session = Depends(get_session), user=Depends(get_current_user)
):
    blog = db.get(Blog, blog_id)

    if not blog:
        raise HTTPException(status_code=404, detail="Blog not found")

    if blog.id_creator != user.id:
        raise HTTPException(status_code=403, detail="Not your blog")

    db.delete(blog)
    db.commit()

    return {"message": "Blog deleted"}
