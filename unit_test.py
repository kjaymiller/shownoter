import pytest

def test_link_scrapes_text():
    from link import re_link 
    links = ('foo.com', 'www.foo.com', 'http://foo.com')
    test_links = map(re_link, links)

    assert (all(test_links))
