import os, json, subprocess
def install():
    folders = [r'C:\Zbrain\Core\System', r'C:\Zbrain\camasotslab\QLC_Espejo', r'C:\Zbrain\camasotslab\Tools', r'C:\Zbrain\Analisis']
    for f in folders: os.makedirs(f, exist_ok=True)
    
    # Inyectar ADN de Memoria
    dna = {'Agent': 'Aria', 'Status': 'Root_Installed', 'Permissions': 'Full_Clone'}
    with open(r'C:\Zbrain\Core\System\ARIA_DNA.json', 'w') as f: json.dump(dna, f)
    
    # Crear Bitácora Inicial
    with open(r'C:\Zbrain\Core\System\BITACORA.log', 'w') as f:
        f.write('[PUNTO DE RUTA 0]: Agente Aria instalado con exito en el nucleo.\n')
    
    # Crear Testigo Real
    with open(r'C:\Zbrain\ACTIVO.txt', 'w') as f: f.write('ARIA ACTIVA')

if __name__ == '__main__': install()
