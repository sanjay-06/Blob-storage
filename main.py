from fastapi import FastAPI,Request,File,UploadFile,Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from routes.user import user
from routes.page import page

app=FastAPI()

app.include_router(user)

app.include_router(page)

templates=Jinja2Templates(directory="html")

@app.get("/",response_class=HTMLResponse)
def write_home(request : Request):
    return templates.TemplateResponse("index.html",{"request":request})


@app.post("/submitform")
async def handle_form(title:str= Form(...), upload_file:UploadFile = File(...)):
    print(title)
    content_assignment= await upload_file.read(1)
    print(upload_file.filename)
    print(content_assignment)


@app.get("/home")
def write():
    return {
        "Name" : "sanjay"
    }