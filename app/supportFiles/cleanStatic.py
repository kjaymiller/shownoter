import logging
from os import remove
from os import listdir

def grab_files(dir, extension):
    '''Gets Directory and returns as list'''
    file_list = [file for file in listdir(dir) if file.endswith(extension)]
    if len(file_list):
        logging.debug('''Files found:
{}'''.format(file_list))
    else:
        logging.info('No Files Found')
        return 
    return file_list

def remove_files(dir,file_list):
    '''removes files in list'''
    if file_list:
        for file in file_list:
            remove('{0}{1}'.format(dir, file))
            logging.debug(file, 'removed')

    
