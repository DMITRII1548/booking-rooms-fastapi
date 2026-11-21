from datetime import datetime

from pydantic import BaseModel, ConfigDict

from app.responses.user import UserResponse


class RoomResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    number: str
    capacity: int


class BookingResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    user_id: int
    room_id: int
    start_time: datetime
    end_time: datetime


class BookingDetailResponse(BookingResponse):
    room: RoomResponse
    user: UserResponse


class BookingWithRoomResponse(BookingResponse):
    room: RoomResponse


class UserWithBookingsResponse(UserResponse):
    bookings: list[BookingWithRoomResponse]
