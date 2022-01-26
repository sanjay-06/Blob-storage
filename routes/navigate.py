
from fastapi import APIRouter,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


navigator=APIRouter()
templates=Jinja2Templates(directory="html")

@navigator.get("/",response_class=HTMLResponse)
def write_home(request : Request):
    return templates.TemplateResponse("index.html",{"request":request})

@navigator.get("/files",response_class=HTMLResponse)
def write_home(request : Request):
    return templates.TemplateResponse("files.html",{"request":request})

@navigator.get("/permission",response_class=HTMLResponse)
def write_home(request : Request):
    return templates.TemplateResponse("permission.html",{"request":request})

@navigator.get("/upload",response_class=HTMLResponse)
def write_home(request : Request):
    return templates.TemplateResponse("upload.html",{"request":request})

@navigator.get("/signup",response_class=HTMLResponse)
def write_home(request : Request):
    return templates.TemplateResponse("signup.html",{"request":request})