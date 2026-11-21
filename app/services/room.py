from fastapi import HTTPException
from sqlalchemy.orm import Session
from app.models import Room
from app.repositories import room as room_repository

def get_rooms(db: Session) -> list[Room]:
    return room_repository.get_rooms(db)

def get_room_by_id(db: Session, room_id: int) -> Room:
    room = room_repository.get_room_by_id(db, room_id)

    if room is None:
        raise HTTPException(status_code=404, detail="Room not found")

    return room