import keyboard
import pyautogui
import os
import time

# Configuración
OUTPUT = "C:\\VIRGILIO_CORE\\CAPTURA_REALIDAD.png"

def capturar_pantalla():
    print("🔱 VIRGILIO: Capturando realidad visual...")
    # Pequeño delay para que no salga el menú de inicio si se activa por error
    time.sleep(0.2)
    screenshot = pyautogui.screenshot()
    screenshot.save(OUTPUT)
    
    # Creamos una ORDEN.txt falsa para que el Monitor sepa que debe subir la imagen
    with open("C:\\VIRGILIO_CORE\\ORDEN.txt", "w", encoding="utf-8") as f:
        f.write("CAPTURA_REALIDAD.png\n")
        f.write("Sincronia Visual Solicitada")
    
    print("✅ Captura lista y enviada al Agente de Escucha.")

print("📡 Ojo de Virgilio activo. Presiona CTRL+SHIFT+IMPR PANT para sincronizar.")
keyboard.add_hotkey('ctrl+shift+print screen', capturar_pantalla)

keyboard.wait()
