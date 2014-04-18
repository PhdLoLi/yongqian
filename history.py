#!/usr/bin/python
# -*- coding:utf8 -*-
#top read all the routers and ports from now to 2min ago
#author:Loli Wang

import os
import sys
import datetime

def allRouter(path):
    if len(sys.argv) > 1:
	    step = int(sys.argv[1])
    else:
	    step = 50

    endtime = datetime.datetime.now()
    starttime = endtime - datetime.timedelta(days=step)
    endtime = endtime.strftime('%Y%m%d%H%M')
    starttime = starttime.strftime('%Y%m%d%H%M')
    print starttime + "~" + endtime
    
    routers = os.listdir(path)
    for r in routers:
        if(os.path.isdir(path + '/' + r)):
            if(r[0] == '.'):
                pass
            else:
		ports = os.listdir(path + '/' + r)
	#	print r
		#print ports
		for p in ports:
			if(os.path.isdir(path + '/' + r + '/' + p)):
				if(p[0] == '.'):
					pass
				else:
					os.system('/home/www/IPv6mon/snmpmon/bin/dat2txt %s %s %s %s |python history2.py'%(r,p,starttime,endtime))

if __name__ == '__main__':
	allRouter('/home/www/IPv6mon/snmpmon/dat')
    #print '总文件数 =', allFileNum
