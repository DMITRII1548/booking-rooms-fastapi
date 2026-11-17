from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.helpers.jwt import AccessTokenPayload, create_access_token
from app.helpers.password import hash_password, verify_password
from app.models.user import User
from app.repositories import revoked_token as revoked_token_repository
from app.repositories import user as user_repository
from app.requests.user import RegisterRequest, LoginRequest


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

def login(db: Session, data: LoginRequest) -> str:
    user = user_repository.get_user_by_email(db, data.email)

    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")

    if not verify_password(data.password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect email or password")

    return create_access_token(user.id)

def logout(db: Session, payload: AccessTokenPayload) -> None:
    revoked_token_repository.revoke(db, payload.jti, payload.expires_at)
    revoked_token_repository.delete_expired(db)
    db.commit()
