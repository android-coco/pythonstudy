#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print(list(range(1,11)))

# [1x1, 2x2, 3x3, ..., 10x10]怎么做？方法一是循环：
L = []
for x in range(1,11):
	L.append(x * x)
print(L)

print([x * x for x in range(1,11)])
print([x * x for x in range(1,11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])

# 列出当前目录下的所有文件和目录名，可以通过一行代码实现：
import os
print([d for d in os.listdir('.')])

# 列表生成式也可以使用两个变量来生成list：
d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '='+ v for k,v in d.items()])

# 把一个list中所有的字符串变成小写：
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [s.lower() for s in L1 if isinstance(s,str)]
# 测试:
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('测试通过!')
else:
    print('测试失败!')