from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, DateTime, ForeignKey, Index
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

if TYPE_CHECKING:
    from app.models.room import Room
    from app.models.user import User


class Booking(Base):
    __tablename__ = "bookings"
    __table_args__ = (
        CheckConstraint("end_time > start_time", name="ck_booking_time_order"),
        Index("ix_booking_room_time", "room_id", "start_time", "end_time"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    room_id: Mapped[int] = mapped_column(ForeignKey("rooms.id"), index=True)
    start_time: Mapped[datetime] = mapped_column(DateTime())
    end_time: Mapped[datetime] = mapped_column(DateTime())

    user: Mapped["User"] = relationship(back_populates="bookings")
    room: Mapped["Room"] = relationship(back_populates="bookings")