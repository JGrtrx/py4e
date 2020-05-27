from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'http://py4e-data.dr-chuck.net/comments_373068.html'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

tags = soup('a')
num = list()
for tag in tags :
    tag.strip()
    gotit = re.findall('<span ([0-9]+)', tag)
    num.append(int(gotit[0]))
    
print(sum(num))