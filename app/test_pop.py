"""Testing the shownotes.sn_pop() method"""
import ptshownotes

chat = '''
shownoter.com
#category1
google.com
this text should be ignored
#category2
yahoo.com
#category3
duckduckgo.com
'''

test = ptshownotes.Shownotes(chat)

print(test.md_text)
