from pymongo import MongoClient
from models.permission import Permission

from schemas.permission import permissionsEntity

conn = MongoClient("mongodb+srv://sanjay:1234@cluster0.gxmvm.mongodb.net/cloudwiry?retryWrites=true&w=majority")

db=conn.get_database("cloudwiry")

permission=db.permissions

# x=permission.insert_one({"username":"san692001@gmail.com", "read":["text1.txt","text2.txt","text3.txt"],
#     "write":["text1.txt","text2.txt","text3.txt"],
#     "execute":["text1.txt","text2.txt","text3.txt"]})


# userlist=["san692001@gmail.com-read","san692001@gmail.com-write","a@gmail.com-read"]

# userdict={}
# for permissions in userlist:
#     user,permissionval=permissions.split("-")

#     if user in userdict:
#         userdict[user].append(permissionval)
#     else:
#         userdict[user]=[permissionval]

# print(userdict)

# users=list(userdict.keys())
# permissions=list(userdict.values())

# print(users)
# print(permissions)

# i=0
# for user in users:
#     queryresult=permission.find_one({"username":user})
#     if queryresult==None:
#         username=user
#         read=[]
#         write=[]
#         exe=[]
#         for value in permissions[i]:
#             if value=='read':
#                 read.append('1.txt')
#             elif value=='write':
#                 write.append('1.txt')
#             else:
#                 exe.append('1.txt')
#         query=Permission.get_permissionobj(user,read,write,exe)

#         permission.insert_one(query)
#         i+=1
#     else:
#         queryresult=permissionsEntity(queryresult)
#         for value in permissions[i]:
#             if value in queryresult:
#                 queryresult[value].append('1.txt')
#             else:
#                 queryresult[value]=['1.txt']


#         queryresult.pop('id')

#         newvalue={"$set":queryresult}

#         permission.update_one({"username":user}, newvalue)
#         i+=1







# x=permission.find()

# for e in x:
#     print(e)


# print("Last modified: %s" % )
# print("Created: %s" % )

# {'username': 'john@gmail.com', 'read': {'text1.txt', 'chat.png', 'customers.png'}, 'write': [], 'owner': []}

f = open("files/text1.txt", "r")

file=f.read()

print(file)