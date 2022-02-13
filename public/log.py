# -*- coding: utf-8 -*-

"""
@author: wuqi
@file: log.py
@time: 2022/1/29 19:04
@usage: 
"""
import logging
import os
from datetime import date

date = date.today().isoformat()
logpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'log', str(date))
if not os.path.exists(logpath):
    os.makedirs(logpath)

alllog = os.path.join(logpath, 'all.log')
errlog = os.path.join(logpath, 'err.log')

logger = logging.getLogger('LOG')
logger.setLevel(logging.DEBUG)

rf_handler = logging.FileHandler(alllog)
rf_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)-8s - %(filename)-10s[:%(lineno)d] - %(message)s"))

f_handler = logging.FileHandler(errlog)
f_handler.setLevel(logging.ERROR)
f_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)-8s - %(filename)-10s[:%(lineno)d] - %(message)s"))

c_handler = logging.StreamHandler()
c_handler.setLevel(logging.DEBUG)
c_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)-8s - %(filename)-10s[:%(lineno)d] - %(message)s"))

logger.addHandler(rf_handler)
logger.addHandler(f_handler)
logger.addHandler(c_handler)

if __name__ == '__main__':
    print(os.getcwd())
    print('Hello world')
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')
