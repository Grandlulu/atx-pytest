# !/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# author: lucien
# package:
import allure
import time


class Test_groupCall():
    @allure.feature("group_call")
    @allure.story("login")
    def test001_login(self, connectDevice):
        '''登入选择单位'''
        time.sleep(3)
        for i in range(50):
            connectDevice(className="android.widget.Button", resourceId="cn.vsx.vc:id/ptt").long_click(duration=1)
        # time.sleep(1)
        # connectDevice(className="android.widget.LinearLayout", resourceId="cn.vsx.vc:id/bv_setting").click(timeout=2)
        # time.sleep(1)
        # connectDevice(className="android.widget.TextView", text="日志上传").drag_to(className="android.widget.TextView",
        #                                                                         text="PTT快捷键",
        #                                                                         duration=2)
        # time.sleep(1)
        # connectDevice(className="android.widget.TextView", text="退出系统").click(timeout=None)
        # time.sleep(1)
        # connectDevice(className="android.widget.Button", text="确定").click()

