import re

def link_detect(text):
    re_link =  re.compile(r'\b\S+\.[a-zA-Z]{2,}\S*', re.M)
    return re.findall(re_link, text)

def valid_link(text):
    prefix = ''
    if not re.search(r'\w{3,5}://', text):
        prefix += 'http://'
    return prefix + text