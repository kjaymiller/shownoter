"""
Pytest Testing Module
"""

import requests_mock
import pytest
from shownoter import re_link, get_links, get_title, detect_image


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

@pytest.fixture
def code_newbie():
    return str.encode('''
    <html><head><title>CodeNewbie - Test</title></head></html>
   ''')


@requests_mock.Mocker(kw='mock')
def test_url(code_newbie, **kwargs):
    link = 'http://codenewbie.org'
    html = kwargs['mock'].get( link , content = code_newbie)
    result = get_title('http://codenewbie.org')
    
    assert html.called
    assert result == 'CodeNewbie - Test'

# Test Image Detection Class
def test_detect_image_detects_png():
    image = 'foo.png'
    assert detect_image(image)

def test_detect_image_detects_jpg():
    image = 'foo.jpg'
    assert detect_image(image)

def test_detect_image_detects_gif():
    image = 'foo.gif'
    assert detect_image(image) 

def test_detect_image_does_NOT_detect_anything_else():
    not_image = 'foo.bar'
    assert not detect_image(not_image)

@requests_mock.Mocker(kw='mock')
def test_link_title_fetched_url(code_newbie, **kwargs):
    link = 'http://www.codenewbie.org'
    html = kwargs['mock'].get( link , content = code_newbie)
    title = 'CodeNewbie - Test'
    result = get_links(link = link, title=get_title(link))
    assert html.called
    assert result == '[{title}]({link})'.format(title = title, link = link)
