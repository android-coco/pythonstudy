#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# StringIO操作的只能是str，如果要操作二进制数据，就需要使用BytesIO。

from io import BytesIO
f = BytesIO()
# 请注意，写入的不是str，而是经过UTF-8编码的bytes。
f.write('中文'.encode('utf-8'))
print(f.getvalue())

f = BytesIO(b'\xe4\xb8\xad\xe6\x96\x87')
print(f.read())