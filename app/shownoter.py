"""
The shownoter module contains the core Shownoter functionality

WARNING: Shownoter.py is undergoing a refactoring. Please do not add any new
code until the refactoring has been completed.

For information on refactoring: please see Trello board at
https://trello.com/c/1YXgQUOq/117-refactor-shownoter-py
"""


import re
import requests

from app import url_parser
from bs4 import BeautifulSoup
from datetime import datetime


def detect_links(content):  # TODO: REMOVE
    """ Returns a list of urls from a string"""
    re_link = re.compile(r'\b\S+\.[a-zA-Z]{2,}\S*', re.M)
    links = []

    for results in re.findall(re_link, content):

        if results not in links:
            links.append(results)

    return links


def possible_urls(url):
    """ Generator that returns possible variations of a given url """
    if re.search(r'^\w{3,5}://', url):
        yield url
    else:
        prefixes = ['http://', 'https://', 'http://www.', 'https://www.']

        for prefix in prefixes:
            yield prefix+url


def request_get(link):
    """ A wrapper around requests.get to allow for easy mocking """
    return requests.get(link, timeout=1.5, allow_redirects=False)


def request_content(url):
    """ Returns content from the url provided or raises ValueError """
    try:
        request = request_get(url)
    except:
        # TODO insert some logging here requests.ConnectionError (or other)
        # being trapped.
        raise ValueError("Url not found")

    if request.status_code == 200:
        return request
    else:
        # TODO insert some logging here
        pass

    raise ValueError("Url not found")


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


def fetch_site_title(site_content, default_title=""):
    """Parses the title of a site from it's content"""
    if site_content is None:  # if site returns no data
        return default_title

    soup = BeautifulSoup(site_content, 'html.parser')
    if soup is None or soup.title is None:
        return default_title

    title = soup.title.text
    return title.strip()


def format_link_as_markdown(title, url, is_image):
    """Formats a generic link to a markdown list item link uses image markdown
    if image detected"""
    if is_image:
        return '* ![{}]({})'.format(title, url)

    else:
        return '* [{}]({})'.format(title, url)


def fetch_data(site):
    """ Collects the various information about the link """
    # TODO REMOVE SELF SITE AND MAKE JUST SITE!!!
    site = valid_link(site)
    url = site.url
    title = fetch_site_title(site.content)
    return (site, url, title)


def prep_link(url):
    link_is_valid = True
    url = valid_link(url).url
    link = {'url': url}
    url = link['url']
    link['is_image'] = url_parser.image_detect(url)

    if link['is_image']:
        link['title'] = ''

    else:
        try:
            site, url, title = fetch_data(url)
            link['title'] = title

        except ValueError:
            link_is_valid = False

    if link_is_valid:
        if not link['title']:
            link['title'] = link['url']

        title = link['title']
        markdown = format_link_as_markdown(title=title,
                                           url=url,
                                           is_image=link['is_image'])

        link['markdown'] = markdown
        link['created'] = datetime.utcnow()
        return link

    else:
        return None

def check_link_validity(url):
    return True
