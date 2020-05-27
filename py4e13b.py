import json
import urllib.request, urllib.parse, urllib.error

url = input('Enter location:')
print('Retrieving', url)


info = json.loads(url)
print('Retrieved', len(info), 'characters')

total = 0

for count in info[comment].items() : 
    total = total + int(count[0])

print(total)