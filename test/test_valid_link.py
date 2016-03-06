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
def good_test():
    test_var = 'http://link.com'
    return test_var


def test_link_extracted_from_html(good_test):
    """tests if a link can be found in an html link handler"""
    href = '<a href="{}">some value</a>'.format(good_test)
    assert valid_link.extract_from_html(href) == {
                                                'url': good_test,
                                                'title': 'some value'
                                                }

def test_link_extracted_from_mkdown(good_test):
    """test if a link can be found in a markdown url handler"""
    pass
