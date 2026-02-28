@echo off
title ARIA ZBRAIN BOOT
echo [ARIA]: Iniciando Sistema...
powershell -ExecutionPolicy Bypass -Command "(New-Object -ComObject Shell.Application).MinimizeAll()"
start notepad "C:\Zbrain\ACTIVO.txt"
exit
