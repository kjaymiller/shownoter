import re
import requests
from markdown import markdown
from bs4 import BeautifulSoup

def link_detect(site):
    re_link =  re.compile(r'\b\S+\.[a-zA-Z]{2,}\S*', re.M)
    return re.findall(re_link, site)

def valid_link(site):
    def req(link):
        r = requests.get(link, timeout=1.5, allow_redirects=False)
        return r
    
    if re.search(r'\w{3,5}://', site):
        try:
            r = req(site)
        
        except:
            return

    prefixes = ['http://', 'https://', 'http://www.', 'https://www.']
    for prefix in prefixes:
        try:
            result = req(prefix + site)
        
        except:
            print('tried {} failed'.format(prefix + site))
        
        else:
            if result.status_code == 200:
                return result
        
    return

def image_detect(site):    
    image_extension = ['.jpg', '.png', '.jpeg']
    extension = re.search(r'\.[a-zA-Z]{2,}', site, re.M)
    if extension.group(0) in image_extension:
        return True
    
def title(site):
    """Does not look for title if image"""
    if site:
        return BeautifulSoup(site.text, 'html.parser').title.text
    else:
        return ''

def create_markdown(site, title):
    return '* {}[{}]({})'.format('!' if not title else '', title, site)

def links_to_string(link_list):
    links = ''
    for link in link_list:
        links += '{}\n'.format(link)
    return links

def combine_shownotes(description, links, html):
    shownotes = '{}\n##Links\n{}'.format(description, links)
    if html:
        shownotes = markdown(shownotes) 
    else:
        shownotes = shownotes.replace('\n', '<br>')
    return shownotes 
