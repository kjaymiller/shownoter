"""Testing the functionality of app/validations/custom_title.py"""
import pytest
from app.validations import custom_title


@pytest.fixture
def dash():
    return "Some Value - link.com"


def test_detect_custom_title_finds_url(dash):
    assert custom_title.detect_custom_title(dash)['url'] == 'link.com'


def test_detect_custom_title_finds_title(dash):
    assert custom_title.detect_custom_title(dash)['title'] == 'Some Value'


def test_detect_custom_title_returns_None_if_no_space_dash(dash):
    assert custom_title.detect_custom_title('this should return None') == None
