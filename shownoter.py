import re
import requests
from bs4 import BeautifulSoup

def link_detect(url):
    re_link =  re.compile(r'\b\S+\.[a-zA-Z]{2,}\S*', re.M)
    return re.findall(re_link, url)

def valid_link(url):
    prefix = ''
    if not re.search(r'\w{3,5}://', url):
        prefix += 'http://'
    return prefix + url

def link_title(url):
    r = requests.get(url)
    return BeautifulSoup(r.text, 'html.parser').title.text