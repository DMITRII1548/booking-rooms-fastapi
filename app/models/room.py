from typing import TYPE_CHECKING

from sqlalchemy import CheckConstraint, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

if TYPE_CHECKING:
    from app.models.booking import Booking


class Room(Base):
    __tablename__ = "rooms"
    __table_args__ = (
        UniqueConstraint("number", name="uq_room_number"),
        CheckConstraint("capacity > 0", name="ck_room_capacity_positive"),
    )

    id: Mapped[int] = mapped_column(primary_key=True)
    number: Mapped[str] = mapped_column(String(20))
    capacity: Mapped[int]

    bookings: Mapped[list["Booking"]] = relationship(back_populates="room")