from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.dependency import get_db
from app.responses.room import RoomResponse, DetailRoomResponse
from app.services import room as room_service
router = APIRouter()

@router.get("/", response_model=list[RoomResponse])
def get_rooms(db: Session = Depends(get_db)):
    return room_service.get_rooms(db)

@router.get("/{id}", response_model=DetailRoomResponse)
def get_room(id: int, db: Session = Depends(get_db)):
    return room_service.get_room_by_id(db, id)