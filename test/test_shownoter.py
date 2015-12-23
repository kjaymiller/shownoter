from app import shownoter
import pytest
import requests_mock

@pytest.fixture
def mock_html():
    return '<html><head><title>Test</title></head></html>'

class GetResult(object):
    def __init__(self, url):
        self.status_code = 200
        self.url = url
        self.content = '<html><head><title>Test</title></head></html>'

def mock_get(url):
    return GetResult(url)

# Test link detection

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

# Test that urls are formatted correctly

def test_valid_link_inserts_prefix_if_none(monkeypatch):
    monkeypatch.setattr(shownoter, 'get', mock_get)

    link = shownoter.Link('link.com')
    assert 'http://link.com' == link.url

def test_valid_link_does_nothing_if_prefix_exists(monkeypatch):
    monkeypatch.setattr(shownoter, 'get', mock_get)

    link = shownoter.Link('http://link.com')
    assert 'http://link.com' == link.url

# Test image detection

def test_image_detect_detects_png():
    link = 'link.png'
    assert shownoter.image_detect(link)

def test_image_detect_detects_jpg():
    link = 'link.jpg'
    assert shownoter.image_detect(link)

def test_image_detect_detects_gif():
    link = 'link.gif'
    assert shownoter.image_detect(link)

def test_image_detect_does_not_detect_outside_other_links():
    link = 'link.foo'
    assert not shownoter.image_detect(link)

def test_image_detect_does_not_throw_attribute_error_when_no_extension():
    link = 'https://gist.github.com/anonymous/7e5fa94f6e946551b70a'
    assert not shownoter.image_detect(link)

@requests_mock.Mocker(kw='mock')
def test_title(mock_html, **kwargs):
    link = 'http://link.com'
    html = kwargs['mock'].get(link, text=mock_html)
    sample_link = shownoter.Link(link)
    assert html.called
    assert sample_link.url == 'http://link.com/'
    assert sample_link.title == 'Test'
    assert sample_link.markdown == '* [Test](http://link.com/)'

# Test output formatting

def test_links_to_string():
    test_list = ['pie', 'cake', 'ice cream']
    results = shownoter.links_to_string(test_list)
    assert 'pie\ncake\nice cream\n' == results

# Test Markdown generation

def test_link_markdown():
    link = 'link.com'
    title = 'Test'
    assert '[Test](link.com)' in shownoter.link_markdown(title, link)

def test_image_markdown():
    link = 'link.png'
    title = ''
    assert '![](link.png)' in shownoter.image_markdown(title, link)

# Test formatting functions

def test_format_links_as_hash_returns_a_list_of_three_element_hashes(monkeypatch):
    monkeypatch.setattr(shownoter, 'get', mock_get)

    text = "link.com"
    results = shownoter.format_links_as_hash(text)
    assert 1 == len(results)
    assert "* [Test](http://link.com)" == results[0]["markdown"]
    assert "Test" == results[0]["title"]
    assert "http://link.com" == results[0]["url"]
