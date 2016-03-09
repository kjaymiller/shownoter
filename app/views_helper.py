"""The views_helper.py hosts any functions that assist the views.py module"""
from app import shownoter
from app import url_parser
from app import cache_db


def shownoter_wrapper(content):
    """wrapper around shownoter functionality. This creates a dictionary
    values of the Link/Image class"""

    potential_links = url_parser.search_for_links(content)
    links = []

    for url in potential_links:
        cached_link = cache_db.retrieve_from_cache_db(url)
        if cached_link:
            links.append(cached_link)

        elif shownoter.check_link_validity(url):
            link = shownoter.prep_link(url)

            if link:
                cache_db.insert_to_cache_db(link)
                links.append(link)

        else:
            continue

    return links
