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
    image_extension = ['.jpg', '.png', '.jpeg']
    extension = re.search(r'\.[a-zA-Z]{3,}$', site, re.M)
    if extension.group(0) in image_extension:
        return ''
    r = requests.get(site)
    return BeautifulSoup(r.text, 'html.parser').title.text

def create_markdown(site, title):
    return '* {}[{}]({})'.format('!' if not title else '', title, site)

def links_to_string(link_list):
    links = ''
    for link in link_list:
        links += '{}<br>'.format(link)
    return links

def combine_shownotes(description, links, html=False):
    if html:
        separator = '<br>'
    else:
        separator = '\n'
    shownotes = '{}{}{}'.format(description, separator, links)
    return shownotes 
