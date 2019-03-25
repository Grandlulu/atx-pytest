# !/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# author: lucien
# package:
import allure
import time
import pytest


class Test_groupCall():
    @pytest.mark.repeat(5)
    @allure.feature("group_call")
    @allure.story("login")
    def test001_login(self, connectDevice):
        '''登入选择单位'''
        connectDevice(className="android.widget.Button", resourceId="cn.vsx.vc:id/ptt").long_click(duration=2, timeout=10)
        assert connectDevice(resourceId="cn.vsx.vc:id/ptt", text="按住 说话").exists
        # connectDevice(className="android.widget.Button", resourceId="cn.vsx.vc:id/ptt").touch.up()

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
        connectDevice()
