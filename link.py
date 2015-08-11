import re

def re_link(text):
    re_link =  re.compile(r'^#.*|\b\S+\.\S+', re.M)
    return re.findall(re_link, text)

class Link():
    """link object"""
    def __init__(self, text):
        self.text = re_link(text)
        self.category = "Test1"
