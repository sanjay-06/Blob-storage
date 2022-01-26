
from fastapi import APIRouter,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


page=APIRouter()
templates=Jinja2Templates(directory="html")

@page.get("/files",response_class=HTMLResponse)
def write_home(request : Request):
    return templates.TemplateResponse("files.html",{"request":request})

@page.get("/permission",response_class=HTMLResponse)
def write_home(request : Request):
    return templates.TemplateResponse("permission.html",{"request":request})

@page.get("/upload",response_class=HTMLResponse)
def write_home(request : Request):
    return templates.TemplateResponse("upload.html",{"request":request})

@page.get("/signup",response_class=HTMLResponse)
def write_home(request : Request):
    return templates.TemplateResponse("signup.html",{"request":request})