import pymongo 
from bson.objectid import ObjectId

conn = pymongo.MongoClient('localhost', 27017)
db = conn.test
collection = db.shownoter

def create_entry(links):
    """Adds new link to database"""
    result = collection.insert_one({'links':links})
    return result.inserted_id

def append_to_entry(id, entry):
    """adds/edits fields to entry in database. """

    result = collection.update_one({'_id':ObjectId(id)}, {'$set': entry}, upsert=True)

def retrieve(id):
    """fetches results in database"""
    result = collection.find_one({'_id':ObjectId(id)})
    return result
