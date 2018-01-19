#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
	"""docstring for Student"""
	pass

s = Student()
s.name = 'Michael' # 动态给实例绑定一个属性
print(s.name)

def set_age(self,age): # 定义一个函数作为实例方法
	self.age = age

from types import MethodType
s.set_age = MethodType(set_age,s)# 给实例绑定一个方法
s.set_age(25) # 调用实例方法
print(s.age)# 测试结果

#但是，给一个实例绑定的方法，对另一个实例是不起作用的：
s2 = Student() # 创建新的实例
# s2.set_age(25) # 尝试调用方法

# 为了给所有实例都绑定方法，可以给class绑定方法：
def set_score(self,score):
	self.score = score

Student.set_score = set_score
# 给class绑定方法后，所有实例均可调用：
s.set_score(100)
print(s.score)

s2.set_score(100)
print(s2.score)

# 使用__slots__   只允许对Student实例添加name和age属性。
# 使用__slots__要注意，__slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用的：
class Student1(object):
    __slots__ = ('name', 'age') # 用tuple定义允许绑定的属性名称

class GraduateStudent(Student1):
	pass

g = GraduateStudent()
g.score = 9999