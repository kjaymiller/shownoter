import pytest
from app import valid_link


def test_valid_link_parameters():
    assert valid_link.top_level_domains
    assert valid_link.uris


def test_tlds_not_in_check_tld():
    assert 'asdfsdfw' not in valid_link.uris


def test_actual_tld_returns_true():
    assert 'com' in valid_link.top_level_domains


def test_actual_url_return_true():
    assert 'http' in valid_link.uris


@pytest.fixture
def good_link():
    test_var = '<a href="http://link.com">some title</a>'
    return test_var


@pytest.fixture
def good_image():
    test_var = '<img src="image.jpg" alt="some title">'
    return test_var


def test_not_a_detected_returns_false(good_image):
    assert not valid_link.detect_a_in_html(good_image)


def test_a_detected(good_link):
    assert valid_link.detect_a_in_html(good_link)


def test_img_detected(good_image):
    assert valid_link.detect_img_in_html(good_image)


def test_fetch_url_from_html(good_link):
    assert valid_link.detect_url_from_href(good_link) == 'http://link.com'


def test_fetch_link_from_html_returns_None_if_not_found(good_image):
    assert valid_link.detect_url_from_href(good_image) == None


def test_fetch_link_title_from_html(good_link):
    assert valid_link.detect_title_from_a_tag(good_link) == 'some title'


def test_fetch_link_title_returns_None_if_no_url(good_image):
    assert valid_link.detect_title_from_a_tag(good_image) == None


def test_fetch_image_url_from_html(good_image):
    assert valid_link.detect_url_from_img(good_image) == 'image.jpg'


def test_fetch_image_url_from_html_returns_none_if_not_found(good_link):
    assert valid_link.detect_url_from_img(good_link) == None


def test_fetch_image_title_from_html(good_image):
    assert valid_link.detect_title_from_img(good_image) == 'some title'


def test_fetch_image_title_from_html_returns_None_if_not_found(good_link):
    assert valid_link.detect_url_from_img(good_link) == None


def test_render_link_object_from_html(good_link):
    """test if dictionary object is returned with title and url from a tag"""

    assert valid_link.render_link_from_html(good_link) == {
                                                'title': 'some title',
                                                'url': 'http://link.com'
                                                }


def test_render_link_object_from_html_returns_None_if_none_a(good_image):
    """tests if function is tested on a non-A_tag"""

    assert valid_link.render_link_from_html(good_image) == None


def test_render_link_object_from_html_returns_None_if_no_url():
    """tests if function is tested on a non-A_tag"""

    missing_url = '<a>There is no Url</a>'
    assert valid_link.render_link_from_html(missing_url) == None


def test_render_link_object_from_html_reutrns_empty_string_if_no_title():
    """tests in function will complete but return title empty
    if there is no title"""

    missing_title = '<a href="http://link.com"></a>'
    assert valid_link.render_link_from_html(missing_title) == {
                                                    'url': 'http://link.com',
                                                    'title': ''
                                                    }
