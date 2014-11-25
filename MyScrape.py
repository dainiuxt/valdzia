#!/usr/bin/python3

import sys, MyParser, httpclient

# try to assign the subdomain and path values
# if the assignment fails, just use default values
try:
	subdomain, path = sys.argv[1:]
#~ except:
	#~ subdomain, path = 'milwaukee', '/eng/'

# instantiate the parser
parser = MyParser.ClParser()

# instantiate the page
page = httpclient.Page(subdomain, path)

# get the page and feed it to the parser
parser.feed(page.get_as_string())

# display the results
print('################\n    Results:\n################\n', parser.results)
