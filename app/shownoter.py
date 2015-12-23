""" The shownoter module contains the core Shownoter functionality """

import re
import requests

from bs4 import BeautifulSoup
from markdown import markdown


def format_links_as_hash(source):

    chat_links = link_detect(source)
    links = []

    for link in chat_links:
        link = link.lower()
        if image_detect(link):
            link = Image(link)

        else:
            link = Link(link)

        entry = {
            'url':link.url,
            'title':link.title,
            'markdown':link.markdown}
        links.append(entry)

    return links

def format_links_as_markdown(source):
    """ Wraps the shownoter functionality in a single function call """
    links = link_detect(source)
    urls = []

    for link in links:
        if image_detect(link):
            entry = Image(link)
        else:
            entry = Link(link)

        urls.append(entry.markdown)

    output = links_to_string(urls)
    return output.strip()

def link_detect(site):
    """ Returns a list of urls from a string"""
    re_link =  re.compile(r'\b\S+\.[a-zA-Z]{2,}\S*', re.M)
    results = re.findall(re_link, site)
    return results

def get(link):
    """ A wrapper around requests.get to allow for easy mocking """
    return requests.get(link, timeout=1.5, allow_redirects=False)

def image_detect(url):
    """
    Determines is a string is an image.
    Returns true if it is an image.
    """
    image_extension = ['.jpg', '.png', '.jpeg', '.gif']
    extension = re.search(r'\.[a-zA-Z]{2,}$', url, re.M)

    if extension == None:
        return False

    if extension.group(0) in image_extension:
        return True

    return False

def parse_title(content):
    """Parses the title of a site from it's content"""
    return BeautifulSoup(content, 'html.parser').title.text

def link_markdown(title, url):
    """Formats a generic link to a markdown list item link"""
    return '* [{}]({})'.format(title, url)

def image_markdown(title, url):
    """Formats a link as an image"""
    return '* ![{}]({})'.format(title, url)

class Link():
    """ A class that wraps link functionality """
    def __init__(self, site):
        self.site = self.valid_link(site)
        self.url =  self.site.url
        self.title = parse_title(self.site.content)
        self.markdown = link_markdown(self.title, self.url)

    def valid_link(self, site):
        """Returns the content of a website from a url

        If the first request fails it will attempt variations

        If all variations fail a ValueError is raised"""
        if re.search(r'^\w{3,5}://', site):

            try:
                request = get(site)

            except:
                print('Link not valid') #TODO:log statement
                return False

            else:
                return request

        else:
            prefixes = ['http://', 'https://', 'http://www.', 'https://www.']

            for prefix in prefixes:

                try:
                    request = get(prefix + site)

                except:
                    print('tried {} failed'.format(prefix + site)) #TODO:log statement

                else:

                    if request.status_code == 200:
                        return request
                    else:
                        continue

            raise ValueError('No Valid Link Detected')

class Image(Link):
    """Images are like links except they ignore connectivity tests."""
    title = ''

    def __init__(self, site):
        self.url = site
        self.markdown = image_markdown(self.title, self.url)

def links_to_string(links):
    """This function takes a list of objects and returns it as a string"""

    links_string = ''
    for link in links:
        links_string += link + '\n'
    return links_string
