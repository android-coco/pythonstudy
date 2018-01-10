#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

print(my_abs(-2))

#如果想定义一个什么事也不做的空函数，可以用pass语句：
def nop():
	pass

def move(x,y,step,angle=0):
	nx = x + step * math.cos(angle)
	ny = y - step * math.sin(angle)
	return nx,ny
x,y = move(100,100,60,math.pi / 6)
print(x,y)
# 但其实这只是一种假象，Python函数返回的仍然是单一值
# 原来返回值是一个tuple！但是，在语法上，返回一个tuple可以省略括号，而多个变量可以同时接收一个tuple，按位置赋给对应的值，
# 所以Python的函数返回多值其实就是返回一个tuple，但写起来更方便。
r = move(100,100,60,math.pi / 6)
print(r)

# 一元二次方程的两个解。
def quadratic(a,b,c):
	x,y = 0,0
	if a == 0:
		return "a不能＝0"
	# 方差
	temp = b * b - 4 * a * c
	x = (-b + math.sqrt(temp)) / (2 * a)
	y = (-b - math.sqrt(temp)) / (2 * a)
	return x,y
print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
