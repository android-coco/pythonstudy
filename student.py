#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Student(object):
	"""docstring for Student"""
	def __init__(self, name,score):
		super(Student, self).__init__()
		self.name = name
		self.score = score
	def print_score(self):
		print('%s %s' % (self.name,self.score))
	def get_grade(self):
		if self.score >= 90:
			return 'A'
		elif self.score >= 60:
			return 'B'
		else:
			return 'C'

bart = Student('Bart Simpson',59)
print(bart.name)
print(bart.score)
bart.print_score()

lisa = Student('Lisa', 99)
bart1 = Student('Bart', 59)
print(lisa.name, lisa.get_grade())
print(bart1.name, bart1.get_grade())