from sqlalchemy.orm import Session

from app.models.room import Room


def get_room_by_id(db: Session, room_id: int) -> Room | None:
    return db.get(Room, room_id)
