import urllib.request, urllib.parse
import ssl, json

# Ignore SSL/TLS errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = 'http://py4e-data.dr-chuck.net/opengeo'

while True:
    address = input('Enter location: ')
    if len(address) < 1 : break

    address = address.strip()
    searchparams = dict()
    searchparams['q'] = address

    url = serviceurl+'?'+urllib.parse.urlencode(searchparams)

    print('Retrieving:',url)
    handle = urllib.request.urlopen(url, context=ctx)
    data = handle.read().decode()
    print('Retrieved', len(data), 'characters:')

    try :
        js = json.loads(data)
    except :
        js = None
    
    if not js or 'features' not in js :
        print('==== Download error ====')
        print(data)
        break
    if len(js['features']) < 0 :
        print('=== Object not found ===')
        print(data)
        break

    #print(json.dumps(js['features'][0]['properties'], indent=4))
    reduced = js['features'][0]['properties']
    print(reduced['plus_code'])