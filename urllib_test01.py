#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from urllib import request
import chardet

if __name__ == '__main__':
	response = request.urlopen("http://info.sporttery.cn/football/hhad_list.php")
	html = response.read()
	charset = chardet.detect(html)
	# html = html.decode("utf-8")
	html = html.decode(charset['encoding'])
	print(html)