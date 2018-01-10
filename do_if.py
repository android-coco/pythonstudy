#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖
height = 1.75
weight = 80.5
bmi = 80.5 / (1.75*1.75)
if bmi < 18.5:
	print("过轻")
elif bmi > 18.5 and bmi <= 25:
	print("正常")
elif bmi > 25 and bmi <= 28:
	print("过重")
elif bmi > 28 and bmi <= 32:
	print("肥胖")
elif bmi > 32:
	print("严重肥胖")

