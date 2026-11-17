from typing import Generator

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from app.database import SessionLocal
from app.helpers.jwt import AccessTokenPayload, decode_access_token
from app.models.user import User
from app.repositories import revoked_token as revoked_token_repository
from app.repositories import user as user_repository

bearer_scheme = HTTPBearer(auto_error=False)


def get_db() -> Generator[Session, None, None]:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def _unauthorized() -> HTTPException:
    return HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Not authenticated",
        headers={"WWW-Authenticate": "Bearer"},
    )


def get_token_payload(
    credentials: HTTPAuthorizationCredentials | None = Depends(bearer_scheme),
    db: Session = Depends(get_db),
) -> AccessTokenPayload:
    if credentials is None:
        raise _unauthorized()

    payload = decode_access_token(credentials.credentials)
    if payload is None or revoked_token_repository.is_revoked(db, payload.jti):
        raise _unauthorized()

    return payload


def get_current_user(
    payload: AccessTokenPayload = Depends(get_token_payload),
    db: Session = Depends(get_db),
) -> User:
    user = user_repository.get_user_by_id(db, payload.user_id)
    if user is None:
        raise _unauthorized()

    return user
