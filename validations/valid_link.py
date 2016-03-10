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


def is_url(potential_url):
    """ if the """
    link = re.match(r'\b\S+\.[a-zA-Z]{2,}\S*', potential_url)

    if link:
        return True

    else:
        return False
