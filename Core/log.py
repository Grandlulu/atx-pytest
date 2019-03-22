#!/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# author：Lucien
# 基础包: Log日志封装

import logging
from logging import handlers


class Logs(object):
    level_mapping = {
        'debug': logging.DEBUG,
        'info': logging.INFO,
        'warning': logging.WARNING,
        'error': logging.ERROR,
        'critical': logging.CRITICAL
    }  # 日志映射

    def __init__(self, filename, level='info', when='D', backCount=3,
                 fmt='%(asctime)s - [line:%(lineno)d] - %(levelname)s: %(message)s'):
        self.logger = logging.getLogger(filename)
        format_str = logging.Formatter(fmt)  # 设置格式
        self.logger.setLevel(self.level_mapping.get(level))  # 设置级别
        self.logger.propagate = False  # 关闭logger向上级传输
        stream = logging.StreamHandler()  # 流形式向屏幕输出
        stream.setFormatter(format_str)  # 流的显示的格式
        file = handlers.TimedRotatingFileHandler(filename=filename, when=when, backupCount=backCount,
                                                 encoding='utf-8')  # 往文件里写入
        # Calculate the real rollover interval, which is just the number of
        # seconds between rollovers.  Also set the filename suffix used when
        # a rollover occurs.  Current 'when' events supported:
        # S 秒
        # M 分
        # H 小时
        # D 天
        # W 每星期（interval==0时代表星期一）
        # midnight 凌晨
        file.setFormatter(format_str)  # 设置文件里写入的格式
        self.logger.addHandler(stream)  # 把对象加到logger里
        self.logger.addHandler(file)  # 把对象加到logger里

    def Logger(self):
        return self.logger

if __name__ == '__main__':
    log = Logs('logs').Logger()
    log.info('hello')
