# -*- coding: utf-8 -*-

"""
@author: wuqi
@file: website_downloader.py
@time: 2022/2/7 20:00
@usage: 
"""

import os
import os.path
import requests
import urllib
import tkinter as tk
import tkinter.messagebox
from bs4 import BeautifulSoup, SoupStrainer

# 产生README 说明文件的函数，输入为一个文件夹目录的字符串，输出为该目录下所有文件的树形结构
# 以字符串的形式输出。主要是通过递归调用来实现。
BRANCH = '├─'
LAST_BRANCH = '└─'
TAB = '│  '
EMPTY_TAB = '   '
'''
variables:
input_website
input_max_pages
input_max_layers
'''


class TreeNode(object):
    # 通过__slots__来限制成员变量
    __slots__ = ("value", "children", "layer", "directory", "number")

    def __init__(self, value, layer, directory, number):
        self.value = value
        self.children = []
        self.layer = layer
        self.directory = directory
        self.number = number

    def get_value(self):
        return self.value

    def get_layer(self):
        return self.layer

    def get_directory(self):
        return self.directory

    # 返回节点的序号
    def get_number(self):
        return self.number

    # 插入子节点
    def insert_child(self, node):
        self.children.append(node)

    def pop_child(self):
        return self.children.pop(0)


layer_count = 1
website_count = 1
treenode_queue = []


# download the given website, generate html files and a readme file
def download_website():
    print(input_website.get(), input_max_pages.get(), input_max_layers.get(),
          btn_Group1.get(), btn_Group2.get())
    if not judge():
        print("fail to download")
    else:
        print("chect correct")
        # prepare for the result filefolder
        if not os.path.exists(r'D:\Download_Website'):
            os.makedirs(r'D:\Download_Website')

        download_img = False
        if (int(btn_Group1.get()) == 1):
            download_img = True
        # start to download websites
        global layer_count
        global website_count
        root_treenode = TreeNode(
            input_website.get(), layer_count,
            os.path.join(r"D:\Download_Website", str(website_count)),
            website_count)
        treenode_queue.append(root_treenode)
        print("----------第" + str(layer_count) + "层----------")
        # BFS, using a queue
        # 当队列不为空时，一直循环，直到入队的节点数目达到用户输入的数量时，return退出
        while treenode_queue:
            # 让队尾的节点出队，下载其html文件
            temp = treenode_queue.pop(0)
            print(temp.value, temp.directory, temp.number)
            if not os.path.exists(temp.directory):
                os.makedirs(temp.directory)
            re = requests.get(temp.get_value())
            # 注意需要进行编码，否则下载的 html 文件里的中文会乱码
            re.encoding = "utf-8"
            with open(
                    os.path.join(temp.directory, str(temp.number)) + ".html",
                    "w+",
                    encoding="utf-8") as html_file:
                html_file.write(re.text)
            # 判断用户是否勾选下载多媒体文件，主要使用urllib 的urlretrieve()来下载
            if download_img:
                # 用SoupStrainer 类来过滤html 文件里的img 标签
                soup = BeautifulSoup(
                    re.text, "html.parser", parse_only=SoupStrainer('img'))
                count = 1
                print("正在下载", temp.value, "的图片... ...")
                for img in soup:
                    if not (img["src"] == ""):
                        if str(img["src"][:2]) == r"//":
                            img["src"] = "https:" + img["src"]
                        img_dir = os.path.join(temp.directory, str(count))
                        if img["src"][-3:] == "png":
                            urllib.request.urlretrieve(img["src"],
                                                       img_dir + ".png")
                        elif img["src"][-3:] == "gif":
                            urllib.request.urlretrieve(img["src"],
                                                       img_dir + ".gif")
                        elif img["src"][-3:] == "jpg":  # jpg and other formats
                            urllib.request.urlretrieve(img["src"],
                                                       img_dir + ".jpg")
                        else:  # images which don't has a suffix
                            # 有些图片不带后缀，目前还无法下载下来，比如博客配图
                            print("Failed :", img["src"])
                        count = count + 1

            if (btn_Group2.get() == 2) or (int(
                    input_max_pages.get()) == 1) or (int(
                        input_max_layers.get()) == 1):
                break
            # 层数的判断出口，当下载的网页层数等于用户输入的层数时，退出
            if layer_count >= int(input_max_layers.get()) + 1:
                download_website_of_queue(*treenode_queue)
                with open(r"D:\Download_Website\README.txt",
                          "w+") as readme_file:
                    readme_file.write(get_dir_list(r"D:\Download_Website"))
                return
            # 接下来对于出队的节点使用 BeautifulSoup 和 SoupStrainer 来获取链接
            soup = BeautifulSoup(
                re.text, "html.parser", parse_only=SoupStrainer('a'))
            layer_count = layer_count + 1
            print("----------第" + str(layer_count) + "层----------")
            for each in soup:
                # 对于每个<a>标签中 href 的属性前四个字符是“http”的记录，首先输出其信息，然后构造节点将其入队，并且将其加入上方出队节点的 children 列表
                if each.has_attr("href") and each["href"][:4] == "http":
                    website_count = website_count + 1
                    print("第" + str(website_count) + "个网站/第" +
                          str(layer_count) + "层：" + each["href"])
                    anode = TreeNode(
                        each["href"], layer_count,
                        os.path.join(temp.directory, str(website_count)),
                        website_count)
                    temp.insert_child(anode)
                    treenode_queue.append(anode)
                    if website_count >= int(input_max_pages.get()):
                        download_website_of_queue(*treenode_queue)
                        # finally generate README.txt file
                        # 发现下载数目够了的时候，调用函数下载队列中的所有节点的 html 文件，然后生成README文件，记录输出文件夹中的树形结构
                        with open(r"D:\Download_Website\README.txt",
                                  "w+") as readme_file:
                            readme_file.write(
                                get_dir_list(r"D:\Download_Website"))
                        return


