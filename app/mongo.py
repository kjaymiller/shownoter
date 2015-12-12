import pymongo 
from bson.objectid import ObjectId

conn = pymongo.MongoClient('localhost', 27017)
db = conn.test
shownoter = db.shownoter

def save_to_db(description, links):
    result = shownoter.insert_one({
        'user':'kjaymiller@gmail.com',
        'description':description, 
        'links':links,
        'title':title})

    return result.inserted_id

def retrieve(id):
    result = shownoter.find_one({'_id':ObjectId(id)})
    return result
