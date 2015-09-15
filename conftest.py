import pytest
from app import app as a

@pytest.fixture
def app():
    app = a
    return app
