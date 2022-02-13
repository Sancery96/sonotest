# -*- coding: utf-8 -*-

"""
@author: wuqi
@file: case.py
@time: 2022/1/29 19:22
@usage: 
"""
import time

from thrift.protocol import TBinaryProtocol
from thrift.transport import TSocket, TTransport

from public.config import api_define
from public.log import logger
from public.pythrift.autotest import autotest
from public.pythrift.autotest.ttypes import *


def format_case(case):
    case_content = case
    if case.endswith('.case'):
        with open(case, 'r', encoding='utf-8') as casefile:
            case_content = casefile.read()
    return case_content


class Case:
    def __init__(self):
        pass

    def run(self, ip, case):
        case_content = format_case(case)
        try:
            socket = TSocket.TSocket(ip, 9090)
            socket.setTimeout(120000)
            transport = TTransport.TBufferedTransport(socket)
            protocol = TBinaryProtocol.TBinaryProtocol(transport)
            internalClient = autotest.Client(protocol)
            transport.open()
            client = api_define.WrapClient(internalClient)
            try:
                for no, caseline in enumerate(case_content.split('\n')):
                    exec(caseline)
                    time.sleep(0.5)
                    if self.take_effect():
                        logger.info(f'execute line{no+1:<3} -- {caseline} success!')
                    else:
                        raise Exception(f'execute line{no+1:<3} -- {caseline} fail!')
            except Exception as e:
                logger.error(e)
            finally:
                transport.close()
        except Exception as e:
            logger.error(e)

    def take_effect(self):
        pass


if __name__ == '__main__':
    print('Hello world')
    Case().run('1', 'test/test.case')
    Case().run('1', 'print("hello")')
