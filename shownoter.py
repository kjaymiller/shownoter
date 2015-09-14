import re
import requests
from bs4 import BeautifulSoup

def re_link(text):
    re_link =  re.compile(r'\b\S+\.\S+', re.M)
    result =  re.findall(re_link, text)
    return result

def get_images(link):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']
    match = re.search(r'^.+(?P<extension>\.\S+)$', link)
    if match.group('extension') in image_extensions:
        return '![]({})'.format(link)

def get_title(url):
    request =  requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser' )
    return soup.title.text 
    
