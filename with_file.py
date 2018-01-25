#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# try:
# 	f = open('test.txt','r',encoding='gbk')
# 	str = f.read()
# 	print(str)
# finally:
# 	if f:
# 		f.close()

#这和前面的try ... finally是一样的，但是代码更佳简洁，并且不必调用f.close()方法
with open('test.txt','r',encoding='utf-8',errors='ignore') as f:
	print(f.read())

# 读取图片
with open('1-4.jpg','rb') as f:
	print(f.read())# 十六进制表示的字节

# 字符编码
# 要读取非UTF-8编码的文本文件，需要给open()函数传入encoding参数，例如，读取GBK编码的文件：
# open('test.txt','r',encoding='gbk')
# 遇到有些编码不规范的文件，你可能会遇到UnicodeDecodeError，因为在文本文件中可能夹杂了一些非法编码的字符。遇到这种情况，open()函数还接收一个errors参数，表示如果遇到编码错误后如何处理。最简单的方式是直接忽略：
# open('/Users/michael/gbk.txt', 'r', encoding='gbk', errors='ignore')



# 写文件
# 写文件和读文件是一样的，唯一区别是调用open()函数时，传入标识符'w'或者'wb'表示写文本文件或写二进制文件：
# 以'w'模式写入文件时，如果文件已存在，会直接覆盖（相当于删掉后新写入一个文件）。如果我们希望追加到文件末尾怎么办？可以传入'a'以追加（append）模式写入。
with open('test.txt', 'a') as f:
    f.write('Hello, world!')

with open('test1.txt', 'w') as f:
    f.write('Hello, world!')