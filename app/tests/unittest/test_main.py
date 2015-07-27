"""Test Master Test Module
Centralized Call for Tests for shownoter.co

created: 2015
author: https://github.com/kjaymiller"""

import unittest
import ptshownotes

class test_categories(unittest.TestCase):
    """tests category functionality in ptshownotes.Shownotes"""
    
    def setUp(self):
        chat = '''
#category1
#category2
#category3 '''
        self.test_shownotes = ptshownotes.Shownotes(chat)
        print(self.test_shownotes.link_dict.keys())
        
    def test_shownotes_default_category(self):
        """test shownotes class and all variables"""
        assert '#uncategorized' in self.test_shownotes.link_dict.keys()
    
    def test_category_additions(self):
        """tests additions of categories 1,2, and 3"""
        categories = ('#category1', '#category2', '#category3')
        for category in categories:
            self.assertIn(category, self.test_shownotes.link_dict.keys()) 
    
class testTextType(unittest.TestCase):
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

class testFileExport(unittest.TestCase):
    """Can files be exported using ptshownotes.export_file"""
    def setUp(self):
        chat = 'http://google.com'
        self.test_shownotes = ptshownotes.Shownotes(chat)

    def test_export(self):
        import os
        assert os.path.isfile(self.test_shownotes.export)
if __name__ == '__main__':
    unittest.main()
