import re
from random import randint
from os import remove, path 
import requests
from collections import OrderedDict
from bs4 import BeautifulSoup


def clean_line(line):
    return str().join(c for c in line if ord(c) < 128)

def import_file(notes):
    with open(notes, 'r+') as file:
        return file.read()

class Shownotes():
    def __init__(self, text):
        self.link_dict = OrderedDict()
        self.link_dict['#uncategorized'] = list()
        self.bad_links = list()
        self.md_text = self.snote(text)
        print(self.link_dict)
        self.delete_empty_categories()
    
    def snote(self, chat):
        self.scrape(self.link_detect(chat))
        return self.organize()

    def link_detect(self, chat):
        return re.findall(r'^#.*|\b\S+\.\S+', chat, re.M)
    
    def scrape(self, rlist):
        key = '#uncategorized'
        for line in rlist:
            nline = line.strip()
        
            if nline.startswith('#'):
                key = nline
                self.link_dict[key] = list()
                continue
            
            if not nline.startswith('http'):
                    nline = 'http://' + nline
                    
            try:
                web = requests.get(nline, timeout = 1.5)
                soup = BeautifulSoup(web.content)
                rtitle = clean_line(soup.title.text)
                if (rtitle, nline) not in self.link_dict[key]:
                    self.link_dict[key].append((rtitle, nline))

            except:
                nline = clean_line(nline)
                print(nline, 'failed')
                self.bad_links.append(nline)
    
    def organize(self):
        rstr = str()
        for key in self.link_dict:
            if key == 'bad links':
                continue
            
            print(len(self.link_dict[key]))
            rstr = rstr + '#{}\n'.format(key)
            
            for item in self.link_dict[key]:
                rstr = rstr + '* [{}]({})\n'.format(item[0],item[1])
        
        return rstr
    
    def lpop(self, item, o_list, n_list, new_loc = -1):
        item_loc = self.link_dict[o_list].index(item)
        item = self.link_dict[o_list].pop(item_loc)
        self.link_dict[n_list].insert(new_loc, item)
        self.md_text = self.organize()
  
    def ldel(self, item):
        del self.link_dict[item]
        self.md_text = self.organize()

    def export_shownotes(self):
        file_id = randint(0,65535);
        file = 'static/links{}.md'.format(file_id)
        if path.isfile(file):
            remove(file)
        with open(file, 'w+') as file:
            file.write(self.md_text)

    def delete_empty_categories(self):
        for category in self.link_dict:
            if not self.link_dict[category]:
                print(category, 'is empty')
                del self.link_dict[category]
