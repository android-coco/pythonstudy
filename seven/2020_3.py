#!/usr/bin/env python3
# -*- coding: utf-8 -*-

accout = 'youhao'
password = '123456'


print('please input account')
user_account = input()

print('please input passworld')
user_password = input()


if accout == user_account and password == user_password:
    print('success')
else:
    print('fail')