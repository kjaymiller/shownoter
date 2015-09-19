import re
import requests
from bs4 import BeautifulSoup

def re_link(text):
    re_link =  re.compile(r'\b\S+\.\S+', re.M)
    results = list()
    for link in  re.findall(re_link, text):
        url_start = any([link.startswith('http://'), link.startswith('https://')])
        if not url_start:
            results.append("http://" + link)
        else:    
            results.append(link)
    
    return results



def detect_image(link):
    image_extensions = ['.jpg', '.png', '.gif']
    match = re.search(r'^.+(?P<extension>\.\S+)$', link)
    if match.group('extension') in image_extensions:
        return True

def get_links(link, title, image=False):
    if image:
        return '![{title}]({link})'.format(title = title, link = link)
    return '[{title}]({link})'.format(title = title, link = link)

def get_title(url, image=False):
    if image:
        return str()
    request =  requests.get(url)
    soup = BeautifulSoup(request.content, 'html.parser' )
    title =  soup.title.text
    return title
     
