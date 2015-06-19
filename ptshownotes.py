import re
import requests
from collections import defaultdict
from bs4 import BeautifulSoup

def lnk_detect(chat):
    return re.findall(r'^#.*|\b\S+\..+\b', chat, re.M)

def scrape(rlist):    
    key = '#uncategorized'
    rdict = defaultdict(list)
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
            rtitle = str().join(c for c in soup.title.text if ord(c)<128)
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

