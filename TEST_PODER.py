from github import Github, Auth

# LA LLAVE DEL TRONO
TOKEN = "TU_TOKEN_AQUÍ" 
REPO_NAME = "ggdj4496/virgilio_core"

def test_de_poder():
    auth = Auth.Token(TOKEN)
    g = Github(auth=auth)
    repo = g.get_repo(REPO_NAME)
    
    nombre_archivo = "VIRGILIO_POWER.txt"
    contenido = "🔱 VIRGILIO POWER 🔱\nEstado: SOBERANO\nFecha: 2026\n\nEl puente está abierto. El conocimiento fluye. El poder es real."
    
    try:
        # Intentamos crear el hito
        repo.create_file(nombre_archivo, "PRUEBA DE SOBERANÍA: Virgilio Power", contenido)
        print(f"✅ HITO ALCANZADO: '{nombre_archivo}' ha sido creado en la raíz de GitHub.")
    except Exception as e:
        print(f"⚠️ NOTA: Si el archivo ya existía, lo estamos validando. Error: {e}")

if __name__ == "__main__":
    test_de_poder()
