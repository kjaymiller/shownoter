import logging
import lorem
import ptshownotes

logger = logging.getLogger('testing_main')
#logging.basicConfig(level = logging.DEBUG)
logging.basicConfig(level = logging.INFO)

### TEST the TEST ###
logging.debug('testing set to at least debug')
logging.info('testing set to at least info')

logging.info('Testing the output upload')
with open('test_input.txt', 'r+') as file:
    file = file.read()
logging.info('SUCCESS: Output upload complete')

logging.info('Testing create shownotes class object')
test_shownotes = ptshownotes.Shownotes(file)
print(test_shownotes.md_text)
logging.info('SUCCESS: Shownotes class created.')
