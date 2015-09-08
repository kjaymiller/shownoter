from selenium import webdriver
import pytest

#User connects to site
driver = webdriver.Firefox()
driver.get('localhost:5000')
assert driver.title == 'This is a Test'
# detect_extensions

# fetch_title

# return_link


driver.close()
