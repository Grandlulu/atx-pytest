# !/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# author: lucien
# package:

import subprocess
import requests
import json
import time


def getDevices():  # 从ATX-Server获取设备列表IP
    devices_list = []
    try:
        res = requests.get(url="http://127.0.0.1:9000/list")
        result = json.loads(res.content)
        for i in range(len(result)):
            if result[i]["present"] == True:
                devices_list.append(result[i]["ip"])
            else:
                pass
        print(f"devices_list is {devices_list}")
        print(f"devices_list len is {len(devices_list)}")
    except:
        time.sleep(1)
        print('reconnect device in 1 sec')
        getDevices()
    return devices_list


def getPhoneInfo(devicesIP):  # 从IP信息获取手机信息
    res = requests.get(url="http://127.0.0.1:9000/list")
    result = json.loads(res.content)
    connPhone_list = []
    connPhone_IP = []
    PhoneInfo = {"ip": "",
                 "version": "",
                 "serial": "",
                 "brand": "",
                 "model": "",
                 "present": "",
                 "battery": ""}
    for i in range(len(result)):  # 判断在线状态并添加设备列表和在线IP列表
        if result[i]["present"] == True:
            connPhone_list.append(result[i])
            connPhone_IP.append(connPhone_list[i]["ip"])
        else:
            pass

    print(f"phone list is {connPhone_list}")
    print(f"connected devices IP are {connPhone_IP}")

    if devicesIP in connPhone_IP:  # 返回对应ip想要的设备信息
        for i in range(len(connPhone_list)):
            if devicesIP == connPhone_list[i]["ip"]:
                PhoneInfo["ip"] = connPhone_list[i]["ip"]
                PhoneInfo["version"] = connPhone_list[i]["version"]  # Android版本
                PhoneInfo["serial"] = connPhone_list[i]["serial"]  # 设备名
                PhoneInfo["brand"] = connPhone_list[i]["brand"]  # 品牌
                PhoneInfo["model"] = connPhone_list[i]["model"]  # 型号
                PhoneInfo["battery"] = connPhone_list[i]["battery"]["level"]  # 电池
                PhoneInfo["present"] = connPhone_list[i]["present"]  # 在线状态
    else:
        print("no ip match")
    return PhoneInfo



if __name__ == '__main__':
    print(getPhoneInfo('192.168.0.116'))
    # print(deviceChecker(1))
