# !/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# author: lucien
# package: run

from concurrent.futures import ProcessPoolExecutor
from Core.deviceInfo import *
import pytest
from Core.server import *
import requests
import json

filePath = os.path.dirname(os.path.abspath("__file__"))
serverPath = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "Core")
projectPath = os.path.dirname(filePath)


def deviceChecker(connectNum=None):  # 检查服务启动和设备连接
    '''

    :param connectNum: number of device how much want to test
    :return: None
    '''
    if len(getDevices()) == connectNum:
        print("devices are ready")
    else:
        print(f"we need test {connectNum} devices")
        print(f"now connected {len(getDevices())}")
        print("waiting 5 sec connect server and devices")
        time.sleep(5)
        deviceChecker(connectNum)


def runnerPool(deviceIP_list):  # 启动多进程运行测试
    with ProcessPoolExecutor(len(getDevices())) as pool:
        pool.map(runPytest, deviceIP_list)


def runPytest(device_IP):  # 运行测试
    Phone = getPhoneInfo(device_IP)
    print("----------start running test-------------")
    print(f"sent cmdopt is {Phone['ip']}")
    report = f"report-{Phone['serial']}"
    try:
        os.system(f"del /s /q " + projectPath + f"\\{report}")
        time.sleep(1)
        os.system(f"rd /s /q " + projectPath + f"\\{report}")
        time.sleep(1)
        print(f"{report} report has deleted")
    except:
        print("error occur")
    else:
        print(f"pool run device is {Phone['serial']}")
        pytest.main(["../TestCases/", f"--cmdopt={Phone['ip']}", "--alluredir", f"../{report}/xml"])
        time.sleep(1)
        os.system(f"allure generate ../{report}/xml -o ../{report}/html")


if __name__ == '__main__':
    server = atx_server()
    server.start_server(serverPath)
    deviceChecker(2)
    runnerPool(getDevices())
