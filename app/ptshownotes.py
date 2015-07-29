import re
from random import randint
import os
import requests
from collections import OrderedDict
from bs4 import BeautifulSoup

def clean_line(line):
    return str().join(c for c in line if ord(c) < 128)

class Shownotes():
    def __init__(self, text, export_path = 'app/downloads/'):
        if type(text) != type(str()):
            raise TypeError('{} found. Looking for "str()"'.format(type(text))) 
       
        self.link_dict = OrderedDict()
        self.link_dict['#uncategorized'] = OrderedDict()
        self.bad_links = list()
        self.md_text = self.shownote(text)
        self.export = self.export_shownotes(export_path) 

    def shownote(self, chat):
        self.scrape(self.link_detect(chat))
        return self.organize()

    def link_detect(self, chat):
        return re.findall(r'^#.*|\b\S+\.\S+', chat, re.M)
    
    def scrape(self, rlist):
        category = '#uncategorized'
        for line in rlist:
            nline = line.strip()
        
            if nline.startswith('#'):
                category = nline
                self.link_dict[category] = OrderedDict()
                continue
            
            if not nline.startswith('http'):
                    nline = 'http://' + nline
                    
            try:
                web = requests.get(nline, timeout = 1.5)
                soup = BeautifulSoup(web.content)
                rtitle = clean_line(soup.title.text)
                if nline not in self.link_dict[category].keys():
                    self.link_dict[category][nline] = rtitle

            except:
                nline = clean_line(nline)
                print(nline, 'failed')
                self.bad_links.append(nline)
    
    def organize(self):
        rstr = str()
        for category in self.link_dict:
            if category == 'bad links':
                continue
            
            rstr = rstr + '#{}\n'.format(category)
            
            for link in self.link_dict[category]:
                rstr = rstr + '* [{}]({})\n'.format(self.link_dict[category][link], link)
        
        return rstr
    
    def pop_link(self, item, o_list, n_list, new_loc = -1):
        item_loc = self.link_dict[o_list].index(item)
        item = self.link_dict[o_list].pop(item_loc)
        self.link_dict[n_list].insert(new_loc, item)
        self.md_text = self.organize()
  
    def delete_link(self, category, item):
        del self.link_dict[category][item]
        self.md_text = self.organize()

    def export_shownotes(self, path):
        file_id = randint(0,65535);
        filename = 'links{}.md'.format(file_id)
        file_path = path + filename
        if os.path.isfile(file_path):
            os.remove(file_path)
        with open(file_path, 'w+') as file:
            file.write(self.md_text)
        return filename        

    def delete_empty_categories(self):
        for category in self.link_dict:
            if not self.link_dict[category]:
                del self.link_dict[category]
                cat_count += 1
        print(self.link_dict)
                
