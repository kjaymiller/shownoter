"""Test Master Test Module
Centralized Call for Tests for shownoter.co

created: 2015
author: https://github.com/kjaymiller"""

import unittest
import ptshownotes

class TestCategories(unittest.TestCase):
    """tests category functionality in ptshownotes.Shownotes"""
    
    def setUp(self):
        chat = '''
#category1
#category2
#category3
http://google.com'''

        self.test_shownotes = ptshownotes.Shownotes(chat, export_path = 'downloads/')
        
    def test_shownotes_default_category(self):
        """test shownotes class and all variables"""
        assert '#uncategorized' in self.test_shownotes.link_dict.keys()
    
    def test_category_additions(self):
        """tests additions of categories 1,2, and 3"""
        categories = ('#category1', '#category2', '#category3')
        for category in categories:
            self.assertIn(category, self.test_shownotes.link_dict.keys()) 

    def test_delete_link(self):
        category = '#category3'
        link = 'http://google.com'
        assert self.test_shownotes.link_dict[category][link]
        self.test_shownotes.delete_link(category, link)
        self.assertNotIn(link, self.test_shownotes.link_dict[category])


    def test_export(self):
        import os
        filename = self.test_shownotes.export
        assert os.path.isfile('downloads/' + filename)

class TestTextType(unittest.TestCase):
    """verifies error handling of text type so only str() data can be entered"""

    def test_int(self):
        chat_int = int()
        with self.assertRaises(TypeError):
            ptshownotes.Shownotes(chat_int)
    
    def test_list(self):
        chat_list = list()
        with self.assertRaises(TypeError):
            ptshownotes.Shownotes(chat_list)
            
    def test_dict(self):
        chat_dict = dict()
        with self.assertRaises(TypeError): 
            ptshownotes.Shownotes(chat_dict)

if __name__ == '__main__':
    unittest.main()
