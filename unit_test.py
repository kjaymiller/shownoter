"""
Pytest Testing Module
"""

import requests_mock
import pytest
from shownoter import re_link, get_links, get_title


def test_re_link_detect_http():
    assert re_link('http://google.com')
    
def test_re_link_detect_https():
    assert re_link('https://google.com')

def test_re_link_detect_www():  
    assert re_link('www.google.com')

def test_re_link_detect_dot_text():
    assert re_link('a.bc')

def test_re_link_does_not_detect_strings_without_periods():
    assert not re_link('google dot com')

def test_re_link_does_not_detect_sentences_using_proper_grammar():
    assert not re_link('This is a serious one. It should not detect sentences')

def test_re_link_detects_multiple_lines():
    links = 'google.com\ntwitter.com'
    assert len(re_link(links)) == 2

def test_re_link_only_detects_links_and_nothing_else():
    links = 'duckduckgo.com is the best'
    result = re_link(links)
    
    assert isinstance(result, list)
    assert len(result) == 1
    assert 'duckduckgo.com' in result

# Test Link class
@requests_mock.Mocker(kw='mock')
def test_link_title_fetched_url(**kwargs):
    link = 'http://codenewbie.org'
    kwargs['mock'].get( link , content = str.encode('''
    <html><head><title>CodeNewbie - Test</title></head></html>
    '''))
    result = get_title(link)
    assert kwargs['mock'].called
    assert result == 'CodeNewbie - Test'

# Test Image Detection Class
def test_get_links_detects_png():
    image = 'foo.png'
    assert get_links(image) == '![]({})'.format(image)

def test_get_links_detects_jpg():
    image = 'foo.jpg'
    assert get_links(image) == '![]({})'.format(image)

def test_get_links_detects_gif():
    image = 'foo.gif'
    assert get_links(image) == '![]({})'.format(image)

@requests_mock.Mocker(kw='mock')
def test_link_title_fetched_url(**kwargs):
    link = 'http://codenewbie.org'
    kwargs['mock'].get( link , content = str.encode('''
    <html><head><title>CodeNewbie - Test</title></head></html>
    '''))
    title = get_title(link)
    result = get_links(link = link, title = title)
    assert kwargs['mock'].called
    assert result == '[{title}]({link})'.format(title = title, link = link)
