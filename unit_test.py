import shownoter
import pytest

def test_link_detect_finds_one_link_text():
    sample_text = '''This is a test
    to see if our regex
    will find link.com
    and return them both'''
    assert shownoter.link_detect(sample_text) == ['link.com']

def test_link_detect_finds_multiple_links():
    sample_text = '''This is a test
    to see if our regex
    will find link.com
    and link.net
    and foo.bar
    and returns them all'''
    assert shownoter.link_detect(sample_text) == ['link.com', 'link.net', 'foo.bar']


def test_valid_link_inserts_prefix_if_none():
    assert shownoter.valid_link('link.com') == 'http://link.com'  

def test_valid_link_does_nothing_if_prefix_exists():
    assert shownoter.valid_link('http://link.com') == 'http://link.com'