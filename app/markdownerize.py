import shownoter
from collections import namedtuple
from itertools import chain

def markdownerize(text_input):
    links = shownoter.re_link(text_input)
    images = list(filter(shownoter.detect_image, links))

    site = namedtuple('site', ['url', 'title'])
    potential_sites = [(link, shownoter.validate_link(link)) for link in links if link not in images]
    print(potential_sites)
    sites = (site(link[0], shownoter.get_title(link[1])) for link in potential_sites if link[1])

    markdown_images = (shownoter.get_markdown(image) for image in images)
    markdown_sites = (shownoter.get_markdown(link.url, title=link.title) for link in sites)
    markdown = list(chain(markdown_sites, markdown_images))
    return markdown