import urllib
import urllib2
import os
import sys

url = 'http://166.111.137.13:8066'


d = {}.fromkeys(['data'])
d['data'] = "".join("haha")
if d['data']!="":
	print d
	data = urllib.urlencode(d)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
