from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.dependency import get_current_user, get_db, get_token_payload
from app.helpers.jwt import AccessTokenPayload
from app.models import User
from app.requests.user import RegisterRequest, LoginRequest
from app.responses.user import UserResponse, TokenResponse
from app.services import user as user_service

router = APIRouter()

@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def register_user(data: RegisterRequest, db: Session = Depends(get_db)):
    return user_service.create_user(db, data)

@router.post("/login", response_model=TokenResponse)
def login(data: LoginRequest, db: Session = Depends(get_db)):
    return TokenResponse(access_token=user_service.login(db, data))

@router.get("/me", response_model=UserResponse)
def me(current_user: User = Depends(get_current_user)):
    return current_user

@router.post("/logout", status_code=status.HTTP_204_NO_CONTENT)
def logout(
    payload: AccessTokenPayload = Depends(get_token_payload),
    db: Session = Depends(get_db),
):
    user_service.logout(db, payload)
