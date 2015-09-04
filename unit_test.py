import pytest
from link import re_link

def test_link_scrapes_text():
    links = ('foo.com', 'www.foo.com', 'http://foo.com')
    test_links = map(re_link, links)

    assert all(test_links)

def test_links_doesnt_detect_link():
    not_links = ('google dot com', 'foo bar', 'This is a serious one. It should not detect sentences')
    test_links = map(re_link, not_links)

    assert not any(test_links)
