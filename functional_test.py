from flask import url_for
from selenium import webdriver
import pytest
#User connects to site

def test_server_is_up_and_running(live_server):
    driver = webdriver.Firefox()
    driver.get('localhost:5000')

def test_server_online(client):
    assert client.get(url_for('index')).status_code == 200

# fetch_title

# return_link


