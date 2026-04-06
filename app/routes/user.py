from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.database.session import get_session
from app.database.model.schema import User

from app.dto.validator.user import UserCreate, UserLogin, UserResponse

from app.core.hash import hash_password, verify_password
from app.core.security import create_access_token
from app.core.deps import get_current_user

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/me", response_model=UserResponse)
def get_me(user: User = Depends(get_current_user)):
    return user


@router.post("/register", response_model=UserResponse)
def register(data: UserCreate, db: Session = Depends(get_session)):

    existing_user = db.exec(select(User).where(User.nim == data.nim)).first()

    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    user = User(
        nama=data.nama, nim=data.nim, password_hashed=hash_password(data.password)
    )

    db.add(user)
    db.commit()
    db.refresh(user)

    return user


@router.post("/login")
def login(data: UserLogin, db: Session = Depends(get_session)):
    user = db.exec(select(User).where(User.nim == data.nim)).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    if not verify_password(data.password, user.password_hashed):
        raise HTTPException(status_code=401, detail="Wrong password")

    token = create_access_token({"sub": str(user.id)})

    return {"access_token": token, "token_type": "bearer"}
