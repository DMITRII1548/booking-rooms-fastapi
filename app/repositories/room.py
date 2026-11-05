from typing import Any
from app import database

def get_room_by_id(room_id: int) -> dict[str, Any] | None:
    return database.rooms.get(room_id)