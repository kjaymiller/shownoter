import re
import urllib.request
from collections import defaultdict
from bs4 import BeautifulSoup

def finder(filename):
    with open(filename,'r') as file:
        return re.findall(r'^#.*|^\S+\..*',file.read().replace(u'\xa0', u' '),re.M)
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
            soup = BeautifulSoup(urllib.request.urlopen(nline))
            rtitle = re.sub('[\n\t]','',str(soup.title)[7:-8].strip())
            rdict[key].append((rtitle,nline))
        except:
            print(nline, 'failed') 
    return rdict    

def org(rdict):
    rstr = ''
    for key in rdict:
        rstr = rstr + '#{}\n'.format(key)
        for item in rdict[key]:
            rstr = rstr + '* [{}]({})\n'.format(item[0],item[1])
    return rstr

links = org(cats(finder('test.txt')))
print(links)

