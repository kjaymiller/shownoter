'''This is the testing file for the ptshownotes.
It checks the regex for crazy types of links'''

from app import ptshownotes


#Testing Variables
text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec a diam lectus. Sed sit amet ipsum mauris. Maecenas congue ligula ac quam viverra nec consectetur ante hendrerit. Donec et mollis dolor. Praesent et diam eget libero egestas mattis sit amet vitae augue. Nam tincidunt congue enim, ut porta lorem lacinia consectetur. Donec ut libero sed arcu vehicula ultricies a non tortor. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean ut gravida lorem. Ut turpis felis, pulvinar a semper sed, adipiscing id dolor. Pellentesque auctor nisi id magna consequat sagittis. Curabitur dapibus enim sit amet elit pharetra tincidunt feugiat nisl imperdiet. Ut convallis libero in urna ultrices accumsan. Donec sed odio eros. Donec viverra mi quis quam pulvinar at malesuada arcu rhoncus. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. In rutrum accumsan ultricies. Mauris vitae nisi at sem facilisis semper ac in est.'''

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
    'bad_link_does_not_exist' : 'http://kjaymiler.coma',
            }

def chk_lnk_detect_success(chat, num):
    print('checking for good links. Expecting {}.'.format(num))
    rlist = ptshownotes.lnk_detect(chat)
    print(str().join(item + '\n' for item in rlist))
    if len(rlist) == num:
        return 'PASS: all links detected'
    else:
        return 'FAIL error detecting links. Only found {}.'.format(len(rlist))

def chk_lnk_detect_fail(chat):
    print('checking for  links. Expecting 0 links.')
    rlist = ptshownotes.lnk_detect(chat)

    if not rlist:
        return 'PASS: 0 links detected'

    else:
        return '''FAIL: A false positive was detected. 
Links were detected that should have not:
{}'''.format(rlist)

def main():


    #Link Detects
    chat = str().join(good_links[x] + '\n' for x in good_links)
    print(chk_lnk_detect_success(chat, len(good_links)))
    print(chk_lnk_detect_fail(text))
    
if __name__ ==  '__main__':
    main()
