#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
d = dict(name='Bob',age = 20,score = 88)
print(json.dumps(d))
# dumps()方法返回一个str，内容就是标准的JSON。类似的，dump()方法可以直接把JSON写入一个file-like Object。

# 要把JSON反序列化为Python对象，用loads()或者对应的load()方法，前者把JSON的字符串反序列化，后者从file-like Object中读取字符串并反序列化：
json_str =  '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))


class Student(object):
	"""docstring for Student"""
	def __init__(self, name,age,score):
		super(Student, self).__init__()
		self.name = name
		self.age = age
		self.score = score


# 序列化
def student2dict(std):
	return {
		'name':std.name,
		'age':std.age,
		'score':std.score
	}

s = Student('Bob',20,88)
print(json.dumps(s,default=student2dict))
# 因为通常class的实例都有一个__dict__属性，它就是一个dict，用来存储实例变量。也有少数例外，比如定义了__slots__的class。
print(json.dumps(s,default=lambda obj:obj.__dict__))

# 反序列化
def dict2student(d):
	return Student(d['name'],d['age'],d['score'])
# 打印出的是反序列化的Student实例对象。	
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str,object_hook = dict2student))

# 对中文进行JSON序列化时，json.dumps()提供了一个ensure_ascii参数，观察该参数对结果的影响：
obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
s1 = json.dumps(obj, ensure_ascii=False)
print('ensure_ascii=True  %s ensure_ascii=False %s' % (s,s1))
