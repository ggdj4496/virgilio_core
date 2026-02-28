import traceback
import sys

try:
    exec(open(r"C:\ZLab_AI_Agent\src\app.py", encoding='utf-8').read())
except Exception as e:
    print(f"ERROR: {e}")
    traceback.print_exc()
    input("Presiona Enter para salir...")
