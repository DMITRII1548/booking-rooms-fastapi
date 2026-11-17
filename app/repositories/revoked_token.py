from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.revoked_token import RevokedToken


def revoke(db: Session, jti: str, expires_at: datetime) -> None:
    db.merge(RevokedToken(jti=jti, expires_at=expires_at))


def is_revoked(db: Session, jti: str) -> bool:
    return db.get(RevokedToken, jti) is not None


def delete_expired(db: Session) -> None:
    db.query(RevokedToken).filter(
        RevokedToken.expires_at < datetime.now(timezone.utc)
    ).delete()
