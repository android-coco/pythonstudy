#!/usr/bin/env python3
# -*- coding: utf-8 -*-
s = set([1,2,3])
# 重复元素在set中自动被过滤：
s1 = set([1,1,2,3])
# 通过add(key)方法可以添加元素到set中，可以重复添加，但不会有效果：
s1.add(4)
s1.add(4)
# 通过remove(key)方法可以删除元素：
s1.remove(4)
print(s,s1)
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
s3 = set([1,2,3])
s4 = set([2,3,4])
# 并集
print(s3 & s4)
# 合集
print(s3 | s4)
# set和dict的唯一区别仅在于没有存储对应的value，但是，set的原理和dict一样，所以，同样不可以放入可变对象，
# 因为无法判断两个可变对象是否相等，
# 也就无法保证set内部“不会有重复元素”。试试把list放入set，看看是否会报错。

# 扩展
yz1 = (1,2,3,4)
list1 = [1,3,4]
# yz2 = (1,list1)
yz2 = (1,6)
d1 = set([yz1,'b',yz2])
print(yz1,yz2)