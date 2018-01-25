#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# pickle模块来实现序列化。
import pickle
d = dict(name='Bob',age=20,score=88)
print(pickle.dumps(d))

# pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入一个file-like Object：
# f = open('dump.txt', 'wb')
# pickle.dump(d, f)
# f.close()

# with open('dump.txt','wb') as f:
# 	pickle.dump(d,f)

with open('dump.txt','rb') as f:
	print(pickle.load(f))
# 当然，这个变量和原来的变量是完全不相干的对象，它们只是内容相同而已。

# Pickle的问题和所有其他编程语言特有的序列化问题一样，就是它只能用于Python，并且可能不同版本的Python彼此都不兼容，
# 因此，只能用Pickle保存那些不重要的数据，不能成功地反序列化也没关系。