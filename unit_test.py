import pytest
from link import re_link

def test_re_link_detect_http():
    assert re_link('http://google.com')
    
def test_re_link_detect_https():
    assert re_link('https://google.com')

def test_re_link_detect_www():  
    assert re_link('www.google.com')

def test_re_link_detect_dot_text():
    assert re_link('a.bc')

def test_re_link_does_not_detect_strings_without_periods():
    assert not re_link('google dot com')

def test_re_link_does_not_detect_sentences_using_proper_grammar():
    assert not re_link('This is a serious one. It should not detect sentences')

def test_re_link_detects_multiple_lines():
    links = 'google.com\ntwitter.com'
    assert len(re_link(links)) == 2

def test_re_link_only_detects_links_and_nothing_else():
    links = 'duckduckgo.com is the best'
    assert re_link(links) == 'duckduckgo.com'
