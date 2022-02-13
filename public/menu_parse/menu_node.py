# -*- coding: utf-8 -*-

"""
@author: wuqi
@file: menu_node.py
@time: 2022/2/9 20:27
@usage: 测量菜单节点定义
"""
from public.ssh_client import SSH
from public.utils.fileutil import FileUtil
from public.utils.xmlutil import XMLUtil
from public.config.path_config import *

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


def get_menu_path(mode):
    """
    mode : 'B' 'C' 'D' 'M' 'E'
    """
    mode = mode.upper().replace(' ', '')
    if mode in ['B', 'C', 'PW', 'CW', 'M', 'ELASTO', '3D4D', '3D4DC']:
        if mode in ['PW', 'CW']:
            menu_filename = 'MeaMenu_D.xml'
        elif mode == 'ELASTO':
            menu_filename = 'MeaMenu_E.xml'
        elif mode == '3D4D':
            menu_filename = 'MeaMenu_3DB.xml'
        elif mode == '3D4DC':
            menu_filename = 'MeaMenu_3DC.xml'
        else:
            menu_filename = f'MeaMenu_{mode}.xml'
    else:
        menu_filename = 'MeaMenu_B.xml'
    print(menu_filename)
    return mea_menu_root_path + menu_filename


def get_comb_path(mea_item_name):
    # print(comb_root_path + name + '.xml')
    return mea_comb_root_path + mea_item_name + '.xml'


def get_remote_xml_tree_root_by_path(ssh, filepath):
    file_content = FileUtil(ssh).get_content(filepath)
    root = ET.fromstring(file_content)
    return root


def get_pnode_by_name(root, pname):
    return root.find(f".//*[@Name='{pname}']")


class MeaNode:
    """
    测量配置文件节点基类
    """

    def __init__(self, ssh):
        self.ssh = ssh
        self.attribs = {}
        self.type = ''
        self.title = ''
        self.name = ''
        self.children = []
        self.index = 0
        self.page = -1
        self.pos = -1  # 触摸屏显示位置
        self.root = None

    @staticmethod
    def has_attr(node, attr):
        if attr in node.attribs:
            return True
        return False

    def display(self):
        print(f'----------------{self.type}------------------->>')
        print(f'{self.name} ===> {self.title}')
        for child in self.children:
            child.display()

    def parse(self, pnode):
        index = 0
        node_list = []
        for node in pnode:
            m_node = __class__(ssh)
            m_node.index = index
            m_node.attribs = node.attrib
            for attr in ['Name', 'Page', 'Pos', 'Type', 'Title']:
                if attr in node.attrib:
                    exec(f"m_node.{attr.lower()} = node.attrib['{attr}']")
            m_node.children = self.parse(node)
            node_list.append(m_node)
            index += 1
        return node_list

    def parse_by_pname(self, root, pname):
        '''
        根据父节点Name属性，解析测量菜单
        :param root:
        :type root:
        :param pname:
        :type pname:
        :return:
        :rtype:
        '''
        pnode = get_pnode_by_name(root, pname)
        return self.parse(pnode)


"""
    print('\n通过xpath，获取指定属性的所有节点')
    for child in root.findall('.//*[@name="Abdomen"]'):
        print(child.tag, child.attrib['name'])
    print('\n通过xpath，获取指定属性A下，标签为B的所有节点')
    for child in root.findall('.//*[@name="Abdomen"]/ComboBox'):
        print(child)
"""


class Command(MeaNode):
    """
    Combine文件中的Command标签
    """

    def __init__(self, ssh):
        super().__init__(ssh)
        self.id = 0
        self.index = -1
        self.repeat = 1
        self.text = ['']

    def _gen_command_dict(self, dir=mea_comb_root_path):
        path_list = FileUtil(self.ssh).get_remote_filenames_in_dir(dir, '.xml$')
        cmd_list = []
        for filepath in path_list:
            try:
                command_tree_root = self.get_xml_content_by_remote_path(filepath)
                for cmd in command_tree_root.findall('CommandList/Command'):
                    cmd_list.append(cmd.text)
            except Exception as e:
                print(e, filepath)
                continue
        for cmd in set(cmd_list):
            if cmd is not None:
                print("'%s' : %d," % (cmd, 2))


