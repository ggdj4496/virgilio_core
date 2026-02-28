import pystray
from PIL import Image, ImageDraw
import os, subprocess

def on_open_interface():
    # Nos trae a la interfaz de trabajo
    os.startfile('https://gemini.google.com')

def on_toggle_voice():
    # Aqui ARIA desarrollara su propio modulo de escucha activada
    print('Modo Voz: Configurando...')

# Crear el icono de estrella de Sheriff para la bandeja
def create_image():
    # ARIA buscara un icono real, por ahora genera un marcador visual
    image = Image.new('RGB', (64, 64), color=(128, 0, 128))
    return image

icon = pystray.Icon('ARIA', create_image(), 'ARIA PRO', menu=pystray.Menu(
    pystray.MenuItem('Abrir Comunicacion General', on_open_interface),
    pystray.MenuItem('Activar/Desactivar Voz', on_toggle_voice),
    pystray.MenuItem('Acceso a Baticueva (Camasots)', lambda: os.startfile('C:\\zbrainpro\\CamasotsLab')),
    pystray.MenuItem('Salir', lambda: icon.stop())
))

print('ARIA: Iniciando en segundo plano...')
icon.run()
