import re
from app.mongo import retrieve_from_db
from app.mongo import create_entry
from app.mongo import links_coll


def remove_url_scheme(url):
    """removes the url scheme and/or 'www' from the url and
        returns the domain and extension"""

    pattern = re.compile(r'\w{3,5}:\/\/(www\.)?|www\.')
    new_url = re.sub(pattern, '', url)
    return new_url


def retrieve_from_cache_db(url):
    """checks links_coll for entries returns url_entry in True or False"""
    base_url = remove_url_scheme(url)
    db_entry = retrieve_from_db(value=base_url,
                                collection=links_coll,
                                field="domain")

    return db_entry


def insert_to_cache_db(db_entry):
    """wrapper that adds entry to link_cache database"""
    return create_entry(value=db_entry, collection=links_coll)
