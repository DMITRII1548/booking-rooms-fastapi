from sqlalchemy.orm import Session

from app.models.user import User


def get_user_by_id(db: Session, user_id: int) -> User | None:
    return db.get(User, user_id)

def is_user_exists_by_email(db: Session, email: str) -> bool:
    return db.query(User).filter(User.email == email).first() is not None

def create_user(db: Session, name: str, email: str, password: str) -> User:
    user = User(name=name, email=email, password=password)
    db.add(user)
    db.flush()
    db.refresh(user)

    return user