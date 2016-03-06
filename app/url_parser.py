import re


def search_for_links(content):
    """ Returns a list of urls from a import string"""
    re_link = re.compile(r'\b\S+\.[a-zA-Z]{2,}\S*', re.M)
    links = []
    for link in re.findall(re_link, content):
        if link not in links:
            links.append(link)
            return links


def image_detect(url):
    """Determines if the url is an image. """
    image_extension = ['.jpg', '.png', '.jpeg', '.gif']
    extension = re.search(r'\.[a-zA-Z]{2,}$', url, re.M)

    if extension is None:
        return False

    if extension.group(0) in image_extension:
        return True
