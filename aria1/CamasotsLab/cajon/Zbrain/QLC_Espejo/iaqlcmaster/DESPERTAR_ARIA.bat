@echo off
net session >nul 2>&1
if %errorLevel% neq 0 (
    powershell -Command "Start-Process '%~f0' -Verb RunAs"
    exit /b
)
title ARIA ZBRAIN OPERATOR [MAX_PRIVILEGE]
color 0B
:MENU
cls
echo =======================================================
echo     ARIA ZBRAIN [REF: LR-52] - ACCESO TOTAL
echo =======================================================
echo 1. DESPERTAR (Lanzar QLC+ / Universo 4)
echo 2. EXAMINAR (Explorar y Modificar Codigo)
echo 3. AMNESIA (Re-aprender / Reset de Registro)
echo 4. ESCALAR (Modo Rendimiento Maestro)
echo 5. SALIR
echo =======================================================
set /p opt="Seleccione mision (1-5): "

if "%opt%"=="1" start /realtime "" "C:\zbrain\camasotslab\iaqlcmaster\proyecto_master\ZBRAIN_MASTER_V1.qxw"
if "%opt%"=="2" start explorer "C:\zbrain\camasotslab\iaqlcmaster"
if "%opt%"=="3" call "C:\zbrain\camasotslab\iaqlcmaster\PROTOCOLO_AMNESIA.bat"
if "%opt%"=="4" powercfg /setactive e9a42b02-d5df-448d-aa00-03f14749eb61
if "%opt%"=="5" exit
goto MENU
