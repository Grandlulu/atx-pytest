# !/usr/bin/python3.7
# -*- coding: UTF-8 -*-
# author: lucien
# package: server

import os
import time
import subprocess

serverPath = os.path.dirname(os.path.abspath("__file__"))


class atx_server():

    def start_server(self, serverPath):  # 启动rethinkdb和atxserver服务
        try:
            if atx_server.isRunning():
                print("Server already run")
                pass
            else:
                start_rethinkdb = "start /b rethinkdb --http-port 8090"
                subprocess.run(start_rethinkdb, shell=True)
                time.sleep(3)
                subprocess.run(serverPath + "\start_atxServer.bat", shell=True)
        except:
            print("-----------starting server------------")
            time.sleep(5)
            self.start_server(self, serverPath)

    def stop_server(self, serverPath):  # 停止rethinkdb和atxserver服务
        os.system(serverPath + "\kill_rethinkdb.bat")
        time.sleep(1)
        os.system(serverPath + "\kill_atxServer.bat")

    def restart_server(self, serverPath):  # 重新启动server
        self.stop_server(serverPath)
        time.sleep(3)
        self.start_server(serverPath)

    @staticmethod
    def isRunning():
        '''
        :return: True or False
        '''
        try:
            process = len(os.popen('netstat -ano|findstr "0.0.0.0:9000"').readlines())
            print(f"server starting take {process} processes")
            if process >= 1:
                print("atx server started")
                return True
            else:
                return False
        except:
            print("Check process ERROR!!!")
            return False


if __name__ == '__main__':
    a = atx_server()
    a.start_server(serverPath)
    # a.stop_server()
