import pymongo
from config import DB_URI, DB_NAME

dbclient = pymongo.MongoClient(DB_URI)
database = dbclient[DB_NAME]

user_data = database['users']
admins_collection = database['admins']

async def add_user(user_id: int):
    user_data.insert_one({'_id': user_id})
    return

async def present_user(user_id: int):
    found = user_data.find_one({'_id': user_id})
    return bool(found)

async def full_userbase():
    user_docs = user_data.find()
    user_ids = [doc['_id'] for doc in user_docs]
    return user_ids

async def del_user(user_id: int):
    user_data.delete_one({'_id': user_id})
    return

async def add_admin(user_id: int):
    try:
        admins_collection.insert_one({'_id': user_id})
        return True
    except Exception as e:
        print(f"Failed to add admin: {e}")
        return False
        
async def remove_admin(user_id: int):
    try:
        admins_collection.delete_one({'_id': user_id})
        return True
    except Exception as e:
        print(f"Failed to remove admin: {e}")
        return False

async def is_admin(user_id: int):
    return bool(admins_collection.find_one({'_id': user_id}))

async def get_admin_list():
    admin_docs = admins_collection.find()
    admin_ids = [doc['_id'] for doc in admin_docs]
    return admin_ids
