import urllib
import urllib2
import os
import sys

url = 'http://166.111.137.13:8077'

lines = sys.stdin.readlines()

d = {}.fromkeys(['snmp'])
d['snmp'] = "".join(lines)
if d['snmp']!="":
	#	print d
	data = urllib.urlencode(d)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
