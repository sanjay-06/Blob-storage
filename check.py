from pymongo import MongoClient

conn = MongoClient("mongodb+srv://sanjay:1234@cluster0.gxmvm.mongodb.net/cloudwiry?retryWrites=true&w=majority")

db=conn.get_database("cloudwiry")

permission=db.permissions

x=permission.insert_one({"username":"san692001@gmail.com", "read":["text1.txt","text2.txt","text3.txt"],
    "write":["text1.txt","text2.txt","text3.txt"],
    "execute":["text1.txt","text2.txt","text3.txt"]})

print(x)


# print("Last modified: %s" % )
# print("Created: %s" % )