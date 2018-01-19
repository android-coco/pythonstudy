#!/usr/bin/env python3
# -*- coding: utf-8 -*-
print(type(123))
print(type('str'))
print(type(None))
print(type(abs))

# 判断基本数据类型可以直接写int，str等，但如果要判断一个对象是否是函数怎么办？可以使用types模块中定义的常量：
import types
def fn():
	pass

print(type(fn) == types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

# 对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数。

# 如果要获得一个对象的所有属性和方法，可以使用dir()函数，它返回一个包含字符串的list，比如，获得一个str对象的所有属性和方法：
print(dir('ABC'))

print(len('ABC'))
print('ABC'.__len__())

class MyObject(object):
	"""docstring for MyObject"""
	def __init__(self):
		super(MyObject, self).__init__()
		self.x = 9
	def power(self):
		return self.x * self.x
obj = MyObject()

print(hasattr(obj,'x')) # 有属性'x'吗？
print(hasattr(obj, 'y')) # 有属性'y'吗？
setattr(obj, 'y', 19) # 设置一个属性'y'
print(hasattr(obj, 'y')) # 有属性'y'吗？
print(getattr(obj, 'y')) # 获取属性'y'
# 如果试图获取不存在的属性，会抛出AttributeError的错误：
print(getattr(obj, 'z', 404)) # 获取属性'z'，如果不存在，返回默认值404

print(hasattr(obj, 'power')) # 有方法'power'吗？
print(getattr(obj, 'power')) # 获取方法'power'
fn = getattr(obj, 'power') # 获取属性'power'并赋值到变量fn
print(fn())

def readImage(fp):
	if hasattr(fp,'read'):
		return read(fp)
	return None

# 实例属性属于各个实例所有，互不干扰；
# 类属性属于类所有，所有实例共享一个属性；
# 不要对实例属性和类属性使用相同的名字，否则将产生难以发现的错误。