# check whether input_website is valid
def judge():
    if (not input_max_pages.get().isdigit()) or (
            not 0 < int(input_max_pages.get()) < 51):
        tk.messagebox.showwarning(title='注意', message='最大下载页的数目为1-50，请重试 :(')
        return False
    elif (not input_max_pages.get().isdigit()) or (
            not 0 < int(input_max_layers.get()) < 11):
        tk.messagebox.showwarning(title='注意', message='最大下载层的数目为1-10，请重试 :(')
        return False
    else:
        try:
            con = requests.get(input_website.get())
        except requests.RequestException:
            tk.messagebox.showerror(title='注意', message='请求出错，请重试 :(')
        except requests.ConnectionError:
            tk.messagebox.showerror(title='注意', message='连接出错，请重试 :(')
        except Exception:
            tk.messagebox.showerror(title='注意', message='出错，请重试 :(')
        else:
            print("status_code:" + str(con.status_code))
            if con.status_code == 200:
                return True
            else:
                return False


def download_website_of_queue(*args):
    download_img = False
    if (int(btn_Group1.get()) == 1):
        download_img = True
    # 函数的输入是一个列表，对于队列中的每个节点，下载其html 文件
    for temp in args:
        re = requests.get(temp.get_value())
        re.encoding = "utf-8"
        if not os.path.exists(temp.directory):
            os.makedirs(temp.directory)
        with open(
                os.path.join(temp.directory, str(temp.number)) + ".html",
                "w+",
                encoding="utf-8") as html_file:
            html_file.write(re.text)

        if download_img:
            soup = BeautifulSoup(
                re.text, "html.parser", parse_only=SoupStrainer('img'))
            count = 1
            print("正在下载", temp.value, "的图片... ...")
            for img in soup:
                if not (img["src"] == ""):
                    if str(img["src"][:2]) == r"//":
                        img["src"] = "https:" + img["src"]
                    img_dir = os.path.join(temp.directory, str(count))
                    if img["src"][-3:] == "png":
                        urllib.request.urlretrieve(img["src"],
                                                   img_dir + ".png")
                    elif img["src"][-3:] == "gif":
                        urllib.request.urlretrieve(img["src"],
                                                   img_dir + ".gif")
                    elif img["src"][-3:] == "jpg":  # jpg and other formats
                        urllib.request.urlretrieve(img["src"],
                                                   img_dir + ".jpg")
                    else:  # images which don't has a suffix
                        print("Failed :", img["src"])
                    count = count + 1


