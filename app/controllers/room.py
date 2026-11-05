
from datetime import date, datetime, timedelta
from typing import Optional

# ---------------------------------------------------------------------------
# Начальные данные
# ---------------------------------------------------------------------------

# Даты считаются от текущего дня, чтобы будущие брони всегда были в будущем,
# а «прошедшая» — всегда в прошлом.
_today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)


def _at(days: int, hour: int, minute: int = 0) -> datetime:
    """Дата через `days` дней от сегодня в указанное время."""
    return _today + timedelta(days=days, hours=hour, minutes=minute)


# Аудитории: ключ — id
rooms: dict[int, dict] = {
    1: {"id": 1, "number": "101", "capacity": 30},
    2: {"id": 2, "number": "205", "capacity": 60},
    3: {"id": 3, "number": "310", "capacity": 120},
    4: {"id": 4, "number": "Акт.зал", "capacity": 300},
}

# Пользователи (преподаватели и сотрудники): ключ — id
users: dict[int, dict] = {
    1: {"id": 1, "name": "Иванов Сергей", "email": "ivanov@univ.uz"},
    2: {"id": 2, "name": "Каримова Дилноза", "email": "karimova@univ.uz"},
    3: {"id": 3, "name": "Петров Алексей", "email": "petrov@univ.uz"},
}

# Бронирования: ключ — id
bookings: dict[int, dict] = {
    1: {"id": 1, "room_id": 1, "user_id": 1,
        "start_time": _at(1, 10), "end_time": _at(1, 11, 30)},   # завтра 10:00–11:30
    2: {"id": 2, "room_id": 2, "user_id": 2,
        "start_time": _at(1, 14), "end_time": _at(1, 15, 30)},   # завтра 14:00–15:30
    3: {"id": 3, "room_id": 1, "user_id": 3,
        "start_time": _at(2, 9), "end_time": _at(2, 10, 30)},    # послезавтра 9:00–10:30
    4: {"id": 4, "room_id": 3, "user_id": 1,
        "start_time": _at(-1, 12), "end_time": _at(-1, 13, 30)}, # ВЧЕРА — для проверки DELETE → 400
}