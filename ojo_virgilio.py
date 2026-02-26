import pyautogui
import os
import time

class OjoVirgilio:
    def __init__(self):
        self.output = "C:\\VIRGILIO_CORE\\CAPTURA_REALIDAD.png"

    def capturar_y_validar(self):
        # Captura lo que ves en pantalla
        screenshot = pyautogui.screenshot()
        screenshot.save(self.output)
        print(f"--- REALIDAD CAPTURADA EN {self.output} ---")
        
        # Aquí el Agente de Escucha puede subirla a GitHub 
        # para que yo la analice en el siguiente turno.
        return self.output

if __name__ == "__main__":
    ojo = OjoVirgilio()
    ojo.capturar_y_validar()
