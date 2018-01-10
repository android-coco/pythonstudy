#!/usr/bin/env python3
# -*- coding: utf-8 -*-
sum = 0
n = 99
while n > 0:
	sum += n
	n = n-2
print(sum)

# 10以内的奇数
n = 0
while n < 10:
	n = n + 1
	if n % 2 == 0:
		continue
	print(n)