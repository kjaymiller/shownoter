import pymongo 
import re
from bson.objectid import ObjectId

conn = pymongo.MongoClient('localhost', 27017)
db = conn.shownoter
shownotes_coll = db.shownotes
links_coll = db.link_cache



def create_entry(links):
    """Adds new link to database"""
    result = shownotes_coll.insert_one({'links':links})
    return result.inserted_id

def append_to_entry(id, entry):
    """adds/edits fields to entry in database. """
    result = shownotes_coll.update_one({'_id':ObjectId(id)}, {'$set': entry}, upsert=True)
    return result

def retrieve(id):
    """fetches results in database"""
    result = shownotes_coll.find_one({'_id':ObjectId(id)})
    return result

def retrieve_from_cache(url):
    """looks for links in the caching database"""
    domain = get_domain(url)
    result = links_coll.find_one({'url':domain})
    return result

def cache_url(url,title):
    """add url to cache"""
    domain = get_domain(url)
    links_coll.insert_one({'url':url, 'domain':domain, 'title':title})

def get_domain(url):
    """returns the domain of the url"""
    if url[-1] == '/':
        url = url[:-1]
    pattern = re.compile(r'\w{3,5}:\/\/(www\.)?|www\.')
    new_url = re.sub(pattern,'', url)
    return new_url
