import pytest
import link

@pytest.fixture
def base_text():
    text = """
#Test1
http://google.com
Test2
This is just text
"""
    return text

@pytest.fixture
def passing_text(base_text):
    text =  [
        "#Test1",
        "http://google.com",
        ]

    return text

@pytest.fixture
def failing_text():
    text = {
        'failing_link': "this is just text",
        'failing_category': "Test2"
    }
    
    return text

def test_link_detection(passing_text, base_text):
    assert link.re_link(base_text) == passing_text

@pytest.fixture
def test_link(base_text):
    test_link = link.Link(base_text)
    return test_link


def test_self_text(test_link, passing_text):
    assert test_link.text == passing_text

def test_set_category(test_link):
    assert test_link.category == "Test1"

def test_links_scrape_links(passing_text):
    pass    

