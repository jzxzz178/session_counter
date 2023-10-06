from sqlalchemy import func
from sqlalchemy.orm import Session

from . import models, schemas


async def get_session_count(db: Session):
    query = (db.query(models.VisitingSession.path,
                      func.count(models.VisitingSession.path))
             .group_by(models.VisitingSession.path))
    return query


async def create_user_session(db: Session, user_session: schemas.CreateUserSession):
    db_session = models.VisitingSession(**user_session.dict())
    db.add(db_session)
    db.commit()
    db.refresh(db_session)
    return db_session
