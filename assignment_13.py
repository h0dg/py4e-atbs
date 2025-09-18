import xml.etree.cElementTree as ET 
import urllib.request, urllib.parse, urllib.error
import ssl

# Ignore SSL/TLS errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')
xml = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(xml)

counts = tree.findall('.//count')
nums = list()
for results in counts:
    num = int(results.text)
    nums.append(num)
print(sum(nums))