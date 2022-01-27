from typing import List
from pydantic import BaseModel

class Permission(BaseModel):

    username: str
    read:List = []
    write:List = []
    execute:List = []

    @staticmethod
    def get_userobj(username,read,write,execute):
        return {"username":username,"read":read,"write":write,"execute":execute}