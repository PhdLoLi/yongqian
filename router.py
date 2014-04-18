#!/usr/bin/python
# -*- coding:utf8 -*-
#author: loli wang
#router.py router  start_time end_time

import os
import sys

def allRouter(path):
    '''
    打印一个目录下的所有文件夹和文件
    '''
    #print routers
    r = sys.argv[1]
    ports = os.listdir(path + '/' + r)
    for p in ports:
	if(os.path.isdir(path + '/' + r + '/' + p)):
		if(p[0] == '.'):
			pass
		else:
			print p
			os.system('/home/www/IPv6mon/snmpmon/bin/dat2txt %s %s %s %s |python me.py'%(r,p,sys.argv[2],sys.argv[3]))

if __name__ == '__main__':
	if len(sys.argv) < 4:
		print 'Please input router & starttime & endtime'
#		print 'argv[0]为:',sys.argv[0]
	#	print argv[1]
	#	print argv[2]
	else:
		allRouter('/home/www/IPv6mon/snmpmon/dat')
    #print '总文件数 =', allFileNum
