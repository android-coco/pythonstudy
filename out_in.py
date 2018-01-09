a = input('请输入A：')
b = input('请输入B：')
c = input('请输入C：')
def bj(a,b,c):
    # 先比较a和b
    if a>=b:
        maxnum = a
    else:
        maxnum = b
    # 再比较maxnum和c
    if c>maxnum:
        maxnum=c
    return maxnum
#print('hello',a,b,c)
print('hello',bj(int(a),int(b),int(c)))