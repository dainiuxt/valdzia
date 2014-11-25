#scrap <p class="vv"> (Name) and <p class="vvv"> (position)
from lxml import html
import urllib
import requests
import bs4
from time import sleep # be nice

#get contacts page
contactspage = requests.get('http://president.lt/lt/dbs_kontaktai/printerlist.html')
contactstree = html.fromstring(contactspage.text)
staffname = [el.text for el in contactstree.xpath('//p[@class="vv"]')]
staffposition = [el.text for el in contactstree.xpath('//p[@class="vvv"]')]
team = []
for i in range(max((len(staffname),len(staffposition)))):
	while True:
		try:
			person = (staffname[i],staffposition[i])
		except IndexError:
			if len(staffname)>len(staffposition):
				staffposition.append('')
				person = (staffname[i],staffposition[i])
			elif len(staffname)<len(staffposition):
				staffname.append('')
				person = (staffname[i],staffposition[i])
			continue
		team.append(person)
		break
print(team)
