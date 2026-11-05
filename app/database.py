"""
Мини-БД в памяти для системы бронирования аудиторий (ЛР2).
Только данные: три «таблицы» из ЛР1 и счётчик id для новых бронирований.
"""

from datetime import datetime, timedelta

# Даты считаются от сегодняшнего дня: будущие брони всегда в будущем,
# бронь №4 всегда вчерашняя (для проверки DELETE прошедшей брони → 400).
today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)

rooms = {
    1: {"id": 1, "number": "101", "capacity": 30},
    2: {"id": 2, "number": "205", "capacity": 60},
    3: {"id": 3, "number": "310", "capacity": 120},
    4: {"id": 4, "number": "Акт.зал", "capacity": 300},
}

users = {
    1: {"id": 1, "name": "Иванов Сергей", "email": "ivanov@univ.uz"},
    2: {"id": 2, "name": "Каримова Дилноза", "email": "karimova@univ.uz"},
    3: {"id": 3, "name": "Петров Алексей", "email": "petrov@univ.uz"},
}

bookings = {
    1: {"id": 1, "room_id": 1, "user_id": 1,
        "start_time": today + timedelta(days=1, hours=10),
        "end_time": today + timedelta(days=1, hours=11, minutes=30)},
    2: {"id": 2, "room_id": 2, "user_id": 2,
        "start_time": today + timedelta(days=1, hours=14),
        "end_time": today + timedelta(days=1, hours=15, minutes=30)},
    3: {"id": 3, "room_id": 1, "user_id": 3,
        "start_time": today + timedelta(days=2, hours=9),
        "end_time": today + timedelta(days=2, hours=10, minutes=30)},
    4: {"id": 4, "room_id": 3, "user_id": 1,
        "start_time": today + timedelta(days=-1, hours=12),
        "end_time": today + timedelta(days=-1, hours=13, minutes=30)},
}

# Следующий id для новой брони (как autoincrement, после удаления не переиспользуется)
next_booking_id = 5