import re

def link_detect(text):
    re_link =  re.compile(r'\b\S+\.[a-zA-Z]{2,}\S*', re.M)
    return re.findall(re_link, text)

def valid_link(text):
    return '{}{}'.format('' if text.
