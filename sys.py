#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

_ver = sys.version_info

is_py2 = (_ver[0] == 2)
is_py3 = (_ver[0] == 3)

if is_py2:
	print('python2')
if is_py3:
	print('python3')
# 平台信息
print(sys.platform)