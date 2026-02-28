@echo off
title ARIA ZBRAIN OPERATOR
color 0B
:MENU
cls
echo =======================================================
echo     ARIA ZBRAIN [REF: LR-52] - PANEL DE OPERACIONES
echo =======================================================
echo 1. DESPERTAR (Lanzar QLC+ y Universo 4)
echo 2. RE-ANALIZAR (Limpieza y Optimizacion)
echo 3. BACKUP (Copia de Seguridad iaqlcmaster)
echo 4. RE-PARAR (Reset de Energia y Latencia)
echo 5. SALIR
echo =======================================================
set /p opt="Seleccione mision (1-5): "

if "%opt%"=="1" start "" "C:\zbrain\camasotslab\iaqlcmaster\proyecto_master\ZBRAIN_MASTER_V1.qxw"
if "%opt%"=="2" powershell -Command "Write-Host 'Analizando...' -Fore Cyan"
if "%opt%"=="3" robocopy "C:\zbrain\camasotslab\iaqlcmaster" "C:\zbrain\BACKUP_ARIA" /MIR
if "%opt%"=="4" powercfg /SETACTIVE SCHEME_CURRENT
if "%opt%"=="5" exit
goto MENU
