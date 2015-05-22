import re
import urllib.request
from collections import defaultdict
from bs4 import BeautifulSoup

def finder(filename):
    with open(filename,'r') as file:
        return re.findall(r'^>.*', file.read().replace(u'\xa0', u' '), re.M)

def cats(rlist):
    rdict = defaultdict(list)
    key = 'uncategorized'
    for line in rlist:
        nline = line[1:].strip().split(' ',1)
        if not nline[0].startswith('http'):
             nline[0] = 'http://' + nline[0]
        try:
            soup = BeautifulSoup(urllib.request.urlopen(nline[0]))
            rtitle = re.sub('[\n\t]','',str(soup.title)[7:-8].strip())
            if len(nline) == 2:
                key = nline[1]
            rdict[key].append((rtitle,nline[0]))
        except:
            print(nline[0], 'failed') 
    return rdict    

def org(rdict):
    rstr = ''
    for key in rdict:
        rstr = rstr + '#{}\n'.format(key)
        for item in rdict[key]:
            rstr = rstr + '* [{}]({})\n'.format(item[0],item[1])
    return rstr

links = org(cats(finder('raw_pt_ep2.txt')))
print(links)

