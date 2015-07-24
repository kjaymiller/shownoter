"""Testing the shownotes.sn_pop() method"""
import ptshownotes

chat = '''
shownoter.co
#category1
google.com
this text should be ignored
#category2
yahoo.com
#category3
duckduckgo.com
bing.com
'''

print('original content')
test = ptshownotes.Shownotes(chat)
print(test.md_text)
a = input()

print('after pop')
test.lpop(test.rdict['#category3'][1], '#category3', '#category2')
print(test.md_text) 
a = input()

print('deleting #category3')
test.ldel('#category3')
print(test.md_text)
a = input()
