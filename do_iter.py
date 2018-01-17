#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import Iterable,Iterator

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
	
def g():
	yield 1
	yield 2
	yield 3

print('Iterable? [1, 2, 3]:', isinstance([1, 2, 3], Iterable))
print('Iterable? \'abc\':', isinstance('abc', Iterable))
print('Iterable? 123:', isinstance(123, Iterable))
print('Iterable? g():', isinstance(g(), Iterable))

print('Iterator? [1, 2, 3]:', isinstance([1, 2, 3], Iterator))
print('Iterator? iter([1, 2, 3]):', isinstance(iter([1, 2, 3]), Iterator))
print('Iterator? \'abc\':', isinstance('abc', Iterator))
print('Iterator? 123:', isinstance(123, Iterator))
print('Iterator? g():', isinstance(g(), Iterator))

# iter list:
print('for x in [1, 2, 3, 4, 5]:')
for x in [1, 2, 3, 4, 5]:
    print(x)

print('for x in iter([1, 2, 3, 4, 5]):')
for x in iter([1, 2, 3, 4, 5]):
    print(x)

print('next():')
it = iter([1, 2, 3, 4, 5])
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

d = {'a': 1, 'b': 2, 'c': 3}

# iter each key:
print('iter key:', d)
for k in d.keys():
    print('key:', k)

# iter each value:
print('iter value:', d)
for v in d.values():
    print('value:', v)

# iter both key and value:
print('iter item:', d)
for k, v in d.items():
    print('item:', k, v)

# iter list with index:
print('iter enumerate([\'A\', \'B\', \'C\']')
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

# iter complex list:
print('iter [(1, 1), (2, 4), (3, 9)]:')
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x, y)

# 凡是可作用于for循环的对象都是Iterable类型；

# 凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

# 集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。