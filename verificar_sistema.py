import os
import subprocess

def check_tools():
    print("--- VERIFICANDO ARSENAL ---")
    tools = ["python", "rustc", "git"]
    for tool in tools:
        status = subprocess.getstatusoutput(f"{tool} --version")
        print(f"[OK] {tool} detectado.") if status[0] == 0 else print(f"[!] {tool} falta.")

if __name__ == "__main__":
    check_tools()
    print("\n[MISION] Accede a https://www.flowhunt.io y usa el System Prompt cargado.")
