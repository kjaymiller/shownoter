import re
import requests

from bs4 import BeautifulSoup
from markdown import markdown


def link_detect(site):
    re_link =  re.compile(r'\b\S+\.[a-zA-Z]{2,}\S*', re.M)
    results = re.findall(re_link, site)
    return results

def get(link):
    request = requests.get(link, timeout=1.5, allow_redirects=False)
    return request

def image_detect(site):    
    image_extension = ['.jpg', '.png', '.jpeg', 'gif']
    extension = re.search(r'\.[a-zA-Z]{2,}$', site, re.M)
    
    if extension.group(0) in image_extension:
        print('image detected')
        return True
    
    else:
        return False

class Link():
    def __init__(self, site):
        self.site = self.valid_link(site)
        self.url =  self.site.url       
        self.title = BeautifulSoup(self.site.content, 'html.parser').title.text
        self.markdown = '* [{}]({})'.format(self.title, self.url)

    def valid_link(self, site):
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
        self.markdown = '* ![]({})'.format(self.title, self.url)

def links_to_string(links):
"""This function takes a list of objects and returns it as a string"""

    links_string = ''
    for link in links:
        links_string += link + '\n'
    return links_string


def compile_shownotes(links, title, description):
"""this function takes the individual components and returns the whole as a string"""

return '''#{title},
##Description
{description}

##Links
{links}'''}
