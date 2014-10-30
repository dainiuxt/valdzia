#scrap <p class="vv"> (Name) and <p class="vvv"> (position)
from lxml import html
import requests
import bs4
from time import sleep # be nice

#get contacts page
presidentr = requests.get('http://president.lt/lt/dbs_kontaktai/printerlist.html')
presidenttree = html.fromstring(presidentr.text)
pr_names = presidenttree.xpath('//p[@class="vv"]/text()')
pr_position = presidenttree.xpath('//p[@class="vvv"]/text()')
sleep(1)

def extract_pr_staff(pr_names, pr_position):
	pr_staff = []
	maxnum = len(pr_names)
	for i in range(maxnum):
		pr_staff.append(zip(pr_names[i], pr_position[i]))
	return pr_staff
	print(pr_staff)

if __name__ == '__main__':
    extract_pr_staff(pr_names, pr_position)
#~ print (pr_names)
#~ print (pr_position)
