#scrap <p class="vv"> (Name) and <p class="vvv"> (position)
import requests
import BeautifulSoup

#get contacts page
president_response = requests.get('http://president.lt/lt/dbs_kontaktai/printerlist.html')

print president_response.text
