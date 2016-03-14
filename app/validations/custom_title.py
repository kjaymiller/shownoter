"""Detect Links and Title Using Common Separators"""
import re


def detect_link(content):
    search_param = re.compile(r"""[*\-\ ]*
                            (?P<title>.+[^\ \-])
                            (\ ?[:\-]?\ )
                            (?P<url>\S+)""", re.X)
    entry = re.match(search_param, content)

    if entry:
        return entry.groupdict()

    else:
        return None
