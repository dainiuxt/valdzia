from lxml import html
import requests
from skylark import Database, Model, Field

#~ database connection
Database.config(db='valdzia', user='valdzia_py', passwd='123456')

class employees(Model):
	name = Field()
	position = Field()

#~ get contacts page
contactspage = requests.get('http://president.lt/lt/dbs_kontaktai/printerlist.html')
contactstree = html.fromstring(contactspage.text)

#~  Get staff names and positions from contacts page
staffname = [el.text or ' ' for el in contactstree.xpath('//p[@class="vv"]')]
staffposition = [el.text or ' ' for el in contactstree.xpath('//p[@class="vvv"]')]

#~ Write staff information to database
employees.create(name=staffname[i],position=staffposition[i])
