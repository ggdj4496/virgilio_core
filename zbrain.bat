@echo off
title Zbrain Core - Instalacion de Sistema
color 0B
set "base=C:\Zbrain"

echo ======================================================
echo          INICIALIZANDO ZBRAIN CORE Y ZLAB
echo ======================================================
echo.

:: Crear Estructura Core (Tu Cerebro)
echo [+] Creando Nucleo de Memoria...
mkdir "%base%\Core\System" 2>nul
mkdir "%base%\Core\IA_Personality" 2>nul
mkdir "%base%\Core\User_Personality" 2>nul
mkdir "%base%\Core\Knowledge_Base" 2>nul

:: Crear Estructura Zlab (Produccion y Camasots)
echo [+] Configurando Laboratorio de Desarrollo (Zlab)...
mkdir "%base%\Zlab\Camasots\Zbrain_Projects" 2>nul
mkdir "%base%\Zlab\Camasots\Recursos\Iconos" 2>nul
mkdir "%base%\Zlab\Camasots\Recursos\PNG_Gobos" 2>nul
mkdir "%base%\Zlab\Camasots\Addons_Tools" 2>nul
mkdir "%base%\Zlab\Camasots\Backlog_Ideas" 2>nul
mkdir "%base%\Zlab\Camasots\Hardware_Dev\FTDI_Drivers" 2>nul
mkdir "%base%\Zlab\Camasots\Hardware_Dev\PCB_Designs" 2>nul
mkdir "%base%\Zlab\Camasots\Hardware_Dev\CNC_GCode" 2>nul

:: Crear Archivos de Registro Inicial
echo Fecha: %date% %time% > "%base%\Core\IA_Personality\log_nacimiento.txt"
echo Estado: Agente Permanente Activo >> "%base%\Core\IA_Personality\log_nacimiento.txt"
echo Perfil: Usuario Profesional - Sin Censura - Aprendizaje Continuo > "%base%\Core\User_Personality\perfil.txt"

echo.
echo ======================================================
echo    INSTALACION COMPLETADA. ZBRAIN ESTA LISTO.
echo ======================================================
pause
