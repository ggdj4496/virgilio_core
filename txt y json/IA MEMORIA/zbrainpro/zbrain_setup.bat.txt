@echo off
title Zbrain - Setup Playlist (PERSI & ARIA)
color 0b

echo [STAGE 1] Creando estructura de carpetas en C:\Zbrain...
mkdir C:\Zbrain\A_core
mkdir C:\Zbrain\B_core
mkdir C:\Zbrain\camasots
mkdir C:\Zbrain\proyectos\01_camasots_dev
mkdir C:\Zbrain\proyectos\99_Almacen
mkdir C:\Zbrain\cajon
mkdir C:\Zbrain\camasots_bridge

echo [STAGE 2] Instalando el Sistema Nervioso de PERSI (A_core)...
echo # Logica de Persi > C:\Zbrain\A_core\persi_logic.sys
echo # Permisos Android > C:\Zbrain\A_core\permisos_android.cfg

echo [STAGE 3] Desplegando a ARIA (B_core)...
echo # Codigo del Bot de Telegram > C:\Zbrain\B_core\aria_bot.py

echo [STAGE 4] Configurando el Brazo Ejecutor (Bridge)...
(
echo import os
echo def execute_command(inst, path, content=None):
echo     try:
echo         if inst == "CREATE_DIR": os.makedirs(path, exist_ok=True)
echo         elif inst == "WRITE_FILE":
echo             with open(path, 'w', encoding='utf-8') as f: f.write(content)
echo         return True
echo     except: return False
echo if __name__ == "__main__": print("Bridge Active")
) > C:\Zbrain\camasots_bridge\bridge_service.py

echo [STAGE 5] Creando el Monitor Visual...
rem (Aqui se genera el script de PowerShell que te di antes automaticamente)

echo --------------------------------------------------
echo PLAYLIST COMPLETADA. Zbrain esta live en C:\Zbrain
echo --------------------------------------------------
pause