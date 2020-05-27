# Following Links with BeautifulSoup
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

n = input('Enter number of cycles')
m = input('Enter position')
url = 'http://py4e-data.dr-chuck.net/known_by_Cailyne.html'
count = n + 1
pos = m
new = url

while n < count :
    if new == url : 
        html = urllib.request.urlopen(url, context=ctx).read()
        print('Retrieving', url)
    html = urllib.reqest.urlopen(new, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    my_tags = tags[pos - 1]
    new = my_tags.get('href', None)
    print('Retrieving', new)
    n = n + 1
