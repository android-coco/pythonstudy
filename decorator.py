#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 装饰器
def now():
	print('2018-01-19')
f = now
f()
# 函数对象有一个__name__属性，可以拿到函数的名字：
print(now.__name__)
print(f.__name__)

# 在代码运行期间动态增加功能的方式，称之为“装饰器”（Decorator）。
def log(func):
	def wrapper(*args,**kw):
		print('call %s():'% func.__name__)
		return func(*args,**kw)
	return wrapper
@log
def now1():
	print('2018-01-19')
now1()
