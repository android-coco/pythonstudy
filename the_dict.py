#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python内置了字典：dict的支持，dict全称dictionary，
# 在其他语言中也称为map，使用键-值（key-value）存储，具有极快的查找速度。
d = {'Michael':95,'Bob':78,'Tracy':85}
d['Jack']=85
# 判断Key是否存在
a = 'Thomas' in d
b = 'Jack' in d
# 要删除一个key，用pop(key)方法，对应的value也会从dict中删除：
d.pop('Bob')
print(d,a,b,d.get('Thomas')==None,d.get('Thomas', -1))
# 扩展
d1 = {'a':(1,2,3,4),'b':(1,[1,3,4])}
print(d1)