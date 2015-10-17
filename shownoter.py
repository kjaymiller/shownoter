import re
import requests
from bs4 import BeautifulSoup

def link_detect(site):
    re_link =  re.compile(r'\b\S+\.[a-zA-Z]{2,}\S*', re.M)
    return re.findall(re_link, site)

def valid_link(site):
    prefix = ''
    if not re.search(r'\w{3,5}://', site):
        prefix += 'http://'
    return prefix + site

def title(site):
    r = requests.get(site)
    return BeautifulSoup(r.text, 'html.parser').title.text

def markdown(site, title):
    return '{}[{}]({})'.format('!' if not title else '', title, site)

def link(site):
    link_url = valid_link(site)
    link_title = title(site)
    link_markdown = markdown(site=link_url, title=link_title)
    
    return {
    'url':link_url,
    'title':link_title,
    'markdown':link_markdown
    }

