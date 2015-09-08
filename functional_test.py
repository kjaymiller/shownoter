from selenium import webdriver
import unittest

#User connects to site
class Shownoter(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('localhost:5000')

    def tearDown(self):
        self.driver.close()
    
    def test_connected_to_right_page(self):
        self.assertEquals('This is a Test', self.driver.title)

#enter text into
    def test_chat_input_returns_content(self):
        chat_text = self.driver.find_element_by_name('chat_text')
        chat_text.send_keys('foo.com')
        chat_text.submit()
        select = self.driver.find_element_by_class_name('results')
        result =  select.get_attribute('innerHTML').strip()
        self.assertEquals("['foo.com']", result)
# fetch_title

# return_link


