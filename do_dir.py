#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Python内置的os模块也可以直接调用操作系统提供的接口函数。
import os
print(os.name)# 操作系统类型
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统。
# 要获取详细的系统信息，可以调用uname()函数：
# os.uname()
# 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。


# 在操作系统中定义的环境变量，全部保存在os.environ这个变量中，可以直接查看：
print(os.environ)

print(os.environ.get('PATH'))
print(os.environ.get('x','default'))
print(os.environ.get('JAVA_HOME','default'))


# 操作文件和目录
# 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中

# # 查看当前目录的绝对路径:
print(os.path.abspath('.'))
# # 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
path = os.path.join('C:\workHome\pythonwork\pythonstudy','testdir')
print(path)
## 然后创建一个目录:
os.mkdir(path)
# 删掉一个目录:
os.rmdir(path)

# 把两个路径合成一个时，不要直接拼字符串，而要通过os.path.join()函数，这样可以正确处理不同操作系统的路径分隔符
# 同样的道理，要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：

print(os.path.split('/Users/michael/testdir/file.txt'))
#os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
print(os.path.splitext('/path/to/file.txt'))


# 列出当前目录下的所有目录
print([x for x in os.listdir('.') if os.path.isdir(x)])

# 列出所有的.py文件，也只需一行代码：
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])