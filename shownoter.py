import re
import requests
from bs4 import BeautifulSoup

def re_link(text):
    re_link =  re.compile(r'\b\S+\.\S+', re.M)
    result =  re.findall(re_link, text)
    return result

def file_type(link):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.swf', '.xvf']
    match = re.search(r'^.+(?P<extension>\.\S+)$', link)
    extension = match.group('extension')
    if extension in image_extensions:
        return extension

def get_title(url):
    request =  requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser' )
    return soup.title.text 
    
