import jwt
from uuid import UUID
from fastapi import APIRouter, Depends,Form, Response
from models.OAuth2 import oauth
from models.Session import SessionData
from models.user import User
from config.db import collection
from schemas.user import userEntity,usersEntity
from models.hasher import Hasher
from models.OAuth2 import oauth
from bson import objectid
from uuid import uuid4
from models.Session import cookie,backend
from models.Basicverifier import verifier

user=APIRouter()

# oauthobj = oauth()

@user.get('/database/file')
async def find_all_users():
    print(usersEntity(collection.find()))
    return usersEntity(collection.find())

@user.get("/logout")
async def del_session(response: Response, session_id: UUID = Depends(cookie)):
    print(session_id)
    await backend.delete(session_id)
    cookie.delete_from_response(response)
    return "deleted session"

@user.get("/whoami", dependencies=[Depends(cookie)])
async def whoami(session_data: SessionData = Depends(verifier)):
    return session_data

@user.post("/login")
async def login(response:Response,email:str = Form(...),password:str = Form(...)):
     queryresult=collection.find_one({"email":email})
     if queryresult == None:
          return {"message":"user not found"}

     result=userEntity(queryresult)
     if not Hasher.verify_password(password,result["password"]):
         return {"message":"Invalid password"}

     user_obj=User.get_userobj(email=email,password=password)
     token=jwt.encode(user_obj,oauth.get_jwtsecret())

     session = uuid4()
     print(session)
     data = SessionData(username=token)
     await backend.create(session, data)
     cookie.attach_to_response(response, session)

    #  oauthobj.set_token(token)

     return {"access_token":token,"token_type":"bearer"}


# @user.post('/')
# async def index(token:str=Depends(oauth.get_oauthscheme())):
#     return {'the_token':token}


@user.post('/register')
async def create_user(email:str= Form(...),password:str=Form(...)):
    hashed_password=Hasher.get_password_hash(password=password)
    user_obj=User.get_userobj(email=email,password=hashed_password)
    collection.insert_one(user_obj)
    return "SUCCESS"

@user.put('/{id}')
async def update_user(id,email:str= Form(...),password:str=Form(...)):
    collection.find_one_and_update({"_id":objectid(id)},{
        "$set":dict(User.get_userobj(email=email,password=password))
    })
    return userEntity(collection.find_one({"_id":objectid(id)}))

