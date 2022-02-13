# -*- coding: utf-8 -*-

"""
@author: wuqi
@file: diffutil.py
@time: 2022/2/5 22:46
@usage: 
"""

import difflib

from public.utils.fileutil import FileUtil

if __name__ == '__main__':
    print('Hello world')
    from public.ssh_client import SSH
    print('Hello world')
    ssh = SSH()
    file = FileUtil(ssh)

    # 对比两个指定文件
    content1 = file.get_content('/home/tony/02-data/series/ro/measure/config/measure/xmlconfig/measurement/Menu/Default/MeaMenu_B.xml')
    content2 = file.get_content('/home/tony/02-data/series/ro/measure/config/measure/xmlconfig/measurement/Menu/Default/MeaMenu_C.xml')
    print(content1)
    print(content2)
    html_content = difflib.HtmlDiff().make_file(content1, content2)
    with open('diff1.html', 'w', encoding='utf-8') as f:
        f.write(html_content)

    # 对比两个指定目录
    # content1 = ssh.exec_command('tree /home/tony/02-data/series/ro/measure/config/measure/xmlconfig/measurement/Menu/Default/MeaMenu_B.xml')[0]
    # content2 = ssh.exec_command('tree /home/tony/02-data/series/rw/measure/config/measure/xmlconfig/measurement/Menu/Default/MeaMenu_C.xml')[0]
    # print(content1)
    # print(content2)
    # html_content = difflib.HtmlDiff().make_file(content1, content2)
    # with open('diff1.html', 'w', encoding='utf-8') as f:
    #     f.write(html_content)