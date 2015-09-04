import re

def re_link(text):
    re_link =  re.compile(r'^#.*|\b\S+\.\S+', re.M)
    result =  re.findall(re_link, text)
    return result

def get_title(url):
    pass

class Link():
    """link object"""
    def __init__(self, text):
        self.text = text
        self.category = category
        self.title = title
