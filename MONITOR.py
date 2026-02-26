import os
import time
import base64
from github import Github, Auth

def iniciar():
    token = os.getenv('VIRGILIO_TOKEN')
    repo_name = "ggdj4496/virgilio_core"
    print("--- MONITOR VIRGILIO V2.0 (VISIÓN) ---")
    try:
        g = Github(auth=Auth.Token(token))
        repo = g.get_repo(repo_name)
        print("CONEXION OK")
        
        while True:
            if os.path.exists("ORDEN.txt"):
                time.sleep(0.5)
                try:
                    with open("ORDEN.txt", "r", encoding="utf-8-sig") as f:
                        lines = f.readlines()
                    if lines:
                        file_to_upload = lines[0].strip()
                        if os.path.exists(file_to_upload):
                            with open(file_to_upload, "rb") as f_data:
                                content = f_data.read()
                            try:
                                c = repo.get_contents(file_to_upload)
                                repo.update_file(c.path, "Vision Sync", content, c.sha)
                            except:
                                repo.create_file(file_to_upload, "Vision Init", content)
                            print(f"IMAGEN ENVIADA: {file_to_upload}")
                            os.remove("ORDEN.txt")
                except Exception as e: print(f"ERR: {e}")
            time.sleep(1)
    except Exception as e: print(f"FATAL: {e}")

if __name__ == "__main__":
    iniciar()