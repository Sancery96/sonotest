# -*- coding: utf-8 -*-

"""
@author: wuqi
@file: inherit.py
@time: 2022/2/9 21:02
@usage: 
"""

class Base:
    def __init__(self, a):
        self.a = a

    def print_var(self, b):
        y = self.a + b
        print(self.a, b)
        return y

class Inheri(Base):
    def __init__(self, a):
        super().__init__(a)

    def print_var(self):
        b = 'm'
        super(Inheri, self).print_var(b)
        # print(b)


if __name__ == '__main__':
    print('Hello world')
    x = Inheri(3).print_var()
    print(x)
