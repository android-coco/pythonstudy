#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Python内建的filter()函数用于过滤序列。

# 在一个list中，删掉偶数，只保留奇数，可以这么写：
def is_odd(n):
	return n % 2 == 1
print(list(filter(is_odd,[1,2,4,5,6,7,8,9,10,15])))

# 把一个序列中的空字符串删掉，可以这么写：
def not_empty(s):
	return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))