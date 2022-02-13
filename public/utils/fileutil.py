# -*- coding: utf-8 -*-

"""
@author: wuqi
@file: fileutil.py
@time: 2022/1/29 19:10
@usage: 
"""

import os
import stat

from public.log import logger

rootpath = os.path.join("\\".join(os.path.dirname(os.path.abspath('__file__')).split('\\')[:-1]), 'tmpfiles\\')


class FileUtil:
    def __init__(self, ssh):
        self.ssh = ssh
        self.sftp = ssh.sftp

    def get_content(self, remotepath):
        """
        获取远程文件内容
        :param remotepath: 远程文件绝对路径
        :type remotepath: str like file path
        :return: 远程文件内容
        :rtype: str
        """
        try:
            return self.ssh.exec_command(f'cat {remotepath}')[0]
        except Exception as e:
            logger.error(f'{e} --> {self.ssh.exec_command(f"cat {remotepath}")[1]}')

    def get_remote(self, remotepath, localpath=rootpath):
        """
        获取远程文件，或远程目录下的所有文件

        remotepath 不存在时，直接返回 False

        remotepath 为目录时，拷贝目录下所有文件到本地

        remotepath 为文件时，拷贝文件到本地

        localpath 为目录时，拷贝文件到目录下

        localpath 为文件时，拷贝并重命名文件到目录下

        :param remotepath: 远程文件路径，或目录
        :type remotepath:
        :param localpath: 本地保存文件名称，或保存路径
        :type localpath:
        :return: None
        :rtype:
        """
        # 远程文件不存在时，直接返回 False
        if not self.exists(remotepath):
            logger.error(f'file {remotepath} not exists')
            return False
        try:
            # remotepath 为目录时，拷贝目录下所有文件到本地
            if stat.S_ISDIR(self.sftp.lstat(remotepath).st_mode):
                self.get_remote_files(remotepath, localpath)
            # remotepath 为文件时，拷贝单个文件到本地
            else:
                self.get_remote_file(remotepath, localpath)
        except Exception as e:
            logger.error(e)

    def get_remote_file(self, remotepath, localpath=rootpath):
        """
        获取单个远程文件到本地

        localpath 为目录时，拷贝文件远程文件到目录下

        localpath 为文件时，拷贝并重命名文件到目录下

        :param remotepath: 远程文件路径
        :type remotepath:
        :param localpath: 本地文件路径
        :type localpath:
        :return: None
        :rtype:
        """
        localdir = os.path.dirname(localpath)
        # 若localpath 目录不存在，则先创建目录
        if not os.path.exists(localdir):
            os.makedirs(localdir)
        # 若localpath 为目录，本地文件名和远程文件同名
        # 若为绝对路径，用isdir判断
        # 若为相对路径，判断basename是否为空
        if os.path.isdir(localpath) or os.path.basename(localpath) == '':
            localpath = os.path.join(localpath, remotepath.split('/')[-1])
        try:
            self.sftp.get(remotepath, localpath)
            logger.info(f'get remote file {remotepath} to local {localpath} success!')
            return True
        except Exception as e:
            logger.error(f'get remote file {remotepath} to local {localpath} fail! ==> {e}')
            return False

    def get_remote_files(self, remotepath, localpath=rootpath):
        """
        获取远程目录下的所有文件到本地
        :param remotepath: 远程文件目录
        :type remotepath:
        :param localpath: 本地文件目录
        :type localpath:
        :return: None
        :rtype:
        """
        remotepath = remotepath.rstrip('/')
        for file in self.listdir_attr(remotepath):
            filename = file.filename
            remotefile = remotepath + '/' + filename
            localfile = os.path.join(localpath, filename)
            if stat.S_ISDIR(file.st_mode):
                # 如果是目录，则递归处理
                self.get_remote_files(remotefile, localfile)
            else:
                self.get_remote_file(remotefile, localfile)

    def get_remote_filenames_in_dir(self, dir, pattern='^-'):
        """
        获取远程目录下的文件名称列表
        :param dir:
        :type dir:
        :param pattern:
        :type pattern:
        :return:
        :rtype:
        """
        path_list = []
        cmd = 'ls -lh %s | grep %s' % (dir, pattern)
        # print(command)
        files = self.ssh.exec_command(cmd)
        if files[0] == '':
            logger.error(files[1]+self.__class__.__name__)
        else:
            for file in files[0].strip().split('\n'):
                # print(file)
                filepath = dir + file.split()[-1]
                # print(filepath)
                path_list.append(filepath)
        return path_list

    def put_remote(self, localpath, remotepath):
        """
        发送本地文件，或目录下的所有文件到远程目录

        localpath 为目录时，拷贝目录下所有文件到远程

        localpath 为文件时，拷贝并重命名单个文件到远程

        :param remotepath: 本地文件路径，或目录
        :type remotepath:
        :param localpath: 远程保存文件名称，或保存路径
        :type localpath:
        :return: None
        :rtype:
        """
        if not os.path.exists(localpath):
            logger.error(f'file {localpath} not exists')
            return False
        try:
            if os.path.isdir(localpath) or os.path.basename(localpath) == '':
                self.put_files_remote(localpath, remotepath)
            else:
                self.put_file_remote(localpath, remotepath)
        except Exception as e:
            logger.error(e)

    def put_file_remote(self, localpath, remotepath):
        """
        发送单个本地文件到远程

        remotepath 不存在时，先创建远程目录

        remotepath 为目录时，拷贝本地文件到该远程目录下

        remotepath 为文件时，拷贝并重命名文件到远程目录

        :param localpath: 本地文件路径
        :type localpath:
        :param remotepath: 远程文件路径
        :type remotepath:
        :return: None
        :rtype:
        """
        remotedir = os.path.dirname(remotepath)
        if not self.exists(remotedir):
            self.mkdir(remotedir)
        # 若remotepath 为目录，本地文件名和远程文件同名
        if self.isdir(remotepath):
            remotepath = remotepath + '/' + os.path.split(localpath)[-1]
        try:
            self.sftp.put(localpath, remotepath)
            logger.info(f'put file {localpath} to remote {remotepath} success!')
        except Exception as e:
            logger.error(f'put file {localpath} to remote {remotepath} fail! ==> {e}')

    def put_files_remote(self, localpath, remotepath):
        """
        发送本地目录下所有文件到远程
        :param localpath: 本地文件路径
        :type localpath:
        :param remotepath: 远程文件路径
        :type remotepath:
        :return: None
        :rtype:
        """
        if not self.exists(remotepath):
            self.mkdir(remotepath)
        for filename in os.listdir(localpath):
            remotefile = remotepath + '/' + filename
            localfile = os.path.join(localpath, filename)
            if os.path.isdir(localfile):
                # 如果是目录，则递归处理
                self.put_files_remote(localfile, remotefile)
            else:
                self.put_file_remote(localfile, remotefile)

    def stat(self, remotepath):
        """
        获取远程文件属性
        :param remotepath: 远程文件，或文件夹
        :type remotepath:
        :return: st_mode,st_size,st_gid,st_atime,st_mtime 通过xx.st_size调用
        :rtype:
        """
        return self.sftp.stat(remotepath)

    @staticmethod
    def isdir(remotepath):
        # print(ssh.exec_command(f'file {remotepath}')[0])
        return ssh.exec_command(f'file {remotepath}')[0].strip().endswith('directory')

    def exists(self, remotepath):
        """
        判断远程文件，或文件夹是否存在

        :param remotepath: 远程文件，或文件夹路径
        :type remotepath:
        :return: True/False
        :rtype:
        """
        return int(ssh.exec_command(f'test -d {remotepath} && echo 1 || echo 0')[0]) \
               or int(ssh.exec_command(f'test -f {remotepath} && echo 1 || echo 0')[0])

    def listdir(self, remotepath):
        return self.sftp.listdir(remotepath)

    def listdir_attr(self, remotepath):
        return self.sftp.listdir_attr(remotepath)

    def mkdir(self, remotepath, mode=0o777):
        self.sftp.mkdir(remotepath, mode)


