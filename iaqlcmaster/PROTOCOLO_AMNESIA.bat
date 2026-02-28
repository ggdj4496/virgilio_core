@echo off
title PROTOCOLO AMNESIA - REAPRENDIZAJE
color 0C
echo [ALERTA] Purgando memorias y configuraciones...
reg delete "HKEY_CURRENT_USER\Software\qlcplus" /f >nul 2>&1
if exist "%APPDATA%\qlcplus" rd /s /q "%APPDATA%\qlcplus"
echo [OK] El sistema ha olvidado. Listo para nueva programacion.
pause
exit
