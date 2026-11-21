from datetime import datetime
from pydantic import BaseModel, ConfigDict
from app.responses.user import UserResponse
from app.responses.room import RoomResponse

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

class BookingWithUserResponse(BookingResponse):
    user: UserResponse

class UserWithBookingsResponse(UserResponse):
    bookings: list[BookingWithRoomResponse]
