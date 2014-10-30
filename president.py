# create virtual python3  environment:
# source py3env/bin/activate

import re
import argparse
import requests
import bs4
from multiprocessing.pool import ThreadPool as Pool
from time import sleep

pr_url = 'http://president.lt/lt/dbs_kontaktai/printerlist.html'

#get contacts data from president.lt
def get_pr_contacts_data():
	pr_data = {}
	pr_response = requests.get(pr_url)
	pr_soup = bs4.BeautifulSoup(pr_response.text)
	pr_data['Vardas'] = pr_soup.selectAll('p.vv')[0].get_text()
	pr_data['Pareigos'] = pr_soup.selectAll('p.vvv')[0].get_text()
	return pr_data
	sleep(1)
	
#print (pr_data)
def show_pr_data():
	results = get_pr_contacts_data
	print (results)
	print(u'Vardas, Pareigos')
	print(u'{0},{1}'.format(results[i]['Vardas'], ', '.join(results[i]['Pareigos'])))

if __name__ == '__main__':
    show_pr_data()
