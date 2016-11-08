import requests
from lxml import html

page = requests.get('http://studentskejedalne.sk')
tree = html.fromstring(page.content)
meals = tree.xpath('//td/text()')

venza = False
for i in meals:
    if "Špagety" in i:
        venza = True
        break

if venza:
    print("YES")
else:
    print ("NO")
