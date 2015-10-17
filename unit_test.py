import shownoter
import pytest
import requests_mock

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

@pytest.fixture
def mock_html():
    return '<html><head><title>Test</title></head></html>'

@requests_mock.Mocker(kw='mock')
def test_title(mock_html, **kwargs):
    link = 'http://link.com' 
    html = kwargs['mock'].get(link, text=mock_html)
    title = shownoter.title(link)
    assert html.called
    assert title == "Test"

def test_markdown():
    link = 'link.com'
    title = 'Test'
    assert shownoter.markdown(link, title) == '[Test](link.com)'

def test_markdown_if_image():
    link = 'link.png'
    title = ''
    assert shownoter.markdown(link, title) == '![](link.png)'

@requests_mock.Mocker(kw='mock')
def test_title(mock_html, **kwargs):
    link = 'http://link.com' 
    html = kwargs['mock'].get(link, text=mock_html)
    sample_link = shownoter.link(link)
    assert html.called
    assert sample_link['url'] == 'http://link.com'
    assert sample_link['title'] == 'Test'
    assert sample_link['markdown'] == '[Test](http://link.com)'