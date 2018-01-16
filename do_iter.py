#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
	print(key)
for value in d.values():
	print(value)
for k,v in d.items():
	print(k,v)
for ch in 'ABC':
	print(ch)

print(isinstance('abc',Iterable)) # str是否可迭代
print(isinstance([1,2,3], Iterable)) # list是否可迭代
print(isinstance(123, Iterable)) # 整数是否可迭代

def cf(x):
	# 25 10 5 1
	m = {25:0,10:0,5:0,1:0}
	for i in m:
		if x >= i:
			m[i] = int(x // i)
			x = x % i
	return str(m[25]) + "个25美分 " + str(m[10]) + "个10美分  " + str(m[5])+ "个5美分  " + str(m[1]) + "个1美分"

x = float(input("请输入美元数(元): ")) * 100
print(cf(x))
# 请使用迭代查找一个list中最小和最大值，并返回一个tuple
def findMinAndMax(l):
	max,min = 0,0
	if isinstance(l, Iterable):
		if len(l) == 0:
			return (None,None)
		min = l[0] # 假设第一个为最小值
		for i in l:
			if max < i:
				max = i
			if min > i:
				min = i
		return (min,max)
	else:
		return (None,None)
# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
	


