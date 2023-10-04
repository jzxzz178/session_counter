from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from sql_app import database
from sql_app.database import SessionLocal, engine

from session_counter import session_counter

router = APIRouter(
    prefix='/pages',
    tags=['Pages']
)

templates = Jinja2Templates(directory='templates')


@router.get('/base')
@session_counter
def get_base_template(request: Request, db: Session = Depends(database.get_db)):
    return templates.TemplateResponse('base.html', {'request': request})


@router.get('/search')
@session_counter
def get_search_template(request: Request, db: Session = Depends(database.get_db)):
    return templates.TemplateResponse('search.html', {'request': request})


@router.get('/home')
@session_counter
def get_home_page(request: Request, db: Session = Depends(database.get_db)):
    return templates.TemplateResponse('home.html', {'request': request})
