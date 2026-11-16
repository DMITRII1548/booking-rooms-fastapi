from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.helpers.password import hash_password
from app.models.user import User
from app.repositories import user as user_repository
from app.requests.user import RegisterRequest


def create_user(db: Session, data: RegisterRequest) -> User:
    if user_repository.is_user_exists_by_email(db, data.email):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Email already registered")

    user = user_repository.create_user(
        db,
        name=data.name,
        email=data.email,
        password=hash_password(data.password),
    )
    db.commit()

    return user
