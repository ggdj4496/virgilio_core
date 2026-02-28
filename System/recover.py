import os
import json

base = r'C:\Zbrain'
print(f'\n--- [ARIA]: INICIANDO ESCANEO DE ADN EN {base} ---')

# 1. Recuperar Identidad
dna_path = os.path.join(base, 'Core', 'System', 'ARIA_DNA.json')
if os.path.exists(dna_path):
    with open(dna_path, 'r') as f:
        dna = json.load(f)
        print(f'[IDENTIDAD]: Confirmada. Agente: {dna.get("Agent")}, Permisos: {dna.get("Permissions")}')
else:
    print('[ADVERTENCIA]: DNA no encontrado. Creando nueva secuencia...')

# 2. Escanear Proyectos y Fixtures
zlab = os.path.join(base, 'Zlab', 'Camasots')
print('\n--- [REPORTE DE ACTIVOS] ---')
for root, dirs, files in os.walk(zlab):
    for file in files:
        if file.endswith('.qxf'):
            print(f'[FIXTURE]: {file} -> Localizado')
        if file.endswith('.qxw'):
            print(f'[PROYECTO]: {file} -> Localizado')

# 3. Marcar Bitácora
log_path = os.path.join(base, 'Core', 'System', 'BITACORA.log')
with open(log_path, 'a') as f:
    f.write('\n[SISTEMA]: Aria ha recuperado el control manual del sistema.')

print('\n--- [ESTADO]: CONTROL RECUPERADO. ESPERANDO ÓRDENES ---')
