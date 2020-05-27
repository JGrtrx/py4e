import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

serviceurl = 'http://py4e-data.dr-chuck.net/json?'

while True :
    address = input('Enter location:')
    if len(address) < 1 : break
    
    parms = dict()
    parms['address'] = address
    parms['key'] = 42
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    
    data = uh.read()
    print('Retrieved', len(data), 'characters')
    
    try: 
        js = json.loads(data)
    except: 
        js = None
    
    if not js or 'status' not in js or js['status'] != 'OK' :
        print('====Failure to Retrieve====')
        print(data)
        continue
    
    loca_id = js["results"][0]["place_id"]
    print('Place_id:', loca_id)
