"""
Pytest Testing Module
"""

import requests_mock
import pytest
from shownoter import re_link, get_markdown, validate_link
from shownoter import get_title, detect_image
from shownoter import Link, Image

def test_re_link_detect_http():
    assert re_link('http://google.com')

def test_re_link_not_detect_float():
    assert not re_link('1.2')
    
def test_re_link_not_detect_number_domain():
    assert not re_link('foo.12')

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
    links = 'http://duckduckgo.com is the best'
    result = re_link(links)
    
    assert isinstance(result, list)
    assert len(result) == 1
    assert 'http://duckduckgo.com' in result

@pytest.fixture
def mock_html():
    return '<html><head><title>Test</title></head></html>'

@requests_mock.Mocker(kw='mock')
def test_url(mock_html, **kwargs):
    link = 'http://foo.bar' 
    html = kwargs['mock'].get(link, text=mock_html)
    site = validate_link(link)
    assert html.called
    
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

def test_markdown_for_websites():
    link = 'foo.org'
    title = 'Test'
    result = get_markdown(link = link, title=title)
    assert result == '* [{title}]({link})'.format(title = title, link = link)

def test_markdown_for_images():
    link = 'foo.png'
    title = 'Test'
    result = get_markdown(link = link, title=title, image = True)
    assert result == '* ![{title}]({link})'.format(title = title, link = link)

def test_re_link_returns_prefix_if_necessary():
    link = 'www.foo.org'
    assert re_link(link) == ['http://www.foo.org']

@requests_mock.Mocker(kw='mock')
def test_gets_title_from_url(mock_html, **kwargs):
    link = 'http://foo.bar' 
    html = kwargs['mock'].get(link, text=mock_html)
    site = validate_link(link)
    title = get_title(site)
    assert title == 'Test'
