from selenium import webdriver
import pytest
#User connects to site

@pytest.fixture
def web_driver():
    driver = webdriver.Firefox()
    driver.get('localhost:5000')
    def addfinalizer():
        driver.close()
    return driver

def test_image(web_driver):
    element = web_driver.find_element_by_id('chat_text')
    element.send_keys('http://cdn.gifbay.com/2015/07/monkeysgifscritterslimes-177906.gif')
    element.submit()
    results = web_driver.find_element_by_class_name('results').text
    assert results == '* ![](http://cdn.gifbay.com/2015/07/monkeysgifscritterslimes-177906.gif)'
# fetch_title


