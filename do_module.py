#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 模块
' a test module'
__author__ = 'Yh'

import sys

def test():
	args = sys.argv
	if len(args) == 1:
		print('Hello World!')
	elif len(args) == 2:
		print('Hello,%s!'% args[1])
	else:
		print('Too many arguments!')

def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)
# 当我们在命令行运行do_module模块文件时，Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该do_module模块时，if判断将失败，
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，最常见的就是运行测试。
if __name__ == '__main__':
	test()