import pymongo 
from bson.objectid import ObjectId

conn = pymongo.MongoClient('localhost', 27017)
db = conn.test
shownoter = db.shownoter

def create_entry(links):
    """Adds new link to database"""
    result = shownoter.insert_one({'links':links})
    return result.inserted_id

def append_to_entry(id, **args):
    """adds/edits fields to entry in database"""
    result = shownoter.update_one({'_id':ObjectId(id)}, {'$set': {field:value}}, upsert=True)

def retrieve(id):
    """fetches results in database"""
    result = shownoter.find_one({'_id':ObjectId(id)})
    return result
