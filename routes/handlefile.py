import jwt, os,time,imghdr
from typing import List
from fastapi import APIRouter, Depends,File,UploadFile,Form,Request
from fastapi.templating import Jinja2Templates
from models.OAuth2 import oauth
from models.Session import SessionData, cookie
from fastapi.responses import FileResponse
from fastapi.responses import HTMLResponse
from models.permission import Permission
from models.Basicverifier import verifier
from config.db import permission
from routes.navigate import merge
from schemas.permission import permissionsEntity,replacelist
from pymediainfo import MediaInfo


filerouter=APIRouter()
templates=Jinja2Templates(directory="html")

@filerouter.post("/upload_file", dependencies=[Depends(cookie)])
async def handle_form(select: List[str] = Form(...), upload_file:UploadFile = File(...),session_data: SessionData = Depends(verifier)):
    filename=upload_file.filename
    file_location = f"files/{filename}"
    with open(file_location, "wb+") as file_object:
        file_object.write(upload_file.file.read())

    print(upload_file)
    payload=jwt.decode(session_data.user_token,oauth.get_jwtsecret(),algorithms=['HS256'])
    email=payload['email']
    select[0]=select[0]+","+email+"-owner"
    print(select)
    Permission.addpermissions(select,filename)

    return {"message":"success","statuscode":200}


@filerouter.get("/file/{id}", dependencies=[Depends(cookie)])
async def send_file(id:str):
    file_location = f"files/{id}"
    return FileResponse(file_location, media_type='application/octet-stream', filename=id)

@filerouter.post("/removepermission", dependencies=[Depends(cookie)])
async def send_file(filepermission:str=Form(...)):
    user,file,access=filepermission.split("-")
    queryresult=permission.find_one({"username":user})
    if queryresult == None:
        return {"message":"error" , "statuscode":404}

    queryresult=permissionsEntity(queryresult)

    if access=="edit":
        print(queryresult["write"])
        queryresult["write"].remove(file)
    else:
        print(queryresult[access])
        queryresult[access].remove(file)

    queryresult.pop("id")

    newquery={"$set":queryresult}

    permission.update_one({"username":user},newquery)

    return {"message":"success","statuscode":200}

@filerouter.post("/addpermission", dependencies=[Depends(cookie)])
async def handle_form(filename:str=Form(...),select:str = Form(...),read:str = Form(...),edit:str= Form(...),owner:str=Form(...)):

    queryresult=permission.find_one({"username":select})

    if queryresult == None:
        return {"message":"error"}

    queryresult=permissionsEntity(queryresult)

    print(read)
    print(edit)
    print(owner)

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

    return {"message":"error","statuscode":200}


@filerouter.get("/deletefile/{file}", dependencies=[Depends(cookie)])
async def handle_form(file:str,session_data: SessionData = Depends(verifier)):

    payload=jwt.decode(session_data.user_token,oauth.get_jwtsecret(),algorithms=['HS256'])
    email=payload['email']

    os.remove("files/"+file)

    queryresult=permission.find_one({"username":email})

    if queryresult == None:
        return {"message":"error"}

    queryresult=permissionsEntity(queryresult)

    mergequery=merge(queryresult['owner'],queryresult['write'])


    for filename in mergequery:
        if(filename == file):
            allpermission=permission.find()

            for filepermission in allpermission:

                if file in filepermission['read']:
                    filepermission['read'].remove(file)

                if file in filepermission['write']:
                    filepermission['write'].remove(file)

                if file in filepermission['owner']:
                    filepermission['owner'].remove(file)

                filepermission.pop('_id')

                newquery={"$set":filepermission}

                permission.update_one({"username":filepermission['username']},newquery)

    return {"message":"success","statuscode":200}


@filerouter.get("/readfile/{file}",response_class=HTMLResponse,dependencies=[Depends(cookie)])
async def read_file(file:str,request : Request,session_data: SessionData = Depends(verifier)):
    payload=jwt.decode(session_data.user_token,oauth.get_jwtsecret(),algorithms=['HS256'])
    exe=(os.path.splitext(file)[1])
    print(exe)
    path="files/"+file
    print(imghdr.what(path))
    fileInfo = MediaInfo.parse(path)
    for track in fileInfo.tracks:
        if track.track_type == "Video":
            return templates.TemplateResponse("showimage.html",{"request":request,"video":path})
        if imghdr.what(path) == None:
            f = open(path, "r")
            files=f.read()
            return templates.TemplateResponse("showfile.html",{"request":request,"username":payload['email'],"file":files,"time":time.ctime(os.path.getctime("files/"+file)),"filename":file})

    print(path)
    return templates.TemplateResponse("showimage.html",{"request":request,"image":path})

@filerouter.get("/writefile/{file}",response_class=HTMLResponse,dependencies=[Depends(cookie)])
async def read_file(file:str,request : Request,session_data: SessionData = Depends(verifier)):
    payload=jwt.decode(session_data.user_token,oauth.get_jwtsecret(),algorithms=['HS256'])
    path="files/"+file
    f = open(path, "r")
    files=f.read()
    return templates.TemplateResponse("showwritefile.html",{"request":request,"username":payload['email'],"file":files,"time":time.ctime(os.path.getctime("files/"+file)),"filename":file})

@filerouter.post("/modifyfile/{file}",dependencies=[Depends(cookie)])
async def handle_form(file:str,filetitle:str=Form(...),textarea:str=Form(...)):
    path="files/"+file
    f = open(path, "w")
    f.write(textarea)
    f.close()

    if file != filetitle:
        path1="files/"+filetitle
        os.rename(path,path1)

    allpermission=permission.find()

    for filepermission in allpermission:

        if file in filepermission['read']:
            filepermission['read']=replacelist(file,filetitle,filepermission['read'])

        if file in filepermission['write']:
            filepermission['write']=replacelist(file,filetitle,filepermission['write'])

        if file in filepermission['owner']:
            filepermission['owner']=replacelist(file,filetitle,filepermission['owner'])

        filepermission.pop('_id')

        newquery={"$set":filepermission}

        permission.update_one({"username":filepermission['username']},newquery)

    return {"message":"ok","statuscode":200}
