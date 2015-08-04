import pytest
from app.shownotes import shownotes

@pytest.fixture
def shownote():
    shownote = shownotes.Shownotes(
        title = 'Test Shownotes',
        description = 'This is a description for the test shownotes'
        )
    return shownote

def test_create_shownotes_object(shownote):
    assert type(shownote) == shownotes.Shownotes
