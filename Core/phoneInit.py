# !/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# author: lucien
# package: phoneInit

import os
import subprocess

filePath = os.path.dirname(os.path.abspath("__file__"))
projectPath = os.path.dirname(filePath)


def localIP():  # 获取本机ip
    ipconfig = subprocess.Popen("ipconfig", shell=True, bufsize=1, stdout=subprocess.PIPE)
    while True:
        phoneText = ipconfig.stdout.readline().strip().decode('gbk')
        if 'IPv4 地址' in phoneText:
            ipaddress = phoneText.split(":", 1)[1].strip()
            print(ipaddress)
            break
    return ipaddress


def initPhone():  # 初始化atx到手机，需创建venv项目环境
    cmd = projectPath + f"\\venv\\Scripts\\python -m uiautomator2 init --server {localIP()}:9000"
    print(cmd)
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    p.communicate()
    # os.system(cmd)


if __name__ == '__main__':
    initPhone()
