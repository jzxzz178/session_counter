from datetime import datetime
from uuid import uuid1

import fastapi
from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

# from sql_app import database

# from session_counter import session_counter
from sql_app import crud, models, schemas, database

router = APIRouter(
    prefix='/pages',
    tags=['Pages']
)

templates = Jinja2Templates(directory='templates')


def update_db(request: Request,
              db: Session):
    user_session = schemas.CreateUserSession(
        id=str(uuid1()),
        ip=request.client.host,
        datetime=datetime.now(),
        path=request.url.path
    )

    crud.create_user_session(
        db,
        user_session
    )


@router.get('/base')
# @session_counter
def get_base_template(request: Request,
                      db: Session = Depends(database.get_db)):
    return templates.TemplateResponse('base.html', {'request': request})


@router.get('/search')
# @session_counter
def get_search_template(request: Request, db: Session = Depends(database.get_db)):
    return templates.TemplateResponse('search.html', {'request': request})


@router.get('/home')
# @session_counter
def get_home_page(request: Request, db: Session = Depends(database.get_db)):
    update_db(request, db)
    return templates.TemplateResponse('home.html', {'request': request})


@router.get('/sessions')
def get_session_count(request: Request, db: Session = Depends(database.get_db)):
    return crud.get_session_count(db)
