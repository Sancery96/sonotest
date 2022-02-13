# -*- coding: utf-8 -*-

"""
@author: wuqi
@file: ssh_client.py
@time: 2022/1/29 19:03
@usage: 
"""

import paramiko
from public.log import logger


class SSH:

    _instance = None
    connected = False

    def __init__(self, ip='192.168.244.128', port=22, username='tony', password='123456'):
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password
        try:
            self.client = paramiko.SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(self.ip, self.port, self.username, self.password)
            SSH.connected = True
            logger.info(f'connect to port {self.port} on {self.ip} success!')
            self.sftp = self.client.open_sftp()
        except Exception as e:
            logger.error(f'connect error ==> {e}')
            self.close()

    def close(self):
        if SSH.connected:
            try:
                self.client.close()
                logger.info(f'closed connection to port {self.port} on {self.ip}!')
                SSH.connected = False
            except Exception as e:
                logger.error(f'stop error! ==> {e}')

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def exec_command(self, cmd):
        stdin, stdout, stderr = self.client.exec_command(cmd)
        return stdout.read().decode('utf-8'), stderr.read().decode('utf-8')


if __name__ == '__main__':
    print('Hello world')
    # ip = '192.168.1.5'
    # port = 9022
    # username = 'root'
    # password = 'dandelion'
    # ssh = SSH(ip=ip, port=port, username=username, password=password)
    # ssh2 = SSH(ip=ip, port=port, username=username, password=password)
    # print(id(ssh), id(ssh2)
    # ip = '192.168.92.57'
    ip = '192.168.244.128'
    ssh = SSH(ip)
    stdout, stderr = ssh.exec_command('pwd')
    # ssh.sftp.mkdir('abcd')
    print(stdout, stderr)


