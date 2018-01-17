#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import reduce
def f(x):
	return x * x
r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))

def add(x,y):
	return x + y

print(reduce(add,[1,3,5,7,9]))
# 当然求和运算可以直接用Python内建函数sum()，没必要动用reduce。
# 但是如果要把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场：
def fn(x,y):
	return x * 10 + y
print(reduce(fn,[1,3,5,7,9]))

# reduce()还可以接收第3个可选参数，作为计算的初始值。如果把初始值设为100，计算：
# reduce(f, [1, 3, 5, 7, 9], 100)
# 结果将变为125，因为第一轮计算是：
# 计算初始值和第一个元素：f(100, 1)，结果为101。

def char2num(s):
	digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
	return digits[s]
print(reduce(fn,map(char2num,'13579')))

# 整理成一个str2int的函数就是：
DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
def str2int(s):
    def fn(x, y):
        return x * 10 + y
    def char2num(s):
        return DIGITS[s]
    return reduce(fn, map(char2num, s))
print(str2int("123456"))
# 还可以用lambda函数进一步简化成：
# def char2num(s):
    # return DIGITS[s]

# def str2int(s):
    # return reduce(lambda x, y: x * 10 + y, map(char2num, s))


# 练习
def normalize(name):
	i = 0
	newname = ''
	for x in name:
		if i == 0:
			newname += x.upper() 
		else:
			newname += x.lower() 
		i = i + 1
	return newname
# 测试:
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

# 练习2
def prod(L):
    def fn(x,y):
        return x * y
    return reduce(fn,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
if prod([3, 5, 7, 9]) == 945:
    print('测试成功!')
else:
    print('测试失败!')

# 练习3  好好看
CHAR_TO_FLOAT  = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,'.':-1}
def str2float(s):
	def fn(ch):
		return CHAR_TO_FLOAT[ch]
	point = 0
	def to_float(f,n):
		# print(f,n)
		nonlocal point
		if n == -1:
			point = 1
			return f 
		if point == 0:
			return f * 10 + n
		else:
			point = point * 10 
			return f + n / point
	return reduce(to_float,map(fn,s),0.0)

print(str2float('0'))
print(str2float('123.456'))
print(str2float('123.45600'))
print(str2float('0.1234'))
print(str2float('.1234'))
print(str2float('120.0034'))
