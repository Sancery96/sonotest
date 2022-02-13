# -*- coding: utf-8 -*-

"""
@author: wuqi
@file: learn_np.py
@time: 2022/2/7 23:03
@usage: 
"""

if __name__ == '__main__':
    print('Hello world')
    import numpy as np

    # 创建一维数组
    a = np.array([1, 2, 3])
    print(a)        # [1 2 3]
    print(type(a))  # <class 'numpy.ndarray'>

    # 创建多维数组
    b = np.array([[1, 2, 3], [4, 5, 6]])
    print(b)
    '''
    [[1 2 3]
    [4 5 6]]
    '''
    print(type(b))   # <class 'numpy.ndarray'>

    # 设置数组元素类型
    # 创建一维数组
    c = np.array([1, 2, 3], dtype='complex')
    print(c)         # [1.+0.j 2.+0.j 3.+0.j]
    print(type(c))   # <class 'numpy.ndarray'>

    # 查看数组维度
    print(a.ndim)    # 1
    print(b.ndim)    # 2
    print(c.ndim)    # 1

    # 指定数组维度
    # d = np.array([1, 2, 3], ndim=2)
    # print(d)        #

    # 转置
    e = np.array([[1, 2], [3, 4], [5, 6]])
    print("原数组：\n", e)
    row = len(e)
    col = len(e[0])
    # print(row, col)
    e = e.reshape(col, row)
    print("新数组：\n", e)
