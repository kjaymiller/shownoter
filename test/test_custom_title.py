"""Testing the functionality of app/validations/custom_title.py"""
import pytest
from app.validations import custom_title


@pytest.fixture
def detected_items():
    correct_result = {
        'url': 'link.com',
        'title': 'Some Value'}
    return correct_result


def test_detect_custom_link_finds_url(detected_items):
    assert custom_title.detect_link('Some Value - link.com') == detected_items


def test_detect_custom_link_returns_None_if_no_space_dash():
    assert custom_title.detect_link('this should return None') == None


def test_detect_custom_title_finds_dash_left_space(detected_items):
    assert custom_title.detect_link('Some Value -link.com') == detected_items


def test_detect_custom_title_finds_dash_right_space(detected_items):
    assert custom_title.detect_link('Some Value- link.com') == detected_items


def test_detect_custom_title_finds_colon(detected_items):
    assert custom_title.detect_link('Some Value : link.com') == detected_items


def test_detect_custom_title_finds_colon_left_space(detected_items):
    assert custom_title.detect_link('Some Value: link.com') == detected_items
