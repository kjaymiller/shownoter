import logging
import ptshownotes
from testing import lorem
from supportFiles import cleanStatic

logger = logging.getLogger('testing_main')
#logging.basicConfig(level = logging.DEBUG)
logging.basicConfig(level = logging.INFO)

### TEST the TEST ###
logging.debug('testing set to at least debug')
logging.info('testing set to at least info')

logging.info('Testing the output upload')
with open('testing/test_input.txt', 'r+') as file:
    file = file.read()
logging.info('SUCCESS: Output upload complete')

logging.info('Testing create shownotes class object')
test_shownotes = ptshownotes.Shownotes(file)
print(test_shownotes.md_text)
logging.info('SUCCESS: Shownotes class created.')

logging.info('Testing export shownotes class object')

test_count = 0
while test_count < 100:
    export_shownotes = test_shownotes.export_shownotes()
    test_count += 1
    
dir = 'static/'
extension = '.md'

###Testing Clean Static###
file_list = cleanStatic.grab_files(dir, extension)
cleanStatic.remove_files(dir, file_list)
file_list = cleanStatic.grab_files(dir, extension)
