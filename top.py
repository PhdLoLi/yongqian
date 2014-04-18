#!/usr/bin/python
# -*- coding:utf8 -*-
#top read all the routers and ports from starttime to endtime
#author:Loli Wang

import os
import sys

def allRouter(path):
    '''
    打印一个目录下的所有文件夹和文件
    '''
    # 所有文件夹，第一个字段是次目录的级别
    dirList = []
    # 所有文件
    fileList = []
    # 返回一个列表，其中包含在目录条目的名称(google翻译)
    routers = os.listdir(path)
    #print routers
    # 先添加目录级别
   # dirList.append(str(level))
    for r in routers:
        if(os.path.isdir(path + '/' + r)):
            # 排除隐藏文件夹。因为隐藏文件夹过多
            if(r[0] == '.'):
                pass
            else:
                # 添加非隐藏文件夹
                dirList.append(r)
		ports = os.listdir(path + '/' + r)
	#	print r
		#print ports
		for p in ports:
			if(os.path.isdir(path + '/' + r + '/' + p)):
				if(p[0] == '.'):
					pass
				else:
				#	files = os.listdir(path + '/' + p)	
					#print p
					os.system('/home/www/IPv6mon/snmpmon/bin/dat2txt %s %s %s %s |python me.py'%(r,p,sys.argv[1],sys.argv[2]))
	break

if __name__ == '__main__':
	if len(sys.argv) < 3:
		print 'Please input starttime & endtime'
#		print 'argv[0]为:',sys.argv[0]
	#	print argv[1]
	#	print argv[2]
	else:
		allRouter('/home/www/IPv6mon/snmpmon/dat')
    #print '总文件数 =', allFileNum
