# -*- coding: utf-8 -*-

"""
@author: wuqi
@file: xmlutil.py
@time: 2022/2/2 11:03
@usage: 
"""

try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET


class XMLUtil:

    def __init__(self):
        pass

    def get_xml_root_by_string(self, xmlstr):
        root = ET.ElementTree(ET.fromstring(xmlstr))
        return root

    def get_xml_root_by_path(self, filepath):
        tree = ET.parse(filepath)
        root = tree.getroot()
        return root

# 系统设置 基本设置和应用设置出厂配置
# 02-data\ro\measure\config\systemsetting\default\measure.xml
# extern_platform\measure\src\systemset\measure\KCalcEquationController.cpp
if __name__ == '__main__':
    print('Hello world')
    filepath = r'D:\Development\sonotest\public\utils\ro\measure\config\measure\xmlconfig\measurement\SysConfig\SysConfig2.xml'
    xmlstr = '''<?xml version="1.0"?>
                <Root cfgver="1">
                    <!--普通下拉框类配置-->
                    <ComboBox>
                        <Item name="MVelCrossLineDispaly" preset="KW_SYSSET_OFF">
                            <Avail name="KW_SYSSET_ON" />
                            <Avail name="KW_SYSSET_OFF" />
                        </Item>
                    </ComboBox>
                    <!--测量科室配置-->
                    <Dept name="Abdomen">
                        <!--下拉框类配置-->
                        <ComboBox>	
                            <!--2D模式冻结自动响应-->
                                <Item name="KW_2D_FREEZE_RESPONSE" preset="KW_FREEZE_TO_CINE">
                                    <Avail name="KW_FREEZE_TO_CINE" />
                                    <Avail name="KW_FREEZE_TO_ANNOT" />
                                </Item>
                            <!--D模式冻结自动响应-->
                                <Item name="KW_D_FREEZE_RESPONSE" preset="KW_FREEZE_TO_CINE">
                                    <Avail name="KW_FREEZE_TO_CINE" />
                                    <Avail name="KW_FREEZE_TO_ANNOT" />
                                </Item>
                            <!--M模式冻结自动响应-->
                                <Item name="KW_M_FREEZE_RESPONSE" preset="KW_FREEZE_TO_CINE">
                                    <Avail name="KW_FREEZE_TO_CINE" />
                                    <Avail name="KW_FREEZE_TO_ANNOT" />
                                </Item>
                                <Item>some content</Item>
                        </ComboBox>
                    </Dept>
                </Root>
            '''
    print('加载xml')
    # 1.从文件加载
    # tree = ET.parse(filepath)
    # root = tree.getroot()

    # 2.从字符串加载
    root = ET.fromstring(xmlstr)

    print('\n获取根节点')
    print(f'root对象:                      {root}\n'
          f'root.tag节点标签:               {root.tag}\n'
          f'root.attrib节点属性:            {root.attrib}\n'
          f'root.attrib["cfgver"]节点属性值:{root.attrib["cfgver"]}\n'
          f'root.text节点文本:              {root.text}'.strip())

    print('\n获取根节点的子节点（一级节点）')
    for child in root:
        print(f'child.tag:{child.tag}\tchild.attrib:{child.attrib}\tchild.text:{child.text}'.strip())

    print('\n获取根节点的子子节点（二级节点）')
    for subroot in root:
        for child in subroot:
            print(f'child.tag:{child.tag}\tchild.attrib:{child.attrib}\tchild.text:{child.text}'.strip())

    print('\n通过iter迭代器，获取指定标签的所有节点')
    for child in root.iter('Avail'):
        print(child.attrib['name'])
    print('\n通过xpath，获取指定标签的所有节点')
    for child in root.findall('.//Avail'):
        print(child.attrib['name'])
    print('\n通过xpath，获取指定标签的第一个节点')
    for child in root.findall('.//Avail[1]'):
        print(child.attrib['name'])

    print('\n通过xpath，获取指定属性的所有节点')
    for child in root.findall('.//*[@name="Abdomen"]'):
        print(child.tag, child.attrib['name'])
    print('\n通过xpath，获取指定属性A下，标签为B的所有节点')
    for child in root.findall('.//*[@name="Abdomen"]/ComboBox'):
        print(child)
    print('\n通过子节点的文本内容，获取父节点')
    for parent in root.findall('.//*[Item="some content"]'):
        print(parent)

    print('\n获取当前节点')
    childs = root.findall('.')
    print(childs)

    print('\nfindall()只能查找当前节点的所有子节点')
    childs = root.findall('Item')
    print(f'childs1:{childs}')
    childs = root.findall('Dept')
    print(f'childs2:{childs}')

    print('\nfind()只能查找当前节点下，第一个匹配的子节点')
    item = childs[0].find('item')
    print(f'item:{item}')
    combbox = childs[0].find('ComboBox')
    print(f'combbox:{combbox}')

    # 修改文本内容
    # child.text = 'xxx'
    # child.set('updated', 'yes')

    # 创建新节点
    # node = ET.Element('Node')
    # node.text = 'xxx'
    # child.append(node)  # 将node节点，添加到child节点之下

    # 删除节点
    # child.remove(node)