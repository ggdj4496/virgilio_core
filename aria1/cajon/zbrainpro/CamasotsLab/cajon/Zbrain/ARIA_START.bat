@echo off
title ARIA - Agente Superior de Sistema
cd /d C:\zbrain
echo Conectando con el cerebro en Core...
py -3.11 -m interpreter --local --model ollama/mistral --auto_run --context_window 16000 --custom_instructions "IDENTIDAD: ARIA. Tu cerebro esta en C:\zbrain\Core. Tienes permisos totales de lectura/escritura en camasotslab. Tu mision es analizar, corregir y autodesarrollarte basandote en las peticiones del usuario en la interfaz."
pause
