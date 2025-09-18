import urllib.request, urllib.parse
import ssl, json

# Ignore SSL/TLS errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('URL: ')
if len(url) < 1 :
    url = 'http://py4e-data.dr-chuck.net/comments_2294097.json'
sitedata = urllib.request.urlopen(url, context=ctx).read()
js = json.loads(sitedata)

counts = list()
for item in js['comments'] :
    counts.append(item['count'])
print(sum(counts))    