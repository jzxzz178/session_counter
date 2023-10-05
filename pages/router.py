from datetime import datetime
from uuid import uuid1

from fastapi import APIRouter, Request, Depends
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from sql_app import crud, schemas, database

router = APIRouter(
    prefix='/pages',
    tags=['Pages']
)

templates = Jinja2Templates(directory='templates')


async def update_db(request: Request,
                    db: Session):
    user_session = schemas.CreateUserSession(
        id=str(uuid1()),
        ip=request.client.host,
        datetime=datetime.now(),
        path=request.url.path
    )
    await crud.create_user_session(
        db,
        user_session
    )


@router.get('/home')
async def get_home_page(request: Request, db: Session = Depends(database.get_db)):
    await update_db(request, db)
    return templates.TemplateResponse('home.html', {'request': request})


# @router.get('/base')
# async def get_base_template(request: Request,
#                             db: Session = Depends(database.get_db)):
#     return templates.TemplateResponse('base.html', {'request': request})


@router.get('/aboutFastapi')
async def get_search_template(request: Request, db: Session = Depends(database.get_db)):
    await update_db(request, db)
    return templates.TemplateResponse('aboutFastapi.html', {'request': request})


@router.get('/sessions')
async def get_session_count(request: Request, db: Session = Depends(database.get_db)):
    return await crud.get_session_count(db)
