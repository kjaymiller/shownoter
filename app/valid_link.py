import csv
import re

with open('app/static/tlds.txt', 'r+') as domains:
    top_level_domains = [domain.lower() for domain in domains.read().splitlines()]

with open('app/static/uri-schemes-1.csv',
          newline='',
          encoding='utf-8') as csvfile:
    uris = []
    reader = csv.DictReader(csvfile)
    for row in reader:
        uris.append(row['URI Scheme'].lower())


def extract_from_html(url):
    """function takes a url and title from html and converts to dict"""

    re_html = re.compile(r"""<a\ (\w+=["'].["']\ )*
                        href=["'](?P<url>.+)["']
                         (\ \w+=["'].["']\ {0,1})*>
                         (?P<title>.+)
                         </a>""", re.VERBOSE)

    result = re.match(re_html, url)
    return result.groupdict()


def extract_from_markdown(url):
    """function takes title and url from markdown and converts to dict"""

    re_mkdown = re.complile(r"""(?P<image_flag>!)*
                            [(?P<title>.*)]
                            \((<?Purl>.+)\)""", re.VERBOSE)

    result = re.match(re_mkdown, url)
    return result.groupdict()
