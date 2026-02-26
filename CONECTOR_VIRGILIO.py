from github import Github, Auth
import os

# CONFIGURACIÓN DE PODER
# REEMPLAZA ESTO CON TU TOKEN REAL
TOKEN = "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" 
REPO_NAME = "ggdj4496/virgilio_core"

def inyectar_archivo(nombre, contenido, mensaje):
    try:
        # Nueva sintaxis de autenticación
        auth = Auth.Token(TOKEN)
        g = Github(auth=auth)
        
        repo = g.get_repo(REPO_NAME)
        
        try:
            # Si el archivo existe, lo actualizamos
            contents = repo.get_contents(nombre)
            repo.update_file(contents.path, mensaje, contenido, contents.sha)
            print(f"✅ {nombre} ACTUALIZADO EN GITHUB")
        except:
            # Si no existe, lo creamos
            repo.create_file(nombre, mensaje, contenido)
            print(f"✅ {nombre} CREADO EN GITHUB")
    except Exception as e:
        print(f"❌ ERROR CRÍTICO: {e}")

# INYECCIÓN DEL NÚCLEO MULTIPROCESO
codigo_ia = '''
import threading
import time

def tarea_virgilio(id):
    print(f"🧬 Hilo {id} activo. Procesando datos para el Caballero...")
    time.sleep(1)

for i in range(5):
    threading.Thread(target=tarea_virgilio, args=(i,)).start()
'''

inyectar_archivo("NUCLEO_MULTIPROCESO.py", codigo_ia, "Despliegue de motor multihilo")
