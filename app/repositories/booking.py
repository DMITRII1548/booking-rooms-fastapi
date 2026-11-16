from datetime import datetime

from sqlalchemy.orm import Session, joinedload

from app.models.booking import Booking


def get_all(db: Session) -> list[Booking]:
    return db.query(Booking).order_by(Booking.start_time).all()


def get_booking_by_id(db: Session, booking_id: int) -> Booking | None:
    return db.get(Booking, booking_id)


def get_booking_with_details_by_id(db: Session, booking_id: int) -> Booking | None:
    return (
        db.query(Booking)
        .options(joinedload(Booking.room), joinedload(Booking.user))
        .filter(Booking.id == booking_id)
        .first()
    )


def delete(db: Session, booking: Booking) -> None:
    db.delete(booking)
    db.flush()


def create(db: Session, user_id: int, room_id: int, start_time: datetime, end_time: datetime) -> Booking:
    booking = Booking(user_id=user_id, room_id=room_id, start_time=start_time, end_time=end_time)
    db.add(booking)
    db.flush()
    db.refresh(booking)
    return booking


def update(
        db: Session,
        booking: Booking,
        room_id: int | None = None,
        start_time: datetime | None = None,
        end_time: datetime | None = None,
) -> Booking:
    if room_id is not None:
        booking.room_id = room_id
    if start_time is not None:
        booking.start_time = start_time
    if end_time is not None:
        booking.end_time = end_time

    db.flush()
    db.refresh(booking)
    return booking


def has_overlap(
        db: Session,
        room_id: int,
        start_time: datetime,
        end_time: datetime,
        exclude_booking_id: int | None = None,
) -> bool:
    query = db.query(Booking).filter(
        Booking.room_id == room_id,
        Booking.start_time < end_time,
        Booking.end_time > start_time,
    )

    if exclude_booking_id is not None:
        query = query.filter(Booking.id != exclude_booking_id)

    return db.query(query.exists()).scalar()
