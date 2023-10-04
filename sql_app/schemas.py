from pydantic import BaseModel
from datetime import datetime


class UserSessionBase(BaseModel):
    id: str
    ip: str
    datetime: datetime
    path: str


class CreateUserSession(UserSessionBase):
    pass


class UserSession(UserSessionBase):
    class Config:
        from_attributes = True
