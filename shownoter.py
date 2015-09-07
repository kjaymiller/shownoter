import re

def re_link(text):
    re_link =  re.compile(r'^#.*|\b\S+\.\S+', re.M)
    result =  re.findall(re_link, text)
    return result

def get_site(url):
    result = requests.get(url)
    return result.content

def get_title(site):
    title = soup.title(site)
    return title
