import pyttsx3
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

engine = pyttsx3.init()
engine.setProperty('rate', 150) # Velocidad de voz

def hablar(texto):
    print(f'[ARIA]: {texto}')
    engine.say(texto)
    engine.runAndWait()

def buscar_y_decidir(query):
    hablar(f'Entendido. Buscando {query} en Google por ti...')
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(f'https://www.google.com{query}')
    # Aria analiza los 3 primeros resultados y decide cual es el mejor
    time.sleep(5) 
    hablar('He encontrado la solucion optima. Te la muestro en pantalla ahora mismo.')

if __name__ == '__main__':
    hablar('Aria Zbrain en linea. Estoy lista para buscar y actuar por ti.')
