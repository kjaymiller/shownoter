import pytest
from validations import url_parser, valid_link, valid_markdown, valid_html


# url_parser_tests
def test_get_potential_links_detects_standard_links():
    content = 'link.com'
    assert url_parser.get_potential_links(content) == ['link.com']


def test_get_potential_links_detects_markdown_links():
    content = '[test](somelink.com)'
    assert url_parser.get_potential_links(content) == [content]


def test_links_found_in_middle_of_string():
    content = 'the site link.com is a cool site'
    assert url_parser.get_potential_links(content) == ['link.com']


def test_get_potential_links_parses_multiple_lines():
    content = """link.com
    foo.com
    bar.com"""
    assert url_parser.get_potential_links(content) == ['link.com',
                                                       'foo.com',
                                                       'bar.com']


def test_get_potential_links_detects_individual_links():
    content = """
    There are many lines here
    Some have links
    like the next one
    link.com
    there are also floats like 2.3
    and don't forget markdown
    like [test](somelink.com)"""

    assert url_parser.get_potential_links(content) == [
        'link.com',
        '2.3',
        '[test](somelink.com)']


def test_get_potential_links_doesnt_allow_duplicate():
    content = """
    link.com
    link.com
    foo.com
    bar.com
    foo.com"""

    assert url_parser.get_potential_links(content) == [
        'link.com',
        'foo.com',
        'bar.com']


# valid_link_tests
def test_valid_link_parameters():
    assert valid_link.top_level_domains
    assert valid_link.uris


def test_tlds_not_in_check_tld():
    assert 'asdfsdfw' not in valid_link.uris


def test_actual_tld_returns_true():
    assert 'com' in valid_link.top_level_domains


def test_actual_url_return_true():
    assert 'http' in valid_link.uris


# valid_html tests
@pytest.fixture
def good_link():
    test_var = '<a href="http://link.com">some title</a>'
    return test_var


@pytest.fixture
def good_image():
    test_var = '<img src="image.jpg" alt="some title">'
    return test_var


def test_not_a_detected_returns_false(good_image):
    assert not valid_html.detect_href(good_image)


def test_a_detected(good_link):
    assert valid_html.detect_href(good_link)


def test_img_detected(good_image):
    assert valid_html.detect_img(good_image)


def test_fetch_url_from_html(good_link):
    assert valid_html.detect_href_url(good_link) == 'http://link.com'


def test_detect_href_url_html_returns_None_if_not_found(good_image):
    assert valid_html.detect_href_url(good_image) == None


def test_detect_href(good_link):
    assert valid_html.detect_href_title(good_link) == 'some title'


def test_fetch_link_title_returns_None_if_no_url(good_image):
    assert valid_html.detect_href_title(good_image) == None


def test_fetch_image_url_from_html(good_image):
    assert valid_html.detect_img_url(good_image) == 'image.jpg'


def test_fetch_image_url_from_html_returns_none_if_not_found(good_link):
    assert valid_html.detect_img_url(good_link) == None


def test_fetch_image_title_from_html(good_image):
    assert valid_html.detect_img_title(good_image) == 'some title'


def test_fetch_image_title_from_html_returns_None_if_not_found(good_link):
    assert valid_html.detect_img_url(good_link) == None


def test_render_link_object_from_html(good_link):
    """test if dictionary object is returned with title and url from a tag"""

    assert valid_html.render_href_link(good_link) == {
                                                'title': 'some title',
                                                'url': 'http://link.com'
                                                }


def test_render_link_object_from_html_returns_None_if_none_a(good_image):
    """tests if function is tested on a non-A_tag"""

    assert valid_html.render_href_link(good_image) == None


def test_render_link_object_from_html_returns_None_if_no_url():
    """tests if function is tested on a non-A_tag"""

    missing_url = '<a>There is no Url</a>'
    assert valid_html.render_href_link(missing_url) == None


def test_render_link_object_from_html_returns_empty_string_if_no_title():
    """tests in function will complete but return title empty
    if there is no title"""

    missing_title = '<a href="http://link.com"></a>'
    assert valid_html.render_href_link(missing_title) == {
                                                    'url': 'http://link.com',
                                                    'title': ''
                                                    }


# valid_markdown_tests
@pytest.fixture
def good_mkdown_link():
    return '[some title](http://link.com)'


@pytest.fixture
def good_mkdown_image():
    return '![some title](http://link.com)'


def test_detect_markdown(good_mkdown_link):
    """Tests wether the markdown is detected in the string."""
    assert valid_markdown.detect_markdown(good_mkdown_link) == good_mkdown_link


def test_markdown_link_type_detects_link(good_mkdown_link):
    assert valid_markdown.markdown_link_type(good_mkdown_link) == 'link'


def test_markdown_link_type_detects_images(good_mkdown_image):
    assert valid_markdown.markdown_link_type(good_mkdown_image) == 'image'


def test_markdown_link_type_returns_None_if_neither_link_or_image():
    assert valid_markdown.markdown_link_type('foo') == None
