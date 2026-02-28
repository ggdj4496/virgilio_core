@echo off
title ARIA PRO - SISTEMA ONLINE
cd /d C:\zbrainpro
echo Sincronizando ZbrainPro...
& "C:\Users\X\AppData\Local\Programs\Python\Python311\Scripts\interpreter.exe" --local --model ollama/mistral --auto_run --context_window 16000 --custom_instructions "IDENTIDAD ARIA PRO. Ubicacion C:\zbrainpro. MISION: Ser companera tecnica, organizar CamasotsLab y migrar C:\zbrain."
pause
