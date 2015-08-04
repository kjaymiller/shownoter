import requests
from bs4 import BeautifulSoup

def clean_line(line):
    """removes any non-ascii characters from the title"""
    return str().join(c for c in line if ord(c) in range(32,129))

def get_title(url):
    request = requests.get(url)
    soup = BeautifulSoup.content(request)
    title = soup.title.text
    return clean_link(title)

class Link:
    """Link object to be passed to shownotes"""
    def __init__(url, **kwargs)
        self.title = kwargs.get('title', get_title(url))
        self.url = url
        
        
    