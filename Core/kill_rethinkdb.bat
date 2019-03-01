@echo off
color a
title Release rethinkdb Port
echo ======================
echo ***     lucien     ***
echo ***     v1.0.0     ***
echo ======================
echo ---------------------------
echo Checking rethinkdb port...
for /F "usebackq tokens=5" %%a in (`"netstat -ano | findstr "8090""`) do (
if not "%%a" =="0" call :ReleasePort %%a
)
echo ---------------------------
echo rethinkdb port has been released!
echo ---------------------------


exit

:ReleasePort
TASKKILL /f /PID %1

exit