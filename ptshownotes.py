import re
import requests
from collections import defaultdict
from bs4 import BeautifulSoup

def find_links(filename):
    with open(filename,'r') as file:
        return re.findall(r'^#.*|^\S+\..*', file.read(), re.M)

def get_links(rlist):
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
            soup = BeautifulSoup(requests.get(nline).content)
            rtitle = re.sub('[\n\t]','',str(soup.title)[7:-8].strip())
            rdict[key].append((rtitle,nline))
        except:
            print(nline, 'failed') 

    return rdict    

def create_markdown(rdict):
    rstr = ''

    for key in rdict:
        rstr = rstr + '#{}\n'.format(key)
        for item in rdict[key]:
            rstr = rstr + '* [{}]({})\n'.format(item[0],item[1])

    return rstr

##############################################################

links = create_markdown(get_links(find_links(input('Enter a Filename: '))))
print(links)

