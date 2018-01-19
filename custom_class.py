#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __str__
class Student(object):
    def __init__(self, name):
        self.name = name
    def __str__(self):
        return 'Student object (name=%s)' % self.name
    __repr__ = __str__


print(Student('Youhao'))

# 这是因为直接显示变量调用的不是__str__()，而是__repr__()，两者的区别是__str__()返回用户看到的字符串，而__repr__()返回程序开发者看到的字符串，也就是说，__repr__()是为调试服务的。
# 解决办法是再定义一个__repr__()。但是通常__str__()和__repr__()代码都是一样的，所以，有个偷懒的写法：


# __iter__
# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，Python的for循环就会不断调用该迭代对象的__next__()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。
class Fib(object):
	"""docstring for Fib"""
	def __init__(self):
		super(Fib, self).__init__()
		self.a,self.b = 0,1# 初始化两个计数器a，b
	def __iter__(self):
		return self # 实例本身就是迭代对象，故返回自己

	def __next__(self):
		self.a,self.b = self.b , self.a + self.b # 计算下一个值
		if self.a > 100000:# 退出循环的条件
			raise StopIteration()
		return self.a# 返回下一个值

for n in Fib():
	print(n)

# __getitem__
# Fib实例虽然能作用于for循环，看起来和list有点像，但是，把它当成list来使用还是不行，比如，取第5个元素：
# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib1(object):
	"""docstring for Fib"""
	def __init__(self):
		super(Fib1, self).__init__()
		self.a,self.b = 0,1# 初始化两个计数器a，b
	def __iter__(self):
		return self # 实例本身就是迭代对象，故返回自己

	def __next__(self):
		self.a,self.b = self.b , self.a + self.b # 计算下一个值
		if self.a > 100000:# 退出循环的条件
			raise StopIteration()
		return self.a# 返回下一个值
	def __getitem__(self,n):
		a,b = 1,1
		for x in range(n):
			a,b = b,a+b
		return a 
print(Fib1()[100])
# 对于Fib1却报错。原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
class Fib2(object):
	"""docstring for Fib"""
	def __init__(self):
		super(Fib2, self).__init__()
		self.a,self.b = 0,1# 初始化两个计数器a，b
	def __iter__(self):
		return self # 实例本身就是迭代对象，故返回自己

	def __next__(self):
		self.a,self.b = self.b , self.a + self.b # 计算下一个值
		if self.a > 100000:# 退出循环的条件
			raise StopIteration()
		return self.a# 返回下一个值
	def __getitem__(self,n):
		if isinstance(n,int):
			a,b = 1,1
			for x in range(n):
				a,b = b,a+b
			return a 
		if isinstance(n,slice):
			start = n.start
			stop = n.stop
			if start is None:
				start = 0
			a,b = 1,1
			L = []
			for x in range(stop):
				if x >= start:
					L.append(a)
				a,b = b,a+b
			return L

f2 = Fib2()
print(f2[0:5])
print(f2[:10])

# __getattr__
# 正常情况下，当我们调用类的方法或属性时，如果不存在，就会报错。
# 这实际上可以把一个类的所有属性和方法调用全部动态化处理了，不需要任何特殊手段。
class Student1(object):

    def __getattr__(self, attr):
        if attr=='age':
            return lambda: 25
        raise AttributeError('\'Student\' object has no attribute \'%s\'' % attr)
s1 = Student1()
print(s1.age())

class Chain(object):
	"""docstring for Chain"""
	def __init__(self, path=''):
		super(Chain, self).__init__()
		self._path = path

	def __getattr__(self,path):
		return Chain('%s%s' % (self._path,"/"+path))

	def __str__(self):
		return self._path

	__repr__ = __str__

print(Chain().status.user.timeline.list)


# GET /users/:user/repos
#print(Chain1().users('michael').repos)


# __call__
# 只需要定义一个__call__()方法，就可以直接对实例进行调用。
class Student2(object):
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print('My name is %s.' % self.name)

s = Student2('xxx')
s()

# 我们需要判断一个对象是否能被调用，能被调用的对象就是一个Callable对象，比如函数和我们上面定义的带有__call__()的类实例：
print(callable(Student2))
print(callable(max))
print(callable([1, 2, 3]))
print(callable(None))
print(callable('str'))
# Python的class允许定义许多定制方法，可以让我们非常方便地生成特定的类。