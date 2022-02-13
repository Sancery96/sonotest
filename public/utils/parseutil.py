# -*- coding: utf-8 -*-

"""
@author: wuqi
@file: parseutil.py
@time: 2022/2/8 0:32
@usage: 
"""

from parse import parse, compile


if __name__ == '__main__':
    print('Hello world')
    pattern = compile('I am {name}, {age} years old, {gender}')
    res = pattern.parse("I am Jack, 27 years old, male")
    print(res, res['name'])

    print('Hello world')
    pattern = compile('I am {name}, {age:d} years old, {gender}, {time:tg}')
    res = pattern.parse("I am   Jack , 27 years old, male, 20/1/1972 10:21:36 AM +1:00")
    print(res, res['name'].strip())
