#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 字符格式化，有两种方式：
# 1、通过%占位符方式，%s，%d,%
# 2、通过format，其中format比较好用，可以居中、可以用%、可以用二进制、可以填充字符自定义；

# 1、利用%
tp1 = "i am %s"%"aaa"
tp2 = "i am %s age %d" % ("alex",18) # 顺序关联
tp3 = "i am %(name)s age %(age)d" % {"name":"alex","age":18} # 指定名称，起名字
tp4 = "percent%.2f"%99.567 # 保留小数点几位
tp5 = "i am %(pp).2f"%{"pp":12.45667}# 指定名称，保留两位小数
tp6 = "i am %(pp).2f%%"%{"pp":13.34566}# 用双%%来引用%
print("tp1:",tp1)
print("tp2:",tp2)
print("tp3:",tp3)
print("tp4:",tp4)
print("tp5:",tp5)
print("tp6:",tp6)

# 2、利用format
tp1 = "i am {},age{},you are{}".format("hhh",123,"yyy")# 顺序填充
tp2 = "i am {},age{},you are{}".format(*["hhh",123,"yyy"])# 动态参数填充
tp3 = "i am {0},age{1},you are{0} too".format("hhh",123)# 占位符索引填充，顺序填充
tp4 = "i am {0},age{1},you are{0} too".format(*["hhh",123])# 占位符索引填充，动态参数填充
tp5 = "i am {name},age{age},you are{name} too".format(name="hhh",age=123)# 指定名称填充，名称顺序可变
tp6 = "i am {name},age{age},you are{name} too".format(**{"name":"hhh","age":123})# 指定名称，动态参数，字典需要**
tp7 = "i am {0[0]},age{0[1]},you are{0[2]}".format([1,2,3],[11,22,33])# 通过列表传递
tp8 = "i am {:s},age{:d},money{:f}".format("hh",18,88.11)# 格式化字符，S字符，d整数，f浮点型
tp9 = "i am {name:s},age{age:d}".format(name="hh",age=18)# 指定名称，S字符，d整数，f浮点型
tp10= "i am {name:s},age{age:d}".format(**{"name":"hhh","age":123})# 动态参数+指定名称，S字符，d整数，f浮点型
tp11= "numbers:{:b},{:o},{:d},{:x},{:X},{:%}".format(15,15,15,15,15,3.666)# 格式化字符，b二进制，d整型
tp12= "numbers:{0:b},{0:o},{0:d},{0:x},{0:X},{0:%}".format(15)#格式化+索引，b是字节型，o是八进制，x是16进制
tp13= "numbers:{num:b},{num:o},{num:d},{num:x},{num:X},{num:%}".format(num=15)# 格式化+指定名称
print("tp1:",tp1)
print("tp2:",tp2)
print("tp3:",tp3)
print("tp4:",tp4)
print("tp5:",tp5)
print("tp6:",tp6)
print("tp7:",tp7)
print("tp8:",tp8)
print("tp9:",tp9)
print("tp10:",tp10)
print("tp11:",tp11)
print("tp12:",tp12)
print("tp13:",tp13)

# 3、颜色格式：

# ANSI控制码的说明 
# \033[0m 关闭所有属性 
# \033[1m 设置高亮度 
# \033[4m 下划线 
# \033[5m 闪烁 
# \033[7m 反显 
# \033[8m 消隐 
# \033[30m -- \33[37m 设置前景色 
# \033[40m -- \33[47m 设置背景色 
# \033[nA 光标上移n行 
# \033[nB 光标下移n行 
# \033[nC 光标右移n行 
# \033[nD 光标左移n行 
# \033[y;xH设置光标位置 
# \033[2J 清屏 
# \033[K 清除从光标到行尾的内容 
# \033[s 保存光标位置 
# \033[u 恢复光标位置 
# \033[?25l 隐藏光标 
# \033[?25h 显示光标  


# 设置控制台输出字体颜色
# 格式：\033[显示方式;前景色;背景色m
# 采用终端默认设置：\033[0m

# 数值表示的参数含义：
# 显示方式: 0（默认值）、1（高亮）、22（非粗体）、4（下划线）、24（非下划线）、 5（闪烁）、25（非闪烁）、7（反显）、27（非反显）
# 前景色: 30（黑色）、31（红色）、32（绿色）、 33（黄色）、34（蓝色）、35（洋 红）、36（青色）、37（白色）
# 背景色: 40（黑色）、41（红色）、42（绿色）、 43（黄色）、44（蓝色）、45（洋 红）、46（青色）、47（白色）


# 红色字体
print('\033[1;31m')
print('*' * 10)
print('hello world！')
print('*' * 10)
print('\033[0m')

# 绿色字体
print('\033[1;32m' + 'green' + '\033[0m')
# 蓝色字体
print('\033[1;34m' + 'blue' + '\033[0m')
# 黄字下划线
print('\033[4;33m' + 'yellow' + '\033[0m')
# 红底黑字
print('\033[1;30;41m' + 'black' + '\033[0m')
# 白底黑字
print('\033[1;30;47m' + 'white' + '\033[0m')