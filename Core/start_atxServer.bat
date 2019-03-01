@echo off
color a
title start ATX_Server
echo ======================
echo ***     lucien     ***
echo ***     v1.0.0     ***
echo ======================
C:
CD %HomePath%\go\src\github.com\openatx\atx-server\
echo
echo 
echo --------启动服务------------
start /b atx-server --port 9000
