from datetime import datetime
from typing import Any

from app import database


def get_all() -> list[dict[str, Any]]:
    return list(database.bookings.values())


def get_booking_by_id(booking_id: int) -> dict[str, Any] | None:
    return database.bookings.get(booking_id)


def get_booking_with_details_by_id(booking_id: int) -> dict[str, Any] | None:
    booking = get_booking_by_id(booking_id)

    if booking is None:
        return None

    room = database.rooms.get(booking["room_id"])
    user = database.users.get(booking["user_id"])

    return {
        **booking,
        "room": {"id": room["id"], "number": room["number"]} if room else None,
        "user": {"id": user["id"], "name": user["name"]} if user else None,
    }


def delete_booking(booking_id: int) -> None:
    database.bookings.pop(booking_id, None)

def create(user_id: int, room_id: int, start_time: datetime, end_time: datetime) -> dict[str, Any]:
    booking_id = database.next_booking_id

    booking = {
        "id": booking_id,
        "room_id": room_id,
        "user_id": user_id,
        "start_time": start_time,
        "end_time": end_time,
    }

    database.bookings[booking_id] = booking
    database.next_booking_id += 1
    return booking

def update(
        booking_id: int,
        room_id: int,
        start_time: datetime,
        end_time: datetime
) -> dict[str, Any] | None:
    booking = database.bookings.get(booking_id)

    if booking is None:
        return None

    booking["room_id"] = room_id
    booking["start_time"] = start_time
    booking["end_time"] = end_time
    return booking

def has_overlap(
        room_id: int,
        start_time: datetime,
        end_time: datetime,
        exclude_booking_id: int | None = None
) -> bool:
    for b in database.bookings.values():
        if b["room_id"] == room_id and b["id"] != exclude_booking_id \
                and start_time < b["end_time"] and end_time > b["start_time"]:
            return True
    return False