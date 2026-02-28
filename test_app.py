import sys
import traceback

try:
    # Tu código original aquí
    exec(open(r"C:\ZLab_AI_Agent\src\app.py").read())
except Exception as e:
    print(f"ERROR: {e}")
    traceback.print_exc()
    input("Presiona Enter para salir...")
