import fastapi
from fastapi import FastAPI, Depends
from fastapi.routing import APIRoute
from fastapi.staticfiles import StaticFiles
from sqlalchemy.orm import Session
from starlette.responses import HTMLResponse, RedirectResponse

from pages.router import router as router_pages
from sql_app import models, database
from sql_app.database import engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="My Website"
)

app.include_router(router_pages)
app.mount('/static', StaticFiles(directory='static'), name='static')


@app.get("/")
async def root(request: fastapi.Request, db: Session = Depends(database.get_db)):
    return RedirectResponse('pages/home')

#
# def custom_route(path, endpoint, methods=None):
#     if methods is None:
#         methods = ["GET"]
#     route = APIRoute(path=path, endpoint=endpoint, methods=methods)
#     app.router.routes.append(route)
#
#
# def read_html_file(file_path):
#     with open(file_path, "r", encoding="utf-8") as file:
#         html_content = file.read()
#     return html_content
#
#
# def home(request: fastapi.Request):
#     homehtml = read_html_file('templates/home.html')
#     return HTMLResponse(content=homehtml)
#
#
# custom_route("/", home)
