# Extracting Data from XML
import urllib.request
import xml.etree.ElementTree as ET

url = 'http://py4e-data.dr-chuck.net/comments_373070.xml'
response = urllib.request.urlopen(url)
tree = ET.fromstring(response.read())
total = sum([int(count.text) for count in tree.findall('comments/comment/count')])
print(total)
