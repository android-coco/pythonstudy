#!/usr/bin/env python3
# -*- coding: utf-8 -*-
classmates = ['x','y','z']
classmates.append("x")
classmates.insert(1,'a')
# 删除指定元素
# 要删除list末尾的元素，用pop()方法：
# 要删除指定位置的元素，用pop(i)方法，其中i是索引位置：
# classmates.pop()
print(classmates,len(classmates))
print(classmates[0])
# 元组
t1 = (1,3)
t2 = ()
# t3不是元组  是普通变量加小括号
t3 = (1)
t4 = (1,)
print(t1,t2,t3,t4)
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
# 打印Apple:
print(L[0][0])
# 打印Python:
print(L[1][1])
# 打印Lisa:
print(L[2][2])