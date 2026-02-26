
import threading
import time

def tarea_virgilio(id):
    print(f"🧬 Hilo {id} activo. Procesando datos para el Caballero...")
    time.sleep(1)

for i in range(5):
    threading.Thread(target=tarea_virgilio, args=(i,)).start()
