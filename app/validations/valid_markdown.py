"""Module Detects if a line is a valid markdown link reference"""
import re


def detect_markdown(content):
    """function content a single line """

    link = re.search(r'!*\[.*\]\(.+\)', content)
    if link:
        return link.group()
    else:
        return None


def markdown_link_type(content):
    """Determines if the markdown is a standard link or an image"""
    if detect_markdown(content):
        if content[0] == '!':
            return 'image'
        else:
            return 'link'
    else:
        return None
