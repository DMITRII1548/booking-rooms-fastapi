from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.dependency import get_db
from app.requests.booking import CreateBookingRequest, UpdateBookingRequest
from app.responses.booking import BookingDetailResponse, BookingResponse
from app.services import booking as booking_service

router = APIRouter()


@router.get("/", response_model=list[BookingResponse])
def get_bookings(db: Session = Depends(get_db)):
    return booking_service.get_all_bookings(db)


@router.get("/{id}", response_model=BookingDetailResponse)
def get_booking(id: int, db: Session = Depends(get_db)):
    return booking_service.get_booking_by_id(db, id)


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=BookingResponse)
def create_booking(data: CreateBookingRequest, db: Session = Depends(get_db)):
    return booking_service.create_booking(db, data)


@router.patch("/{id}", response_model=BookingResponse)
def update_booking(id: int, data: UpdateBookingRequest, db: Session = Depends(get_db)):
    return booking_service.update_booking(db, id, data)


@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_booking(id: int, db: Session = Depends(get_db)):
    booking_service.delete_booking(db, id)
