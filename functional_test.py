from selenium import webdriver
from flask import url_for
import pytest
#User connects to site
@pytest.mark.usefixtures('live_server')
class TestSiteFunctionality:
    pass

def test_server_online(client):
    assert client.get(url_for('index')).status_code == 200

# fetch_title

# return_link


