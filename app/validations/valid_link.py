import csv
import re


with open('app/static/tlds.txt', 'r+') as domains:
    top_level_domains = [
        domain.lower() for domain in domains.read().splitlines()]


with open('app/static/uri-schemes-1.csv',
          newline='',
          encoding='utf-8') as csvfile:
    uris = []
    reader = csv.DictReader(csvfile)
    for row in reader:
        uris.append(row['URI Scheme'].lower())


def detect_a_in_html(a_tag):
    """checks tag for a record"""
    if re.search(r'<a.+</a>', a_tag):
        return True

    else:
        return False


def detect_img_in_html(img_tag):
    if re.search(r'<img.+>', img_tag):
        return True

    else:
        return False


def detect_url_from_href(a_tag):
    url = re.search(r"""href=["'](?P<url>\S+)["']""", a_tag)
    return url.group('url') if url else None


def detect_title_from_a_tag(a_tag):
    title = re.search(r'<a.+>(?P<title>.*)</a>', a_tag)
    return title.group('title') if title else None


def detect_url_from_img(img_tag):
    url = re.search(r"""src=["'](?P<url>\S+)["']""", img_tag)
    return url.group('url') if url else None


def detect_title_from_img(img_tag):
    title = re.search(r"""alt=["'](?P<title>.+)["']""", img_tag)
    return title.group('title') if title else None


def render_link_from_html(a_tag):
    if detect_a_in_html(a_tag):
        url = detect_url_from_href(a_tag)
        title = detect_title_from_a_tag(a_tag)

        if url:
            return {
                'url': url,
                'title': title
                }
    else:
        return None


def detect_markdown(content):
    """function content a single line """

    link = re.search(r'!*\[.*\]\(.+\)', content)
    if link:
        return link.group()
    else:
        return None


def markdown_link_or_image(content):
    if detect_markdown(content):
        if content[0] == '!':
            return 'image'
        else:
            return 'link'
