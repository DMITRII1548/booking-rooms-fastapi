from http.client import HTTPResponse

from starlette import status

from app.services import booking as booking_service
from fastapi import APIRouter
from app.requests.booking import CreateBookingRequest, UpdateBookingRequest

router = APIRouter()

@router.get("/")
def get_bookings() -> list:
    return booking_service.get_all_bookings()

@router.get("/{id}")
def get_booking(id: int) -> dict:
    return booking_service.get_booking_by_id(id)

@router.post("/", status_code=status.HTTP_201_CREATED)
def create_booking(data: CreateBookingRequest):
    return booking_service.create_booking(data)

@router.put("/{id}")
def update_booking(data: UpdateBookingRequest, id: int) -> dict:
    return booking_service.update_booking(id, data)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_booking(id: int):
    booking_service.delete_booking(id)