if __name__ == '__main__':
    from public.ssh_client import SSH
    print('Hello world')
    ssh = SSH()
    file = FileUtil(ssh)
    if file.exists('/home/root1/__init__.py'):
        print('exist')
    else:
        print('not exist')

    file.put_remote(r'W:\Development\Sonoscape\pluto', '/home/tony/')
    # ssh.exec_command('tar -zxvf  /home/root1/pluto.zip')

    # file.mkdir('/home/root1/abx/')
    # file.get_remote('/home/root1', r'../tmp/')
    # file.get_remote('/home/root1/__init__.py', '../tmp/')
    # file.get_remote_file('/home/root1/__init__.py', '../tmp')
    # file.put_file_remote(r'D:\code\autotest\utils\__init__.py', '/home/root1/tmpf/init.py')
    # file.put_remote(r'W:\Development\Sonoscape\pluto\02-data\series', '/home/root1/wuq/02-data')
    # print(file.isdir('/home/root1/__init__.py'))
    # file.get_remote_files('/home/tony/VistaSB/proj/start/02-data/rw/autotest', './files')
    # file.put_files_remote(r'E:\部门文档\12 超声产品线\901-测量组\105-新员工培养\03-系统设计相关文档', '/tmp/media/sdb1/设计文档')
    # file.put_remote(r'D:\Development\auto_scan_bug_info-master.zip', '/tmp/media/sdb1/code/auto_scan_bug_info-master')

    # content = file.get_content(r'/home/root1/wuq/02-data/ro/measure/config/measure/xmlconfig/measurement/Menu/Library'
    #                            r'/MeaMenu_B.xml')
    # print(content.splitlines()[-1])
