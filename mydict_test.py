#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from mydict import Dict

class TestDict(unittest.TestCase):

	# 每个测试方法调用前后是否会打印出setUp...和tearDown...。
	def setUp(self):
		print('setUp...')
	# 每个测试方法调用前后是否会打印出setUp...和tearDown...。
	def tearDown(self):
		print('tearDown...')

	def test_init(self):
		d = Dict(a=1,b='test')
		# 断言函数返回的结果与1相等
		self.assertEqual(d.a,1)
		self.assertEqual(d.b,'test')
		self.assertTrue(isinstance(d,dict))

 
	def test_key(self):
		d = Dict()
		d['key'] = 'value'
		# 断言函数返回的结果与1相等
		self.assertEqual(d.key,'value')

	def test_attr(self):
		d = Dict()
		d.key = 'value'
		self.assertTrue('key' in d)
		# 断言函数返回的结果与1相等
		self.assertEqual(d['key'],'value')

	def test_keyerror(self):
		d = Dict()
		# 期待抛出指定类型的Error
		with self.assertRaises(KeyError):
			value = d['empty']

	def test_attrerror(self):
		d = Dict()
		# 期待抛出指定类型的Error
		with self.assertRaises(AttributeError):
			value = d.empty
#  运行测试文件
# 1 命令行
# python -m unittest mydict_test
# 2 写代码直接运行
# if __name__ == '__main__':
# 	unittest.main()
#python mydict_test
   