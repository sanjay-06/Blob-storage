import jwt
from models.OAuth2 import oauth
from models.Session import SessionData, cookie
from fastapi import APIRouter, Depends,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from models.Basicverifier import verifier
from config.db import permission
from schemas.permission import permissionsEntity

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

    finallist=merge(listreadwrite,file['execute'])

    return templates.TemplateResponse("files.html",{"request":request,"username":email,"result":finallist})

@navigator.get("/permission",response_class=HTMLResponse,dependencies=[Depends(cookie)])
def write_home(request : Request,session_data: SessionData = Depends(verifier)):
    payload=jwt.decode(session_data.user_token,oauth.get_jwtsecret(),algorithms=['HS256'])
    return templates.TemplateResponse("permission.html",{"request":request,"username":payload['email']})

@navigator.get("/upload",response_class=HTMLResponse,dependencies=[Depends(cookie)])
def write_home(request : Request,session_data: SessionData = Depends(verifier)):
    payload=jwt.decode(session_data.user_token,oauth.get_jwtsecret(),algorithms=['HS256'])
    return templates.TemplateResponse("upload.html",{"request":request,"username":payload['email']})

@navigator.get("/signup",response_class=HTMLResponse)
def write_home(request : Request):
    return templates.TemplateResponse("signup.html",{"request":request})