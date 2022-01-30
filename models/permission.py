from typing import List
from pydantic import BaseModel
from schemas.permission import permissionsEntity
from config.db import permission

class Permission(BaseModel):

    username: str
    read:List = []
    write:List = []
    owner:List = []

    @staticmethod
    def get_permissionobj(username,read=[],write=[],owner=[]):
        return {"username":username,"read":read,"write":write,"owner":owner}

    @staticmethod
    def addpermissions(userlist,filename):
        userdict={}

        userlist=userlist[0].strip("'").split(",")
        userlist=list(set(userlist))
        for permissions in userlist:
            user,permissionval=permissions.split("-")
            if user in userdict:
                userdict[user].append(permissionval)

            else:
                userdict[user]=[permissionval]

        print(userdict)

        users=list(userdict.keys())
        permissions=list(userdict.values())

        print(users)
        print(permissions)

        i=0
        for user in users:
            queryresult=permission.find_one({"username":user})
            if queryresult==None:
                read=[]
                write=[]
                exe=[]
                for value in permissions[i]:
                    if value=='read':
                        read.append(filename)
                        read=list(set(read))
                    elif value=='write':
                        write.append(filename)
                        write=list(set(write))
                    else:
                        exe.append(filename)
                        exe=list(set(exe))
                query=Permission.get_permissionobj(user,read,write,exe)

                permission.insert_one(query)
                i+=1
            else:
                queryresult=permissionsEntity(queryresult)
                for value in permissions[i]:
                    if value in queryresult:
                        queryresult[value].append(filename)
                        queryresult[value]=list(set(queryresult[value]))
                        if(value=='write'):
                            if(len(queryresult['read'])<1):
                                queryresult['read']=[filename]
                            else:
                                queryresult['read'].append(filename)
                                queryresult['read']=list(set(queryresult['read']))
                    else:
                        queryresult[value]=[filename]
                        queryresult[value]=list(set(queryresult[value]))
                        if(value=='write'):
                            if(len(queryresult['read'])<1):
                                queryresult['read']=[filename]
                            else:
                                queryresult['read'].append(filename)
                                queryresult['read']=list(set(queryresult['read']))

                queryresult.pop('id')

                newvalue={"$set":queryresult}

                permission.update_one({"username":user}, newvalue)
                i+=1