""" 
The shownoter module contains the core Shownoter functionality 

WARNING: Shownoter.py is undergoing a refactoring. Please do not add any new code until the refactoring has been completed. 

For information on refactoring: please see Trello board at https://trello.com/c/1YXgQUOq/117-refactor-shownoter-py
"""


import re
import requests

from app import mongo
from app import url_parser

from datetime import datetime
from bs4 import BeautifulSoup
from markdown import markdown

def link_detect(site): #TODO: REMOVE
    """ Returns a list of urls from a string"""
    re_link =  re.compile(r'\b\S+\.[a-zA-Z]{2,}\S*', re.M)
    links = []

    for link in re.findall(re_link, site):

        if link not in links:
            links.append(link)

    return links

def get(link): 
    """ A wrapper around requests.get to allow for easy mocking """
    return requests.get(link, timeout=1.5, allow_redirects=False)

def parse_title(content, default_title=""):
    """Parses the title of a site from it's content"""
    if content == None:
        return default_title

    soup =  BeautifulSoup(content, 'html.parser')
    if soup == None or soup.title == None:
        return default_title

    title = soup.title.text
    return title.strip()

def format_link_as_markdown(title, url, is_image):
    """Formats a generic link to a markdown list item link uses image markdown if image detected"""
    if is_image:
        return '* ![{}]({})'.format(title, url)

    else:
        return '* [{}]({})'.format(title, url)

def request_content(site):
    """ Returns content or raises ValueError """
    success = True

    try:
        request = get(site)
    except:
        # TODO insert some logging here requests.ConnectionError (or other) being trapped.
        raise ValueError("Url not found")

    if request.status_code == 200:
        return request
    else:
        # TODO insert some logging here
        pass

    raise ValueError("Url not found")

def possible_urls(url):
    """ Generator that returns possible variations of a given url """
    if re.search(r'^\w{3,5}://', url):
        yield url
    else:
        prefixes = ['http://', 'https://', 'http://www.', 'https://www.']

        for prefix in prefixes:
            yield prefix+url

def valid_link(site):
    """Returns the content of a website from a url

    If the first request fails it will attempt variations

    If all variations fail a ValueError is raised"""

    for url in possible_urls(site):
        try:
            return request_content(url)
        except ValueError:
            continue

    raise ValueError("No valid link permutation found")

    def fetch_data(site):
        """ Collects the various information about the link """
            #TODO REMOVE SELF SITE AND MAKE JUST SITE!!!
            site = valid_link(site)
            url =  site.url
            title = parse_title(self.site.content)


def retrieve_links_from_source(source):
    """wrapper around shownoter functionality. This creates a dictionary values of the Link/Image class"""

    potential_links = url_parser.search_for_links(source)
    links = []

    for link in potential_links:
        links_is_valid = True 
        # TODO: insert checks for valid links
        
        link = {url:'url'}
        link['is_image'] = url_parser.image_detect(link)

        if link['is_image']:
            link['title'] = ''
        
        else:
            try:
                
                collect_data(url)
            except ValueError:
                valid_link = False
                continue

        if valid_link: 
            if not link['title']:
                link['title'] = link['url']
            
            markdown = format_link_as_markdown(title=title,
                    url=url,
                    is_image=link['is_image'])

            entry = {
                'url':link.url,
                'title':link.title,
                'markdown':markdown}
            
            links.append(entry)

    return links

