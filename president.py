#scrap <p class="vv"> (Name) and <p class="vvv"> (position)
from lxml import html
import requests
import bs4

#get contacts page
presidentr = requests.get('http://president.lt/lt/dbs_kontaktai/printerlist.html')
presidenttree = html.fromstring(presidentr.text)
pr_names = presidenttree.xpath('//p[@class="vv"]/text()')
pr_position = presidenttree.xpath('//p[@class="vvv"]/text()')

print (pr_names)
print (pr_position)
#presidentf = open('president.txt', 'w')
#presfile.encode('utf-8')
#presidentf.write(presidentr.text)
#presidentf.close
