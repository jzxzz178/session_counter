from sqlalchemy import Column, String, DATETIME

from .database import Base


class VisitingSession(Base):
    # noinspection SpellCheckingInspection
    __tablename__ = "sessions"

    id = Column(String, primary_key=True, index=True)
    ip = Column(String)
    datetime = Column(DATETIME)
    path = Column(String)
