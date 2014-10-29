#scrap <p class="vv"> (Name) and <p class="vvv"> (position)
import re
import argparse
#import sys
#sys.setdefaultencoding('utf-8')
from lxml import html
from urllib2 import urlopen
import requests
import bs4
from bs4 import BeautifulSoup

pr_url = 'http://president.lt/lt/dbs_kontaktai/printerlist.html'

def get_pr_contacts():
	#pr_data = {}
	pr_read = requests.get(pr_url)
	pr_soup = bs4.BeautifulSoup(pr_read.text)
	pr_data['Vardas'] = pr_soup.select('p.vv')[0].get_text()
	pr_data['Pareigos'] = pr_soup.select('p.vvv')[0].get_text()

print (pr_data)
	
#prf = open('president.txt', 'w')
#prf.encode('utf-8')
#prf.write(pr_data())
#prf.close
#print('president.txt')