class MeaItem(MeaNode):
    """
    测量项
    """

    def __init__(self, ssh):
        super().__init__(ssh)
        self.type = 'KW_ITEM'
        self.comb = -1
        self.option = -1
        self.command = []

    def get_item_method(self):
        """
        获取测量项当前所用的测量方法
        若菜单配置文件中，存在属性Optional=1，则表示该测量项为多方法测量项
        先从MenuMemory.xml中进行查找，未找到，则默认发起第一个方法
        :param ssh:
        :type ssh:
        :return:
        :rtype:
        """
        # get method of item
        # 获取测量项当前的测量方法
        method = 0
        if self.option == 1:
            menu_memory_filepath = ''
            menu_memory_file_content = FileUtil(self.ssh).get_content(menu_memory_filepath)
            mem_tree_root = XMLUtil().get_xml_root_by_string(menu_memory_file_content)
            for item in mem_tree_root.findall('Type/Item'):
                if self.name == item.attrib['name']:
                    method = int(item.attrib['index'])
                elif self.name + str(self.comb) == item.attrib['name']:
                    method = int(item.attrib['index'])
        return method

    def get_command_list(self, filename):
        # get all commands in current file
        """
        获取Combine文件CommandList标签下的Command列表
        :param filename:
        :type filename:
        :return:
        :rtype:
        """
        command_list = []
        comb_path = self.get_comb_path(filename)

        comb_tree_root = self.get_xml_content_by_remote_path(comb_path)
        id = 0
        for cmd_item in comb_tree_root.findall("CommandList/Command"):
            # print(_.attrib)
            command = Command(self.ssh)
            command.id = id
            command.text = cmd_item.text
            if 'Index' in cmd_item.attrib:
                command.index = int(cmd_item.attrib['Index'])
            if 'Repeat' in cmd_item.attrib:
                command.repeat = int(cmd_item.attrib['Repeat'])
                command.text = [cmd_item.text for i in range(command.repeat)]
            command_list.append(command)
            id += 1
        return command_list

    def get_item_command_list(self):
        # get all commands of item
        filename = self.name
        method = self.get_item_method()
        if self.comb == -1:
            command = self.get_command_list(filename)[method]
        else:
            if self.option == -1:
                command = self.get_command_list(filename)[self.comb]
            else:
                command = [c for c in self.get_command_list(filename) if self.comb == c.index][method]  # 血流量
        print(command.text)
        if command.text is None:
            new_filename = filename + '_' + str(method + 1)
            command.text = [c.text for c in self.get_command_list(new_filename)]
            # print(_.text)
        # print(command.text)
        return command


class MeaGroup(MeaNode):
    def __init__(self, ssh):
        MeaNode.__init__(self, ssh)
        self.type = 'KW_GROUP'


class MeaApp(MeaNode):
    def __init__(self, ssh):
        MeaNode.__init__(self, ssh)
        self.type = "KW_APP"


class MeaAppGroup(MeaNode):
    def __init__(self, ssh):
        super().__init__(ssh)
        self.type = "KW_APPGROUP"


if __name__ == '__main__':
    print('Hello world')
    path = get_menu_path('C')
    ssh = SSH()
    content = FileUtil(ssh).get_content(path)
    # print(content)
    # print(ssh.exec_command(f'cat {path}'))

    root = get_remote_xml_tree_root_by_path(ssh, path)
    appgroup_root = root.find(".//Node[@Name='Calc']")
    # appgroup_root = root.find(".//Node[@Name='KW_PAEDIATRICS']")
    # appgroup_list = parse_mea_appgroup(root)

    # MeaAppGroup(ssh).parse(root)
    # appgroup_list =MeaAppGroup(ssh).parse(appgroup_root)
    appgroup_list = MeaAppGroup(ssh).parse_by_pname(root, pname='Calc')
    # appgroup_list =MeaAppGroup(ssh).parse(root, p_name='Calc')
    print(appgroup_list)
    for appgroup in appgroup_list:
        appgroup.display()
        # print(appgroup.name, appgroup.pos, appgroup.children[0].name, appgroup.attribs)
        # print(appgroup.children[0].name)
        # for k, v in appgroup.__dict__.items():
        #     print(k, v)

    # item = MeaItem(ssh)
    # group = MeaGroup(ssh)
    # item.name = 'KW_CARDIAC_LV_SIMP'
    # item.comb = 1
    # item.option = 1
    # method = item.get_item_method()
    # print(method)
    # command = item.get_item_command_list()
    # print(command.text)
