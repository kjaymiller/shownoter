import re
from requests import get
from bs4 import BeautifulSoup

def re_link(text):
    re_link =  re.compile(r'\b\S+\.[a-zA-Z]{2,}\S*', re.M)
    return set(re.findall(re_link, text))
        

def detect_image(link):
    image_extensions = ['.jpg', '.png', '.gif']
    match = re.search(r'^.+(?P<extension>\.\S+)', link)
    return match.group('extension') in image_extensions

def validate_link(link):
    try:
        if not re.search(r'\w{3,5}://', link):
            print('adding to {}'.format(link))
            link = 'http://' + link
        request = get(link, timeout= 1.5)

    except:
        return False 
    
    else:
        return request 

def  get_title(link):
    soup = BeautifulSoup(link.text, 'html.parser')
    return soup.title.string

def get_markdown(url, title = ''):
    return '* {}[{title}]({url})'.format('!' if not title else '', title=title, url=url)

         
