import re

def re_link(text):
    re_link =  re.compile(r'^#.*|\b\S+\.\S+', re.M)
    result =  re.findall(re_link, text)
    return result
