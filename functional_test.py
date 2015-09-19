from selenium import webdriver
import pytest
#User connects to site

def test_driver():
    driver = webdriver.Firefox()
    driver.get('localhost:5000')
    element = driver.find_element_by_id('chat_text')
    element.send_keys('http://cdn.gifbay.com/2015/07/monkeysgifscritterslimes-177906.gif')
    element.submit()
    results = driver.find_element_by_class_name('results').text
    driver.close()
    assert '* ![](http://cdn.gifbay.com/2015/07/monkeysgifscritterslimes-177906.gif)' == results
# fetch_title

# return_link


