#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
	print('try...')
	r = 10 / 0
	print('result:',r)
except ZeroDivisionError as e:
	print('except:',e)
finally:
	print('finally...')
print('END')

# Python的错误其实也是class，所有的错误类型都继承自BaseException，
# 所以在使用except时需要注意的是，它不但捕获该类型的错误，还把其子类也“一网打尽”。

try:
    print('try...')
    r = 10 / int('a')
    print('result:', r)
except ValueError as e:
    print('ValueError:', e)
except ZeroDivisionError as e:
    print('ZeroDivisionError:', e)
finally:
    print('finally...')
print('END')


import logging

def foo(s):
	return 10 / int(s)

def bar(s):
	return foo(s) * 2

def main():
	try:
		bar('0')
	except Exception as e:
		logging.error(e)

main()
print('END')

# 抛出错误
class FooError(ValueError):
	pass

def foo1(s):
	n = int(s)
	if n == 0:
		raise FooError('inalid value :%s' % s)
	return 10 / n

foo1('0')