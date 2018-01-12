#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(L[0:])
# 记住倒数第一个元素的索引是-1
print(L[-2:])

# 切片操作十分有用。我们先创建一个0-99的数列：
L1 = list(range(100))
print(L1)
# 前10个数：
print(L1[:10])
# 后10个数:
print(L1[-10:])
# 前11-20个数：
print(L1[10:20])
# 前10个数，每两个取一个：
print(L1[:10:2])
# 所有数，每5个取一个：
print(L1[::2])
print(L1[:])

# 元组
print((0, 1, 2, 3, 4, 5)[:3])

# 字符串'xxx'也可以看成是一种list，每个元素就是一个字符
print('ABCDEFG'[:3])
print('ABCDEFG'[::2])
# 利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
def trim(s):
	s = str(s)
	if s == '':
		return s
	if s != "" and s[0] == ' ':
		s = s[1:]
	if s != "" and  s[-1] == ' ':
		s = s[:-1]
	if s != "" and (s[0] == ' ' or s[-1] == ' '):
		return trim(s)
	return s
# 测试:
if trim(123  ) != '123':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')
