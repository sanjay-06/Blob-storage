import jwt, os,time,gzip,shutil
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
import mimetypes



filerouter=APIRouter()
templates=Jinja2Templates(directory="html")

@filerouter.post("/upload_file", dependencies=[Depends(cookie)])
async def handle_form(select: List[str] = Form(...), upload_file:UploadFile = File(...),session_data: SessionData = Depends(verifier)):
    filename=upload_file.filename
    file_location = f"files/{filename}"
    with gzip.open(file_location, "wb+") as file_object:
        content=upload_file.file.read()
        file_object.write(content)

    print(upload_file)
    payload=jwt.decode(session_data.user_token,oauth.get_jwtsecret(),algorithms=['HS256'])
    email=payload['email']
    if select[0]=='None':
        select.pop(0)
        select.append(email+"-owner")
    select[0]=select[0]+","+email+"-owner"
    print(select)
    Permission.addpermissions(select,filename)

    return {"message":"success","statuscode":200}


@filerouter.get("/file/{id}", dependencies=[Depends(cookie)])
async def send_file(id:str):
    file_location = f"files/{id}"
    return FileResponse(file_location, media_type='application/octet-stream', filename=id)

@filerouter.get("/file/extract/{id}", dependencies=[Depends(cookie)])
async def send_file(id:str):
    path=f"files/{id}"
    file_location = f"files/extract/{id}"
    with gzip.open(path, 'rb') as f_in:
        with open(file_location, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)
            return FileResponse(file_location, media_type='application/octet-stream', filename=id)


@filerouter.post("/removepermission", dependencies=[Depends(cookie)])
async def send_file(filepermission:str=Form(...)):
    user,file,access=filepermission.split("-")
    queryresult=permission.find_one({"username":user})
    if queryresult == None:
        return {"message":"error" , "statuscode":404}

    queryresult=permissionsEntity(queryresult)

    if access=="read":
        queryresult["read"].remove(file)


    if access=="edit":
        queryresult["read"].remove(file)
        queryresult["write"].remove(file)

    if access=="owner":
        queryresult["read"].remove(file)
        queryresult["write"].remove(file)
        queryresult["owner"].remove(file)

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
        queryresult["read"].append(filename)
        queryresult["write"].append(filename)
        queryresult["read"]=list(set(queryresult["read"]))
        queryresult["write"]=list(set(queryresult["write"]))

    if owner=="yes":
        queryresult["read"].append(filename)
        queryresult["write"].append(filename)
        queryresult["read"]=list(set(queryresult["read"]))
        queryresult["write"]=list(set(queryresult["write"]))
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

        if(os.path.isfile("files/"+file)):
            os.remove("files/"+file)

    return {"message":"success","statuscode":200}


@filerouter.get("/readfile/{file}",response_class=HTMLResponse,dependencies=[Depends(cookie)])
async def read_file(file:str,request : Request,session_data: SessionData = Depends(verifier)):
    payload=jwt.decode(session_data.user_token,oauth.get_jwtsecret(),algorithms=['HS256'])
    filename=file.lower()
    path="files/"+filename
    filetype = mimetypes.guess_type(path)[0].split("/")[0]
    if filetype == 'text':
          f = gzip.open(path, "rb")
          files=f.read().decode()
          return templates.TemplateResponse("showfile.html",{"request":request,"username":payload['email'],"file":files,"time":time.ctime(os.path.getctime("files/"+file)),"filename":file})
    elif filetype == 'image':
        return templates.TemplateResponse("showimage.html",{"request":request,"username":payload['email'],"time":time.ctime(os.path.getctime("files/"+file)),"filename":file})
    else:
        return templates.TemplateResponse("showvideo.html",{"request":request,"username":payload['email'],"time":time.ctime(os.path.getctime("files/"+file)),"filename":file})

@filerouter.get("/writefile/{file}",response_class=HTMLResponse,dependencies=[Depends(cookie)])
async def read_file(file:str,request : Request,session_data: SessionData = Depends(verifier)):
    payload=jwt.decode(session_data.user_token,oauth.get_jwtsecret(),algorithms=['HS256'])
    filename=file.lower()
    path="files/"+filename
    filetype = mimetypes.guess_type(path)[0].split("/")[0]
    if filetype == 'text':
          f = gzip.open(path, "rb")
          files=f.read().decode()
          return templates.TemplateResponse("showwritefile.html",{"request":request,"username":payload['email'],"file":files,"time":time.ctime(os.path.getctime("files/"+file)),"filename":file})
    elif filetype == 'image':
        return templates.TemplateResponse("editimage.html",{"request":request,"username":payload['email'],"time":time.ctime(os.path.getctime("files/"+file)),"filename":file})
    else:
        return templates.TemplateResponse("editvideo.html",{"request":request,"username":payload['email'],"time":time.ctime(os.path.getctime("files/"+file)),"filename":file})


@filerouter.post("/modifyfile/{file}",dependencies=[Depends(cookie)])
async def handle_form(file:str,filetitle:str=Form(...),textarea:str=Form(...)):

    path="files/"+file
    if textarea!='None':
        f = gzip.open(path, "wb+")
        f.write(textarea.encode())
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


