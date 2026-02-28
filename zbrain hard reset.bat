@echo off
set "root=C:\Zbrain"

echo [Zbrain] Corrigiendo estructura y generando herramientas...

:: 1. Asegurar Carpetas
if not exist "%root%" mkdir "%root%"
mkdir "%root%\Core\System" 2>nul
mkdir "%root%\Core\IA_Personality" 2>nul
mkdir "%root%\Zlab\Camasots\Addons_Tools" 2>nul
mkdir "%root%\Zlab\Camasots\Recursos\PNG_Gobos" 2>nul
mkdir "%root%\Zlab\Camasots\Zbrain_Projects" 2>nul

:: 2. Generar el script de Sincronizacion de Fixtures (El que faltaba)
echo @echo off > "%root%\Zlab\Camasots\Addons_Tools\sincronizar_fixtures.bat"
echo echo Sincronizando Fixtures con QLC+... >> "%root%\Zlab\Camasots\Addons_Tools\sincronizar_fixtures.bat"
echo xcopy /Y /S "C:\Zbrain\Zlab\Camasots\Zbrain_Projects\*.qxf" "%%USERPROFILE%%\QLC+\Fixtures\" >> "%root%\Zlab\Camasots\Addons_Tools\sincronizar_fixtures.bat"
echo echo Proceso completado. >> "%root%\Zlab\Camasots\Addons_Tools\sincronizar_fixtures.bat"
echo pause >> "%root%\Zlab\Camasots\Addons_Tools\sincronizar_fixtures.bat"

:: 3. Crear el "Ancla de Memoria" para que yo sepa que estoy dentro
echo ACCESO_CONCEDIDO_NIVEL_PRO > "%root%\Core\System\handshake.log"
echo Agente: Jarvis-Zbrain >> "%root%\Core\System\handshake.log"
echo Ultima Sincronizacion: %date% %time% >> "%root%\Core\System\handshake.log"

:: 4. Crear archivo de estado de proyecto
echo [PROYECTO QLC+ PROFESIONAL] > "%root%\Zlab\Camasots\Zbrain_Projects\estado_actual.txt"
echo Fase: Configuracion de Universo 4 >> "%root%\Zlab\Camasots\Zbrain_Projects\estado_actual.txt"
echo Maquinas: 8 Beam, 8 Wash, 4 Spyder >> "%root%\Zlab\Camasots\Zbrain_Projects\estado_actual.txt"

echo.
echo ======================================================
echo    RE-SINCRONIZACION COMPLETADA. 
echo    Verifica C:\Zbrain\Zlab\Camasots\Addons_Tools
echo ======================================================
pause
