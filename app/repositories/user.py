from typing import Any
from app import database

def get_user_by_id(user_id: int) -> dict[str, Any] | None:
    return database.users.get(user_id)