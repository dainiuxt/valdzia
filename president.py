#scrap <p class="vv"> (Name) and <p class="vvv"> (position)
from lxml import html
import requests
import bs4
from bs4 import BeautifulSoup

president_data = {}
president_url = 'http://president.lt/lt/dbs_kontaktai/printerlist.html'
president_read = requests.get(president_url) #response
president_soup = bs4.BeautifulSoup(president_read.text)
president_data['Vardas'] = president_soup.select('p.vv')#.get.text()
president_data['Pareigos'] = president_soup.select('p.vvv')#.get.text()
#president_tree = html.fromstring(president_read.text)
#president_names = president_tree.xpath('//p[@class="vv"]/text()')
#president_position = president_tree.xpath('//p[@class="vvv"]/text()')
#president_names.extend(president_position)
print (president_data)

	
#presidentf = open('president.txt', 'w')
#presfile.encode('utf-8')
#presidentf.write(presidentr.text)
#presidentf.close
