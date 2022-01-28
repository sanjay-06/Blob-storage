import jwt
from typing import List
from fastapi import APIRouter, Depends,File,UploadFile,Form,Request
from fastapi.templating import Jinja2Templates
from models.OAuth2 import oauth
from models.Session import SessionData, cookie
import os,time
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from models.permission import Permission
from models.Basicverifier import verifier
from config.db import permission
from schemas.permission import permissionsEntity

filerouter=APIRouter()
templates=Jinja2Templates(directory="html")

@filerouter.post("/upload_file", dependencies=[Depends(cookie)])
async def handle_form(select: List[str] = Form(...), upload_file:UploadFile = File(...),session_data: SessionData = Depends(verifier)):
    filename=upload_file.filename
    file_location = f"files/{filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(upload_file.file.read())

    payload=jwt.decode(session_data.user_token,oauth.get_jwtsecret(),algorithms=['HS256'])
    email=payload['email']
    select.append(email+"-owner")
    Permission.addpermissions(select,filename)

    return {"info": f"file '{upload_file.filename}' saved at '{file_location}'"}


@filerouter.get("/file/{id}", dependencies=[Depends(cookie)])
async def send_file(id:str):
    file_location = f"files/{id}"
    return FileResponse(file_location, media_type='application/octet-stream', filename=id)

@filerouter.post("/addpermission", dependencies=[Depends(cookie)])
async def handle_form(filename:str=Form(...),select:str = Form(...),read:str = Form(...),edit:str= Form(...),owner:str=Form(...)):

    queryresult=permission.find_one({"username":select})

    if queryresult == None:
        return {"message":"error"}

    queryresult=permissionsEntity(queryresult)

    print(queryresult)

    if read=="yes":
        queryresult["read"].append(filename)
        queryresult["read"]=list(set(queryresult["read"]))


    if edit=="yes":
        queryresult["write"].append(filename)
        queryresult["write"]=list(set(queryresult["write"]))

    if owner=="yes":
        queryresult["owner"].append(filename)
        queryresult["owner"]=list(set(queryresult["owner"]))

    queryresult.pop("id")

    print(queryresult)
    newquery={"$set":queryresult}

    permission.update_one({"username":select},newquery)

    # return {"info": f"file '{upload_file.filename}' saved at '{file_location}'"}

@filerouter.get("/readfile/{file}",response_class=HTMLResponse,dependencies=[Depends(cookie)])
async def read_file(file:str,request : Request,session_data: SessionData = Depends(verifier)):
    payload=jwt.decode(session_data.user_token,oauth.get_jwtsecret(),algorithms=['HS256'])
    path="files/"+file
    f = open(path, "r")
    files=f.read()
    return templates.TemplateResponse("showfile.html",{"request":request,"username":payload['email'],"file":files,"time":time.ctime(os.path.getctime("files/"+file)),"filename":file})

@filerouter.get("/home")
def write():
    return {
        "Name" : "sanjay"
    }
