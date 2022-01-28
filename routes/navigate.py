import jwt,os.path, time

from config.db import collection
from models.OAuth2 import oauth
from models.Session import SessionData, cookie
from fastapi import APIRouter, Depends,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from models.Basicverifier import verifier
from config.db import permission
from schemas.permission import permissionsEntity
from schemas.user import usersEntity

navigator=APIRouter()
templates=Jinja2Templates(directory="html")


@navigator.get("/",response_class=HTMLResponse)
def write_home(request : Request):
    return templates.TemplateResponse("index.html",{"request":request})

# async def get_token(token:str = Depends(oauthobj.get_token())):
#     try:
#         payload=jwt.decode(token,oauth.get_jwtsecret(),algorithms=['HS256'])
#         user = payload.email
#         print(payload)

#     except:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="invalid email"
#             )

#     return user

def merge(list1,list2):
    return list1+list(set(list2)-set(list1))

@navigator.get("/files",response_class=HTMLResponse,dependencies=[Depends(cookie)])
def write_home(request : Request,session_data: SessionData = Depends(verifier)):
    payload=jwt.decode(session_data.user_token,oauth.get_jwtsecret(),algorithms=['HS256'])
    email=payload['email']
    result=permission.find_one({"username":email})

    if result == None:
        return {"message":"error"}

    file=permissionsEntity(result)

    listreadwrite=merge(file['read'],file['write'])

    finallist=merge(listreadwrite,file['owner'])

    result=[]
    for file in finallist:
        result.append([file,time.ctime(os.path.getmtime("files/"+file)),time.ctime(os.path.getctime("files/"+file))])

    return templates.TemplateResponse("files.html",{"request":request,"username":email,"result":result})

@navigator.get("/permission",response_class=HTMLResponse,dependencies=[Depends(cookie)])
def write_home(request : Request,session_data: SessionData = Depends(verifier)):
    payload=jwt.decode(session_data.user_token,oauth.get_jwtsecret(),algorithms=['HS256'])

    queryresult=permission.find_one({"username":payload['email']})

    if queryresult== None:
        return {"message":"error not found","statuscode":404}

    queryresult=permissionsEntity(queryresult)

    owner=list(queryresult['owner'])

    userlist=usersEntity(collection.find())
    listval=[]
    for user in userlist:
        if(payload['email']!=user['email']):
            listval.append(user['email'])
    print(listval)

    return templates.TemplateResponse("permission.html",{"request":request,"username":payload['email'],"ownership":owner,"users":listval})

@navigator.get("/upload",response_class=HTMLResponse,dependencies=[Depends(cookie)])
def write_home(request : Request,session_data: SessionData = Depends(verifier)):
    payload=jwt.decode(session_data.user_token,oauth.get_jwtsecret(),algorithms=['HS256'])
    userlist=usersEntity(collection.find())
    listval=[]
    for user in userlist:
        if(payload['email']!=user['email']):
            listval.append(user['email'])
    print(listval)
    return templates.TemplateResponse("upload.html",{"request":request,"username":payload['email'],"users":listval})

@navigator.get("/signup",response_class=HTMLResponse)
def write_home(request : Request):
    return templates.TemplateResponse("signup.html",{"request":request})


@navigator.get("/readfiles",response_class=HTMLResponse,dependencies=[Depends(cookie)])
def show_read_files(request:Request,session_data:SessionData=Depends(verifier)):
    payload=jwt.decode(session_data.user_token,oauth.get_jwtsecret(),algorithms=["HS256"])
    queryresult=permission.find_one({"username":payload['email']})
    if queryresult==None:
        return {"message":"error","statuscode":405}

    queryresult=permissionsEntity(queryresult)
    return templates.TemplateResponse("Read.html",{"request":request,"username":payload['email'],"readfiles":queryresult['read']})

