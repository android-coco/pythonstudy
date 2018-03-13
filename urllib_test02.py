#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request

if __name__ == '__main__':
	req = request.Request("http://info.sporttery.cn/football/hhad_list.php")
	response = request.urlopen(req)
	print("geturl打印信息：%s"%(response.geturl()))
	print('**********************************************')
	print("info打印信息：%s"%(response.info()))
	print('**********************************************')
	print("getcode打印信息：%s"%(response.getcode()))