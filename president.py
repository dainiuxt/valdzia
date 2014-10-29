import re
import argparse
from lxml import html
import requests
import bs4
from bs4 import BeautifulSoup
from time import sleep

pr_url = 'http://president.lt/lt/dbs_kontaktai/printerlist.html'
pr_data = {}
pr_read = requests.get(pr_url)
pr_soup = bs4.BeautifulSoup(pr_read.text)
pr_data['Vardas'] = pr_soup.select('p.vv')[0].get_text()
pr_data['Pareigos'] = pr_soup.select('p.vvv')[0].get_text()
print (pr_data)
sleep(1)
