@echo off
color a
title Release ATX_Server Port
echo ======================
echo ***     lucien     ***
echo ***     v1.0.0     ***
echo ======================
echo ---------------------------
echo Checking atx-server port...
for /F "usebackq tokens=5" %%a in (`"netstat -ano | findstr "9000""`) do (
if not "%%a" =="0" call :ReleasePort %%a
)
echo ---------------------------
echo atxserver port has been released!
echo ---------------------------


exit

:ReleasePort
TASKKILL /f /PID %1

exit