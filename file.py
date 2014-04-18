import urllib
import urllib2
import os

url = 'http://master:8080'

f = open('me.txt')
lines = f.readlines()
f.close
l_list = lines[6:]

for l in l_list:
	records = l.split()
	d = {}.fromkeys(['time', 'Octs_in', 'Pkts_in', 'Octs_out', 'Pkts_out'])
	#wordcount = len(records)
	#print 'wordcount', wordcount
	d['time'] = records[0]
	d['Octs_in'] = records[1]
	d['Pkts_in'] = records[2]
	d['Octs_out'] = records[3]
	d['Pkts_out'] = records[4]
	print d
	print records
	test = ""
	test = test + "("+records[0]+","+records[1]+","+records[2]+","+records[3]+","+ records[4]+")"
	print test
#	os.system('impala-shell.sh -i master -d snmp -q "insert into dat partition(router=\'202.112.36.20\', port=114) values %s"'%test)
	data = urllib.urlencode(d)
	req = urllib2.Request(url, data)
	response = urllib2.urlopen(req)
