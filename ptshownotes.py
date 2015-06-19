import re
import requests
from collections import defaultdict
from bs4 import BeautifulSoup

def finder(filename):
    with open(filename,'r', encoding = 'utf8') as file:
        return re.findall(r'^#.*|^\S+\..+\b', file.read(),re.M)
        
        #Need to make some tests for this regex
        
def cats(rlist):
    rdict = defaultdict(list)
    key = 'uncategorized'
    
    for line in rlist:
        nline = line.strip()
        
        if nline.startswith('#'):
            key = nline
            continue
        
        elif not nline.startswith('http'):
                nline = 'http://' + nline
                
        try:
            web = requests.get(nline)
            soup = BeautifulSoup(web.content)
            rtitle = str().join(c for c in soup.title.text if ord(i)<128)
            rdict[key].append((rtitle,nline))
            
        except:
            print(nline, 'failed')
    
    return rdict

def org(rdict):
    rstr = str()
    for key in rdict:
        rstr = rstr + '#{}\n'.format(key)
        
        for item in rdict[key]:
            rstr = rstr + '* [{}]({})\n'.format(item[0],item[1])
    
    return rstr

notes = finder('test.txt')
links = org(cats(notes))
print(links)
