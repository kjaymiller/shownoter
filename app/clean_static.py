from os import remove
from os import listdir

###Get Static Directory###
def grab_files(dir, extension):
    file_list = [file for file in listdir(dir) if file.endswith(extension)]
    if len(file_list):
        print(file_list)
    else:
        print('Print No Files Found')
        return 
    return file_list

dir = 'static/'
extension = '.md'

file_list = grab_files(dir, extension)

###Remove if files are .md###
if file_list:
    for file in file_list:
        remove('static/{}'.format(file))
        print(file, 'removed')

file_list = grab_files(dir, extension)
    
