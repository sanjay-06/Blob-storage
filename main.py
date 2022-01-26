from distutils.command.upload import upload
from fastapi import FastAPI,Body, Request,File,UploadFile,Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer,OAuth2PasswordRequestForm

app=FastAPI()

templates=Jinja2Templates(directory="html")

oauth_scheme= OAuth2PasswordBearer(tokenUrl="token")

# @app.get("/token")
# aync def

@app.get("/",response_class=HTMLResponse)
def write_home(request : Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/submitform")
async def handle_form(title:str= Form(...), upload_file:UploadFile = File(...)):
    print(title)
    content_assignment= await upload_file.read(1)
    print(upload_file.filename)
    print(content_assignment)

@app.get("/files",response_class=HTMLResponse)
def write_home(request : Request):
    return templates.TemplateResponse("files.html",{"request":request})

@app.get("/permission",response_class=HTMLResponse)
def write_home(request : Request):
    return templates.TemplateResponse("permission.html",{"request":request})

@app.get("/upload",response_class=HTMLResponse)
def write_home(request : Request):
    return templates.TemplateResponse("upload.html",{"request":request})

@app.get("/signup",response_class=HTMLResponse)
def write_home(request : Request):
    return templates.TemplateResponse("signup.html",{"request":request})

@app.get("/home")
def write():
    return {
        "Name" : "sanjay"
    }