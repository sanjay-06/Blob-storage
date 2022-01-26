from fastapi import FastAPI
from routes.user import user
from routes.navigate import navigator
from routes.handlefile import filerouter

app=FastAPI()

app.include_router(user)

app.include_router(navigator)

app.include_router(filerouter)