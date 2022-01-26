from pydantic import BaseModel

class User(BaseModel):
    email:str
    password:str

    @staticmethod
    def get_userobj(email,password):
        return {"email":email,"password":password}