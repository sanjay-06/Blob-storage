from fastapi import FastAPI
from routes.user import user
from routes.navigate import navigator
from routes.handlefile import filerouter
from fastapi.staticfiles import StaticFiles
import uvicorn

app=FastAPI()

app.mount("/static", StaticFiles(directory="html/static"), name="static")

app.include_router(user)

app.include_router(navigator)

app.include_router(filerouter)

uvicorn.run(app,host='0.0.0.0',port=8000)
