# !/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# author: lucien
# package: TestCases

# !/usr/bin/python3.6
# -*- coding: UTF-8 -*-
# author: lucien
# package:  conftest

import pytest
import uiautomator2 as u2


def pytest_addoption(parser):  # 定义命令行传参参数
    parser.addoption("--cmdopt", action="store", default="device", help="None")


@pytest.fixture(scope="session")  # 命令行参数传递给pytest
def cmdopt(request):
    return request.config.getoption("--cmdopt")


@pytest.fixture(scope="session")  # 初始化开始连接设备
def connectDevice(cmdopt):
    address = cmdopt
    d = u2.connect(addr=address)
    d.set_fastinput_ime(True)
    driver = d.session("cn.vsx.vc")
    yield driver
    print("driver finished")
    driver.close()
