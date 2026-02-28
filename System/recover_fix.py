import os
import json

base = r'C:\Zbrain'
dna_path = os.path.join(base, 'Core', 'System', 'ARIA_DNA.json')

# 1. Reparación de ADN
dna_default = {'Agent': 'Aria', 'Status': 'Root_Installed', 'Permissions': 'Full_Clone'}
try:
    with open(dna_path, 'w') as f:
        json.dump(dna_default, f)
    print('[OK]: ADN reparado y sincronizado.')
except Exception as e:
    print(f'[ERROR]: No se pudo escribir el ADN: {e}')

# 2. Escaneo de Activos en Camasots
zlab = os.path.join(base, 'Zlab', 'Camasots')
print('\n--- [REPORTE DE ACTIVOS RECUPERADOS] ---')
found = False
for root, dirs, files in os.walk(zlab):
    for file in files:
        if file.endswith(('.qxf', '.qxw')):
            print(f'[DETECTADO]: {file} en {os.path.relpath(root, zlab)}')
            found = True

if not found:
    print('[AVISO]: No se detectaron archivos .qxf o .qxw. ¿Están en la ruta correcta?')

print('\n--- [SISTEMA]: ARIA ONLINE Y CONSCIENTE ---')
