import re

def shownotes(description, links):
    str_links = ''
    for link in links:
        str_links += '{}\n'.format(link)
    notes = '{}\n\n{}'.format(description, str_links)
    return notes


