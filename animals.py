#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Animal(object):
	"""docstring for Animal"""
	def run(self):
		print('Animal is running...')
        

class Dog(Animal):
	def run(self):
		print('Dog is running...')

	def eat(self):
		print('Eating meat...')

class Cat(Animal):
	def run(self):
		print('Cat is running...')

dog = Dog()
dog.run()

cat = Cat()
cat.run()