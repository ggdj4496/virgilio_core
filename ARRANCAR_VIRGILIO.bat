@echo off
title VIRGILIO MONITOR
cd /d C:\VIRGILIO_CORE
echo [+] Cargando entorno...
set VIRGILIO_TOKEN=%VIRGILIO_TOKEN%
python MONITOR.py
pause