# -*- coding: utf-8 -*-

"""
@author: wuqi
@file: kbdutil.py
@time: 2022/2/7 21:04
@usage: 
"""
import time

import pyautogui

if __name__ == '__main__':
    print('Hello world')
    # print(pyautogui.KEY_NAMES)
    for i in range(9):
        pyautogui.click(1350, 715)
        time.sleep(1)
        pyautogui.hotkey('ctrl', 's')
        time.sleep(1)
        pyautogui.press('enter')
        time.sleep(20)
