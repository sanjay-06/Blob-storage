from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

mongo_url=os.getenv("Mongo_Database_URL")

conn = MongoClient("mongodb+srv://sanjay:1234@cluster0.gxmvm.mongodb.net/cloudwiry?retryWrites=true&w=majority")

db= conn.get_database('cloudwiry')

collection = db.usercredentials

permission = db.permissions
