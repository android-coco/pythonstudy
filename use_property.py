#!/usr/bin/env python3
# -*- coding: utf-8 -*-
class Student(object):

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value

s = Student()
s.score = 60 # OK，实际转化为s.set_score(60)
print(s.score) # OK，实际转化为s.get_score()
# s.score = 9000

class A(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2015 - self._birth

# 上面的birth是可读写属性，而age就是一个只读属性，因为age可以根据birth和当前时间计算出来。

class Screen(object):
	@property
	def width(self):
		return self._width

	@width.setter
	def width(self,value):
		if not isinstance(value,int):
			raise ValueError('width must be an integer!')
		self._width = value

	@property
	def height(self):
		return self._height

	@height.setter
	def height(self,value):
		if not isinstance(value,int):
			raise ValueError('height must be an integer!')
		self._height = value

	@property
	def resolution(self):
		return self._width * self._height

# 测试:
s1 = Screen()
s1.width = 1024
s1.height = 768
print('resolution =', s1.resolution)
if s1.resolution == 786432:
    print('测试通过!')
else:
    print('测试失败!')