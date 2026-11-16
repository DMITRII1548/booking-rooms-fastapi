from datetime import datetime

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.models.booking import Booking
from app.repositories import booking as booking_repository
from app.repositories import room as room_repository
from app.repositories import user as user_repository
from app.requests.booking import CreateBookingRequest, UpdateBookingRequest


def _get_booking_or_404(db: Session, booking_id: int) -> Booking:
    booking = booking_repository.get_booking_by_id(db, booking_id)
    if booking is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Booking not found")
    return booking


def get_all_bookings(db: Session) -> list[Booking]:
    return booking_repository.get_all(db)


def get_booking_by_id(db: Session, booking_id: int) -> Booking:
    booking = booking_repository.get_booking_with_details_by_id(db, booking_id)
    if booking is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Booking not found")
    return booking


def delete_booking(db: Session, booking_id: int) -> None:
    booking = _get_booking_or_404(db, booking_id)

    if booking.start_time <= datetime.now():
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail="Cannot delete a booking that has already started",
        )

    booking_repository.delete(db, booking)
    db.commit()


def create_booking(db: Session, data: CreateBookingRequest) -> Booking:
    if room_repository.get_room_by_id(db, data.room_id) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Room not found")

    if user_repository.get_user_by_id(db, data.user_id) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="User not found")

    if booking_repository.has_overlap(db, data.room_id, data.start_time, data.end_time):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Room is overlap on this time")

    booking = booking_repository.create(
        db,
        user_id=data.user_id,
        room_id=data.room_id,
        start_time=data.start_time,
        end_time=data.end_time,
    )
    db.commit()
    return booking


def update_booking(db: Session, booking_id: int, data: UpdateBookingRequest) -> Booking:
    booking = _get_booking_or_404(db, booking_id)

    if booking.start_time <= datetime.now():
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail="Cannot update a booking that has already started",
        )

    room_id = data.room_id if data.room_id is not None else booking.room_id
    start_time = data.start_time if data.start_time is not None else booking.start_time
    end_time = data.end_time if data.end_time is not None else booking.end_time

    if start_time >= end_time:
        raise HTTPException(
            status.HTTP_400_BAD_REQUEST,
            detail="start_time must be less than end_time",
        )

    if data.room_id is not None and room_repository.get_room_by_id(db, room_id) is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Room not found")

    if booking_repository.has_overlap(db, room_id, start_time, end_time, booking_id):
        raise HTTPException(status.HTTP_400_BAD_REQUEST, detail="Room is overlap on this time")

    updated_booking = booking_repository.update(
        db,
        booking,
        room_id=room_id,
        start_time=start_time,
        end_time=end_time,
    )
    db.commit()
    return updated_booking
