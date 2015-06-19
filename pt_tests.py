'''This is the testing file for the ptshownotes.
It checks the regex for crazy types of links'''

import ptshownotes

#Testing Variables
headers = {
    'header1' : '#header1',
    'header2' : '#header2 is better',
    'header3' : '#header3 has some !@#$%^&*() in it'
            }

good_links = {
   'link' : 'http://kjaymiller.com',
    'redirect' : 'http://www.google.com',
    'no_www' : 'http://google.com',
    'no_html' : 'kjaymiller.com',
    'link_in_sentence' : 'Have you seen kjaymiller.com'
            }

bad_links = {
    'bad_link' : 'httpwwwgooglecom',
    'bad_link_does_not_exist' : 'http://kjaymiler.coma',
    'bad_link_reference' : 'I checked it on google'
            }

def chk_lnk_detect(chat, num):
    print('checking for good links. Expecting {}.'.format(num))
    rlist = ptshownotes.lnk_detect(chat)
    print(str().join(item + '\n' for item in rlist))
    if len(rlist) == num:
        return 'all links detected'
    else:
        return 'error detecting links. Only found {}.'.format(len(rlist))

def main():
    chat = str().join(good_links[x] + '\n' for x in good_links)
    print(chk_lnk_detect(chat, len(good_links)))


if __name__ ==  '__main__':
    main()
