from gc import collect
from matplotlib.collections import Collection
from pymongo import MongoClient

conn = MongoClient("mongodb+srv://sanjay:1234@cluster0.gxmvm.mongodb.net/cloudwiry?retryWrites=true&w=majority")

db= conn.get_database('cloudwiry')

collection = db.usercredentials

