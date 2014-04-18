#!/usr/bin/python
# -*- coding:utf8 -*-
#top read all the routers and ports from now to 2min ago
#author:Loli Wang

import os
import sys
import datetime

def allRouter(path):
    '''
    打印一个目录下的所有文件夹和文件
    '''
    if len(sys.argv) > 1:
	    step = int(sys.argv[1])
    else:
	    step = 2

    endtime = datetime.datetime.now()
    starttime = endtime - datetime.timedelta(minutes=step)
    endtime = endtime.strftime('%Y%m%d%H%M')
    starttime = starttime.strftime('%Y%m%d%H%M')
    print starttime + "~" + endtime
    portnum = 0;
    routernum = 0;
    routers = os.listdir(path)
    for r in routers:
        if(os.path.isdir(path + '/' + r)):
            if(r[0] == '.'):
                pass
            else:
		routernum = routernum + 1
		ports = os.listdir(path + '/' + r)
	#	print r
		#print ports
		for p in ports:
			if(os.path.isdir(path + '/' + r + '/' + p)):
				if(p[0] == '.'):
					pass
				else:
#					os.system('/home/www/IPv6mon/snmpmon/bin/dat2txt %s %s %s %s |python me.py'%(r,p,starttime,endtime))
					portnum = portnum + 1

    print routernum
    print portnum
if __name__ == '__main__':
	allRouter('/home/www/IPv6mon/snmpmon/dat')
    #print '总文件数 =', allFileNum
