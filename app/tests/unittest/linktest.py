import pytest
from app.shownotes import link

def test_clean_line_chars():
    for char in range(32,129):
        char = link.clean_line(ord(char))
        assert char = ord(char)
    
@pytest.fixture
def link():
    link = link.Link('http://google.com')
    