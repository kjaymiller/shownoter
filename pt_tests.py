'''This is the testing file for the ptshownotes.
It checks the regex for crazy types of links'''

import ptshownotes

#Testing Variables
headers = {
    header1 : '#header1',
    header2 : '#header2 is better',
    header3 : '#header3 has some !@#$%^&*() in it'
            }

good links = {
    good_link : http://kjaymiller.com,
    good_link_redirect : 'http://www.google.com',
    good_link_no_www : 'http://google.com',
    good_link_no_html : 'kjaymiller.com',
    good_link_in_sentence : 'Have you seen kjaymiller.com?'
            }

bad links = {
    bad_link : 'httpwwwgooglecom',
    bad_link_does_not_exist : 'http://kjaymiler.coma'
    bad_link_reference = 'I checked it on google?'

just_text = '''The Testing Goat is the unofficial mascot of TDD in the Python testing community. It probably means different things to different people, but, to me, the Testing Goat is a voice inside my head that keeps me on the True Path of Testing, like one of those little angels or demons that pop up above your shoulder in the cartoons, but with a very niche set of concerns. I hope, with this book, to install the Testing Goat inside your head too.
We've decided to build a website, even if we're not quite sure what it's going to do yet. Normally the first step in web development is getting your web framework installed and configured. Download this, install that, configure the other, run the script but TDD requires a different mindset. When you're doing TDD, you always have the Testing Goat inside you single-minded as goats are Test first, test first!

In TDD the first step is always the same: write a test.'''

#TODO Create Tests
