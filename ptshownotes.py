import requests
from bs4 import BeautifulSoup
notes = {}

def get_notes(file):
    with open(file,'r') as f:
        key = ''
        for line in f:
            if line.startswith('>'):                
                if '#' in line:
                    val = line[1:line.find(' #')].strip()
                    key = line[line.find('#'):].strip()
                    print(key, val)
                    notes[key] = notes.get(key, [val])
                    if not val in notes[key]:
                        notes[key].append(val) 
                else:
                    val = line[1:line.find(' #')].strip()
                    notes[key] = notes.get(key, [val])
                    if not val in notes[key]:
                        notes[key].append(val)

def compile(notes):
    old_list = list(enumerate([x for x in notes]))
    new_list = []

    print(old_list)
    for x in old_list:
        new_list.append(notes[old_list[int(input('select order: '))][1]])    
    return(new_list)

def build_file(notes):
    with open('sub_'+filename,'a') as file:
        for group in notes:
            file.write(group + '\n')
            for link in notes[group]:
               web = requests.get(link)
               soup = BeautifulSoup(web.content)
               file.write('[{}]({})\n'.format((str(soup.title)[7:-8]),link))
                
filename = input('Name of File: ') + '.txt'
get_notes(filename)
ord_notes = compile(notes)
build_file(notes)
