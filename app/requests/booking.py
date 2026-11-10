from datetime import datetime

from pydantic import BaseModel, Field, field_validator, model_validator


class CreateBookingRequest(BaseModel):
    room_id: int = Field(gt=0)
    user_id: int = Field(gt=0)
    start_time: datetime
    end_time: datetime

    @field_validator("start_time", "end_time")
    @classmethod
    def must_be_in_future(cls, value: datetime) -> datetime:
        if value.tzinfo is not None:
            value = value.astimezone().replace(tzinfo=None)

        if value <= datetime.now():
            raise ValueError("Date must be in the future")
        return value

    @model_validator(mode="after")
    def start_before_end(self) -> "CreateBookingRequest":
        if self.start_time >= self.end_time:
            raise ValueError("start_time must be less than end_time")
        return self


class UpdateBookingRequest(BaseModel):
    room_id: int | None = Field(default=None, gt=0)
    start_time: datetime | None = None
    end_time: datetime | None = None

    @field_validator("start_time", "end_time")
    @classmethod
    def must_be_in_future(cls, value: datetime | None) -> datetime | None:
        if value is None:
            return value

        if value.tzinfo is not None:
            value = value.astimezone().replace(tzinfo=None)

        if value <= datetime.now():
            raise ValueError("Date must be in the future")
        return value

    @model_validator(mode="after")
    def validate_fields(self) -> "UpdateBookingRequest":
        if self.room_id is None and self.start_time is None and self.end_time is None:
            raise ValueError("At least one field must be provided")

        if self.start_time is not None and self.end_time is not None                 and self.start_time >= self.end_time:
            raise ValueError("start_time must be less than end_time")
        return self
