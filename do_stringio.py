#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# StringIO顾名思义就是在内存中读写str

from io import StringIO
f = StringIO()
print(f.write('hello'))
print(f.write(' '))
print(f.write('world!'))
# getvalue()方法用于获得写入后的str。
print(f.getvalue())

# 要读取StringIO，可以用一个str初始化StringIO，然后，像读文件一样读取:
f = StringIO('Hello!\nHi!\nGoodbye!')
while True:
	s = f.readline()
	if s == '':
		break
	# strip() 方法用于移除字符串头尾指定的字符（默认为空格）。
	print(s.strip())