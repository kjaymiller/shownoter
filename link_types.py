import re

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
