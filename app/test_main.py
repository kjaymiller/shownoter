"""Test Master Test Module
Centralized Call for Tests for shownoter.co

created: 2015
author: https://github.com/kjaymiller"""

import unittest
import ptshownotes
import testing
from supportFiles import cleanStatic

class FunctionTests(unittest.TestCase):
    """Unit Test Root"""
    def setUp(self):
        with open('testing/test_input.txt', 'r+') as file:
            chat = file.read()        
        self.test_shownotes = ptshownotes.Shownotes(chat)   
    def test_shownotes_default_category(self):
        """test shownotes class and all variables"""
        assert '#uncategorized' in self.test_shownotes.link_dict.keys()
        
if __name__ == '__main__':
    unittest.main()
