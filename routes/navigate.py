import jwt
from uuid import UUID
from models.OAuth2 import oauth
from models.Session import SessionData, cookie
from models.Basicverifier import backend
from fastapi import APIRouter, Depends,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from models.Basicverifier import verifier

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


@navigator.get("/files",response_class=HTMLResponse,dependencies=[Depends(cookie)])
# def write_home(request : Request = Depends(get_token)):
def write_home(request : Request,session_data: SessionData = Depends(verifier)):
    payload=jwt.decode(session_data.user_token,oauth.get_jwtsecret(),algorithms=['HS256'])
    return templates.TemplateResponse("files.html",{"request":request,"username":payload['email']})

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