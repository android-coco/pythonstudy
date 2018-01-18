#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 位置参数
def power(x):
	return x * x
# 对于power(x)函数，参数x就是一个位置参数。
def power1(x,n):
	s = 1
	while n > 0:
		n -= 1 
		s *= x
	return s
print(power(2))
print(power1(2,2))
# 修改后的power1(x, n)函数有两个参数：x和n，这两个参数都是位置参数，
# 调用函数时，传入的两个值按照位置顺序依次赋给参数x和n。

# 默认参数
# 一是必选参数在前，默认参数在后
# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。变化小的参数就可以作为默认参数。
# 当不按顺序提供部分默认参数时，需要把参数名写上 enroll('Adam', 'M', city='Tianjin')
def power2(x,n=2):
	s = 1
	while n > 0:
		n -= 1
		s *= x
	return s
# 错误演示 默认参数有个最大的坑
def add_end(L = []):
	L.append('END')
	return L
print(add_end([1, 2, 3]))
print(add_end([1, 2, 3]))
print(add_end())
print(add_end())
#  定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end1(L = None):
	if L is None:
		L = []
	L.append('END')
	return L
# 现在，无论调用多少次，都不会有问题：
print(add_end1())
print(add_end1())

# 可变参数
def cals(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
print(cals())
print(cals(1))
print(cals(1,2,3))
a = [1,2,3]# list
b = (1,2,3)# tuple
# *a表示把a这个list的所有元素作为可变参数传进去。这种写法相当有用，而且很常见
print(cals(*a))
print(cals(*b))


# 关键字参数
# 可变参数允许你传入0个或任意个参数，这些可变参数在函数调用时自动组装为一个tuple。
# 而关键字参数允许你传入0个或任意个含参数名的参数，这些关键字参数在函数内部自动组装为一个dict
def person(name,age,**kw):
	print('name:',name,' age:',age,' other:',kw)
person('Michael', 30)
person('Bob', 35, city='Beijing')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Bob', 35, **extra)



# 命名关键字参数
# 使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：
def person1(name,age,*,city,job):
	print(name, age, city, job)
person1('Jack1', 24,city='Tianjin1',job='Engineer1')

# 如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person2(name,age,*agrs,city,job):
	print(name, age, city, job)
person2('Jack2', 24,city='Tianjin2',job='Engineer2')


def person3(name,age,*,city='Beijing',job):
	print(name, age, city, job)
person3('Jack3', 24, job='Engineer3')


# 参数组合
# 在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
# 但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a,b,c=0,*args,**kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a,b,c=0,*,d,**kw):
	 print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
f1(1, 2)
f1(1, 2, c=3)
f1(1, 2, 3, 'a', 'b')
f1(1, 2, 3, 'a', 'b', x=99)
f2(1, 2, d=99, ext=None)

args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args,**kw)

args = (1, 2, 3)
kw = {'d': 88, 'x': '#'}
f2(*args, **kw)
# 所以，对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的。

