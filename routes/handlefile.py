from fastapi import APIRouter,File,UploadFile,Form
from fastapi.templating import Jinja2Templates


filerouter=APIRouter()
templates=Jinja2Templates(directory="html")

@filerouter.post("/submitform")
async def handle_form(title:str= Form(...), upload_file:UploadFile = File(...)):
    print(title)
    content_assignment= await upload_file.read(1)
    print(upload_file.filename)
    print(content_assignment)


@filerouter.get("/home")
def write():
    return {
        "Name" : "sanjay"
    }
