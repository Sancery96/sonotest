# -*- coding:utf-8 -*-
"""
@author:204280
@file:remote_scrot.py
@time:2022/02/07
"""
from PIL import Image
from CustomLibrary.public import public
import os

def _get_scort_picture(ssh, imageName):
    remote_dir = "/home/tony/VistaSB/proj/start/02-data/rw/autotest/picture/"
    flag = ssh.command("test -d %s && echo 'True' || echo 'False' " % remote_dir)
    flag = flag[0].strip()
    if flag == "False":
        ssh.command("mkdir %s" % remote_dir)
    remote_image = remote_dir + "tmp.png"
    ssh.command(
        "export DISPLAY=:0 && scrot " + remote_image)
    local_image_path = os.path.join(os.getcwd(), imageName)
    local_dir = os.path.split(local_image_path)[0]
    if not os.path.exists(local_dir):
        os.makedirs(local_dir)
    ssh.getFile(remote_image, local_image_path)
    return local_image_path

def view_image(local_image_path):
    with Image.open(local_image_path) as img:
        img.show()


def scort(ssh, imageName="./image/screenshot.jpg", width="800px"):
    """
    Takes a screenshot in JPEG format and embeds it into the log file.
    :param ssh:
    :param imageName: ./image/imageName
    :return:
    """
    local_image_path = _get_scort_picture(ssh, imageName)
    view_image(local_image_path)
    # self._embed_screenshot(imageName, width)
    return imageName


if __name__ == '__main__':
    ssh = public().ssh_connect("192.168.93.135")
    scort(ssh)
