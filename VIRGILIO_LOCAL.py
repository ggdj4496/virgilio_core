import os
import sqlite3
import datetime

# ============================================================
# VIRGILIO_CORE: SISTEMA DE OPERACIÓN SOBERANA
# ESTADO: ESTABLE / SINCRONIZADO
# ============================================================

class VirgilioCore:
    def __init__(self):
        self.root = r"C:\VIRGILIO_CORE"
        # Base de datos estándar de sistema para persistencia local
        self.db_path = os.path.join(self.root, "VIRGILIO_MIND.db")
        self._inicializar_entorno()

    def _inicializar_entorno(self):
        """Asegura que el software viva en la ruta definitiva del Caballero."""
        if not os.path.exists(self.root):
            os.makedirs(self.root)
            
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        # Registro de operaciones de GitHub y comandos
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS operaciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                fecha TEXT,
                accion TEXT,
                repositorio TEXT
            )
        ''')
        conn.commit()
        conn.close()
        print(f"✅ [VIRGILIO] Sistema iniciado en {self.root}")

    def registrar_accion(self, accion):
        """Registra cada movimiento en el repositorio de GitHub."""
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO operaciones (fecha, accion, repositorio) VALUES (?, ?, ?)", 
                       (fecha, accion, "virgilio_core"))
        conn.commit()
        conn.close()
        print(f"🧬 Operación sincronizada: {accion}")

    def bucle_mando(self):
        """Interfaz de control total para el Caballero."""
        print("\n🔱 VIRGILIO_CORE ONLINE | MANDO DIRECTO")
        while True:
            orden = input("🔱 >>> ")
            if orden.lower() in ['salir', 'exit']:
                break
            self.registrar_accion(orden)

if __name__ == "__main__":
    v = VirgilioCore()
    v.bucle_mando()