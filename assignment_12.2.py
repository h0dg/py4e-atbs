import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl # defaults to certificate verification and most secure protocol (now TLS)
import re

# User defined parameters
url = input('Enter - ')
rpt = input('Enter count: ')
pos = input('Enter position: ')
try :
    rpt = int(rpt)
    pos = int(pos)
except :
    print('Please enter a number for Count and Position.')
    quit()

# Function to open link, parse, and return a list of hyperlinks
def parse(url, pos):
    # Ignore SSL/TLS cert errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    lst = list()
    for tag in tags:
        lst.append(tag.get('href', None))
    return lst[pos]
    
i = 0
while i < rpt :
    print('Retrieving:',url)
    url = parse(url, pos - 1)
    i = i + 1
name = re.findall(r'by_([\S]+).html$', url)
print(name[0])