from pymongo import MongoClient
from models.permission import Permission

from schemas.permission import permissionsEntity

conn = MongoClient("mongodb+srv://sanjay:1234@cluster0.gxmvm.mongodb.net/cloudwiry?retryWrites=true&w=majority")

db=conn.get_database("cloudwiry")

permission=db.permissions

col=db.usercredentials

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

# f = open("files/text1.txt", "r")

# file=f.read()

# print(file)

# def replace(element1,element2,listval):
#     return list(map(lambda x: x.replace(element1, element2), listval))


# file="text1.txt"
# filetitle="Text1.txt"
# allpermission=permission.find()

# for filepermission in allpermission:

#     if file in filepermission['read']:
#         filepermission['read']=replace(file,filetitle,filepermission['read'])

#     if file in filepermission['write']:
#         filepermission['write']=replace(file,filetitle,filepermission['write'])

#     if file in filepermission['owner']:
#         filepermission['owner']=replace(file,filetitle,filepermission['owner'])

#     filepermission.pop('_id')

#     newquery={"$set":filepermission}

#     permission.update_one({"username":filepermission['username']},newquery)

# allpermissions=[{'username':'s','read':["1.txt"],'write':[],'owner':[]}]
# owner=["1.txt","2.txt","3.txt"]
# perm=[]
# for filename in owner:
#     for per in allpermissions:
#         for e in per['read']:
#             if e == filename:
#                 perm.append(per['username']+"-"+filename+"-"+"read")

#         for e in per['write']:
#             if e == filename:
#                 perm.append(per['username']+"-"+filename+"-"+'edit')

#         for e in per['owner']:
#             if e == filename:
#                 perm.append(per['username']+"-"+filename+"-"+'owner')


# print(perm)

# list1=[1,2,3]

# list1.remove(1)

# print(list1)
# #Todo

# 1) delete user permissions

# 2) delete file

# 3) ajax request

# 4) fix returns


# x = permission.delete_many({})

# col.delete_many({})

# a=['san692001@gmail.com-read,san692001@gmail.com-write,san692001@gmail.com-owner,19pw28@psgtech.ac.in-owner']

# listval=a[0].strip("'").split(",")

# print(listval)

import imghdr
print(imghdr.what('check.py'))