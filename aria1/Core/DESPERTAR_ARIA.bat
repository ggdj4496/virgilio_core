@echo off
title ARIA CORE - Sistema de Control Camasots (Mistral)
echo [ARIA] Limpiando procesos...
taskkill /f /im ollama.exe >nul 2>&1
timeout /t 2 >nul
echo [ARIA] Arrancando Motor con Cerebro Mistral...
start /b ollama serve
timeout /t 5 >nul
echo [ARIA] Conectando... ?Prep?rate, Guille!
ollama run mistral
pause
