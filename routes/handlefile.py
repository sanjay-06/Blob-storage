from fastapi import APIRouter,File,UploadFile,Form
from fastapi.templating import Jinja2Templates

from fastapi.responses import FileResponse

filerouter=APIRouter()
templates=Jinja2Templates(directory="html")

@filerouter.post("/submitform")
async def handle_form(title:str= Form(...), upload_file:UploadFile = File(...)):
    file_location = f"files/{upload_file.filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(upload_file.file.read())
    return {"info": f"file '{upload_file.filename}' saved at '{file_location}'"}


@filerouter.get("/file/{id}")
async def send_file(id:str):
    file_location = f"files/{id}"
    return FileResponse(file_location, media_type='application/octet-stream', filename=id)

@filerouter.get("/home")
def write():
    return {
        "Name" : "sanjay"
    }
