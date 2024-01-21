from pymongo import MongoClient
from config import mongo_token
client = MongoClient(mongo_token)

user_db = client.data.user

class Database:

    def get_ids() -> list[int]:
        users = user_db.find()
        ids = []
        for user in users:
            ids.append(user["user_id"])
        return ids
    
    def find_user(user_id:int) -> None:
        if user_db.find_one({"user_id":user_id}) == None:
            return False
        return True

    def add_user(user_id:int) -> None:
        user_db.insert_one({"user_id":user_id})