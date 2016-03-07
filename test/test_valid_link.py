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
    assert valid_link.detect_url_from_html(good_link) == 'http://link.com'


def test_fetch_url_returns_None_if_no_url():
    assert valid_link.detect_url_from_html(good_image) == None


def test_fetch_title_from_html(good_link):
    assert valid_link.detect_a_title_in_html(good_link) == 'some title'


def test_fetch_title_returns_None_if_no_url():
    assert valid_link.detect_a_title_in_html(good_image) == None
