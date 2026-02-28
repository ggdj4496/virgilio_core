@echo off
title ARIA SUPERAGENT INTERFACE
echo [02/17/2026 04:35:57] Iniciando sincron?a con Zbrain Core...
start /min powershell.exe -WindowStyle Hidden -File "C:\Zbrain\Core\ARIA_Core.ps1"
start "C:\Windows\System32\mshta.exe" "C:\Zbrain\Core\ARIA_App.hta"

