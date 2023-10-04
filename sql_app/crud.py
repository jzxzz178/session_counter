from sqlalchemy.orm import Session
from datetime import datetime

from . import models, schemas


def get_session_count(db: Session):
    query = db.query(models.VisitingSession).count()
    return query


def create_user_session(db: Session, user_session: schemas.CreateUserSession):
    db_session = models.VisitingSession(**user_session.dict())
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session
