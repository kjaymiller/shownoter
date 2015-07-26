"""Test Master Test Module
Centralized Call for Tests for shownoter.co

created: 2015
author: https://github.com/kjaymiller"""

import unittest
import ptshownotes
import testing
from supportFiles import cleanStatic

class FunctionTests(unittest.TestCase):
    def test_shownotes_default_category(self):
        """test shownotes class and all variables"""
        chat = str()      
        self.test_shownotes = ptshownotes.Shownotes(chat)   
        assert '#uncategorized' in self.test_shownotes.link_dict.keys()
    
    def test_text_type(self):
        """verifies error handling of text type so only str() data can be entered"""

        
    def test_shownotes_chat_int(self):
        chat_int = int()
        with self.assertRaises(TypeError):
            ptshownotes.Shownotes(chat_int)

    def test_shownotes_chat_list(self):
        chat_list = list()
        with self.assertRaises(TypeError):
            ptshownotes.Shownotes(chat_list)
        
    def test_shownotes_chat_dict(self):
        chat_dict = dict()
        with self.assertRaises(TypeError): 
            ptshownotes.Shownotes(chat_dict)

         
if __name__ == '__main__':
    unittest.main()
