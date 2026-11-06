from fastapi import HTTPException
from datetime import datetime
from app.repositories import booking as booking_repository
from app.repositories import room as room_repository
from app.repositories import user as user_repository
from app.requests.booking import CreateBookingRequest, UpdateBookingRequest


def get_all_bookings() -> list:
    return booking_repository.get_all()

def get_booking_by_id(id: int) -> dict:
    booking = booking_repository.get_booking_with_details_by_id(id)

    if booking is None:
        raise HTTPException(
            404,
            detail="Booking not found"
        )

    return booking

def delete_booking(id: int) -> None:
    booking = booking_repository.get_booking_by_id(id)

    if booking is None:
        raise HTTPException(
            404,
            detail="Booking not found"
        )

    if booking["start_time"] <= datetime.now():
        raise HTTPException(
            400,
            detail="Cannot delete a booking that has already started"
        )

    booking_repository.delete_booking(id)

def create_booking(data: CreateBookingRequest) -> dict[str, Any]:
    if room_repository.get_room_by_id(data.room_id) is None or user_repository.get_user_by_id(data.user_id) is None:
        raise HTTPException(
            404,
            detail="Room or user not found"
        )

    if booking_repository.has_overlap(data.room_id, data.start_time, data.end_time):
        raise HTTPException(
            400,
            detail="Room is overlap on this time"
        )

    return booking_repository.create(
        user_id=data.user_id,
        room_id=data.room_id,
        start_time=data.start_time,
        end_time=data.end_time,
    )

def update_booking(booking_id: int, data: UpdateBookingRequest) -> dict[str, Any]:
    booking = booking_repository.get_booking_by_id(booking_id)
    if booking is None:
        raise HTTPException(
            404,
            detail="Booking not found"
        )

    if booking_repository.has_overlap(booking["room_id"], data.start_time, data.end_time, booking_id):
        raise HTTPException(
            400,
            detail="Room is overlap on this time"
        )

    return booking_repository.update(booking_id=booking_id, start_time=data.start_time, end_time=data.end_time)
