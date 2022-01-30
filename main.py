from fastapi import FastAPI
from routes.user import user
from routes.navigate import navigator
from routes.handlefile import filerouter
from fastapi.staticfiles import StaticFiles

app=FastAPI()

app.mount("/static", StaticFiles(directory="html/static"), name="static")
app.mount("/handlestatic", StaticFiles(directory="files"), name="handlestatic")

app.include_router(user)

app.include_router(navigator)

app.include_router(filerouter)