from datetime import datetime, timedelta

from sqlalchemy.orm import Session

from app.models import Booking, Room, User


def seed(db: Session) -> None:
    pass
    # if db.query(Room).first() is not None:
    #     return
    #
    # today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    #
    # room_101 = Room(number="101", capacity=30)
    # room_205 = Room(number="205", capacity=60)
    # room_310 = Room(number="310", capacity=120)
    # hall = Room(number="Акт.зал", capacity=300)
    #
    # ivanov = User(name="Иванов Сергей", email="ivanov@univ.uz")
    # karimova = User(name="Каримова Дилноза", email="karimova@univ.uz")
    # petrov = User(name="Петров Алексей", email="petrov@univ.uz")
    #
    # db.add_all([room_101, room_205, room_310, hall, ivanov, karimova, petrov])
    # db.add_all([
    #     Booking(room=room_101, user=ivanov,
    #             start_time=today + timedelta(days=1, hours=10),
    #             end_time=today + timedelta(days=1, hours=11, minutes=30)),
    #     Booking(room=room_205, user=karimova,
    #             start_time=today + timedelta(days=1, hours=14),
    #             end_time=today + timedelta(days=1, hours=15, minutes=30)),
    #     Booking(room=room_101, user=petrov,
    #             start_time=today + timedelta(days=2, hours=9),
    #             end_time=today + timedelta(days=2, hours=10, minutes=30)),
    #     Booking(room=room_310, user=ivanov,
    #             start_time=today + timedelta(days=-1, hours=12),
    #             end_time=today + timedelta(days=-1, hours=13, minutes=30)),
    # ])
    # db.commit()
