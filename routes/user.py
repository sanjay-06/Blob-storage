import jwt
from fastapi import APIRouter, Depends,Form
from matplotlib.pyplot import connect
from models.OAuth2 import oauth
from models.user import User
from config.db import collection
from schemas.user import userEntity,usersEntity
from models.hasher import Hasher
from models.OAuth2 import oauth
from bson import objectid

user=APIRouter()

@user.get('/database/file')
async def find_all_users():
    print(usersEntity(collection.find()))
    return usersEntity(collection.find())

@user.post("/login")
async def login(email:str = Form(...),password:str = Form(...)):
     queryresult=collection.find_one({"email":email})
     if queryresult == None:
          return {"message":"user not found"}

     result=userEntity(queryresult)
     if not Hasher.verify_password(password,result["password"]):
         return {"message":"Invalid password"}

     user_obj=User.get_userobj(email=email,password=password)
     token=jwt.encode(user_obj,oauth.get_jwtsecret())

     return {"access_token":token,"token_type":"bearer"}


@user.post('/')
async def index(token:str=Depends(oauth.get_oauthscheme())):
    return {'the_token':token}


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

