#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 生成器

g = (x * x for x in range(10))
# print(g)

print(next(g))

for n in g:
	print(n)
#所以，我们创建了一个generator后，基本上永远不会调用next()，
#而是通过for循环来迭代它，并且不需要关心StopIteration的错误。
 
def fib(max):
	n,a,b = 0,0,1
	while n < max:
		print(b)
		a,b = b,a+b
		n = n+1 
	return 'done'
print(fib(6))

def fib1(max):
	n,a,b = 0,0,1
	while n < max:
		yield b
		a,b = b,a+b
		n = n+1
	return 'done'
f = fib1(6)
print(f)

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)
o = odd()
# print(next(o))
# print(next(o))
# print(next(o))
# print(next(o))
# 但是用for循环调用generator时，发现拿不到generator的return语句的返回值。
# 如果想要拿到返回值，必须捕获StopIteration错误，返回值包含在StopIteration的value中：
for x in fib1(6):
	print(x)
g = fib1(6)
while True:
	try:
		x = next(g)
		print('g:',x)
	except StopIteration as e:
		print('Generator return value:',e.value)
		break

# 杨辉三角
def triangles():
	L = [1]
	while True:
		yield L
		L = [L[x] + L[x+1] for x in range(len(L) - 1)]
		L.insert(0,1) # 头
		L.append(1)  # 尾部
		if len(L) > 10:
			break
def triangles1(n):
	L = [1]
	while len(L) <= n:
		yield L
		L = [L[x] + L[x+1] for x in range(len(L) - 1)]
		L.insert(0,1) # 头
		L.append(1)  # 尾部
for t in triangles():
	print(t)

n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
