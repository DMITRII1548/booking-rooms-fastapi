from __future__ import annotations

from typing import TYPE_CHECKING

from pydantic import BaseModel, ConfigDict

if TYPE_CHECKING:
    from app.responses.booking import BookingWithUserResponse


class RoomResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    number: str
    capacity: int

class DetailRoomResponse(RoomResponse):
    bookings: list[BookingWithUserResponse]
