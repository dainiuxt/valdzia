#scrap <p class="vv"> (Name) and <p class="vvv"> (position)
import requests
import bs4

#get contacts page
pres_response = requests.get('http://president.lt/lt/dbs_kontaktai/printerlist.html')
presfile = open('president.txt', 'w')
#presfile.encode('utf-8')
presfile.write(pres_response.text)
presfile.close
