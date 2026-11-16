from datetime import datetime

from pydantic import BaseModel, ConfigDict


class RoomResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    number: str
    capacity: int


class UserResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    email: str


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
