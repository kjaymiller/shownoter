import shownoter
import pytest

def test_link_detect_finds_link_in_text():
    text = '''This is a test
    to see if our regex
    will find link.com
    and return it'''
    
    assert shownoter.link_detect(text) == ['link.com']
    
