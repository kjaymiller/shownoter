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

class Link():
    def __init__(self, title, url):
        self.title = title
        self.url = url

    def markdownerize(self): # Thank Jamal for the name
        title = self.title
        url = self.url
        markdown = '[{title}]({url})'.format(title = title, url = url)
        return markdown

class Image(Link):
    def markdownerize(self):
        title = self.title
        url = self.url
        markdown = '![{title}]({url})'.format(title = title, url = url)
        return markdown