# open the result file folder in D:
def open_file():
    if not os.path.exists(r'D:/Download_Website/Download_Website'):
        os.makedirs(r'D:/Download_Website/Download_Website')
    os.system(r"start explorer D:\Download_Website\Download_Website")


def get_dir_list(path, placeholder=''):
    # 列出输入目录下的文件/文件夹，如果是文件夹，则加入folder_list 列表
    folder_list = [
        folder for folder in os.listdir(path)
        if os.path.isdir(os.path.join(path, folder))
    ]
    # 列出输入目录下的文件/文件夹，如果是文件，则加入file_list 列表
    file_list = [
        file for file in os.listdir(path)
        if os.path.isfile(os.path.join(path, file))
    ]
    result = ''
    # 对于文件夹列表中的第一个到倒数第二个元素，添加一个branch，然后递归调用直到
    # 最深的第一个子文件夹，里面只有文件，然后开始加入第一个到倒数第二个文件，
    # 直到添加完该文件夹的最后一个文件，依次类推，直到根目录文件夹的最深的最后
    # 一个子文件夹里的最后一个最后一个文件，递归才结束
    for folder in folder_list[:-1]:
        result += placeholder + BRANCH + folder + '\n'
        result += get_dir_list(os.path.join(path, folder), placeholder + TAB)
    if folder_list:
        result += placeholder + (BRANCH if file_list else
                                 LAST_BRANCH) + folder_list[-1] + '\n'
        result += get_dir_list(
            os.path.join(path, folder_list[-1]),
            placeholder + (TAB if file_list else EMPTY_TAB))
    for file in file_list[:-1]:
        result += placeholder + BRANCH + file + '\n'
    if file_list:
        result += placeholder + LAST_BRANCH + file_list[-1] + '\n'
    return result


root = tk.Tk()
root.title("网站下载工具  by:cde")
root.geometry('300x360')
tk.Label(
    root, text='要下载的网址：').grid(
        row=1, column=1, columnspan=2, padx=10, pady=10)
input_website = tk.Entry(root)
input_website.grid(row=1, column=3, columnspan=2)

tk.Label(
    root, text='最大下载页：').grid(
        row=2, column=1, columnspan=2, sticky=tk.W, padx=10, pady=10)
input_max_pages = tk.Spinbox(root, from_=1, to=50)
input_max_pages.grid(row=2, column=3, columnspan=2)
tk.Label(
    root, text='最大下载层：').grid(
        row=3, column=1, columnspan=2, sticky=tk.W, padx=10, pady=10)
input_max_layers = tk.Spinbox(root, from_=1, to=10)
input_max_layers.grid(row=3, column=3, columnspan=2)

tk.Label(
    root, text='下载多媒体文件：').grid(
        row=4, column=1, columnspan=2, sticky=tk.W, padx=10, pady=10)
tk.Label(
    root, text='下载其他网页：').grid(
        row=5, column=1, columnspan=2, sticky=tk.W, padx=10, pady=10)
btn_Group1 = tk.IntVar()
btn_Group2 = tk.IntVar()
btn_Group1.set(2)
btn_Group2.set(2)
tk.Radiobutton(
    root, variable=btn_Group1, text='是', value=1).grid(
        row=4, column=3)
tk.Radiobutton(
    root, variable=btn_Group1, text='否', value=2).grid(
        row=4, column=4)
tk.Radiobutton(
    root, variable=btn_Group2, text='是', value=1).grid(
        row=5, column=3)
tk.Radiobutton(
    root, variable=btn_Group2, text='否', value=2).grid(
        row=5, column=4)
start_button = tk.Button(root, text=' 开始下载 ', command=download_website)
start_button.grid(row=7, column=1, columnspan=4, padx=10, pady=15, sticky=tk.S)
open_button = tk.Button(root, text=' 打开下载文件夹 ', command=open_file)
open_button.grid(row=8, column=1, columnspan=4, padx=10, pady=15, sticky=tk.S)
root.mainloop()
