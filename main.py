from datetime import datetime
from uuid import uuid1

import fastapi
import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import ValidationError

from pages.router import router as router_pages
from fastapi.staticfiles import StaticFiles

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from sql_app import crud, models, schemas, database
from sql_app.database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="My Website"
)

app.include_router(router_pages)
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get("/")
# @session_counter
async def root(request: fastapi.Request, db: Session = Depends(database.get_db)):
    return RedirectResponse('pages/home')
