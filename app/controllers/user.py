from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.dependency import get_db
from app.requests.user import RegisterRequest
from app.responses.user import UserResponse
from app.services import user as user_service

router = APIRouter()


@router.post("/register", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def register_user(data: RegisterRequest, db: Session = Depends(get_db)):
    return user_service.create_user(db, data)
