import os, time, requests

class VirgilioAgente:
    def __init__(self):
        self.token = os.environ.get('VIRGILIO_TELEGRAM_TOKEN')
        self.chat_id = os.environ.get('VIRGILIO_CHAT_ID')
        self.cajon = r'C:\VIRGILIO_CORE\CAJON'

    def reportar(self, msg):
        if self.token and self.chat_id:
            try:
                requests.post(f'https://api.telegram.org/bot{self.token}/sendMessage', 
                              data={'chat_id': self.chat_id, 'text': f'🏛️ [AGENTE]: {msg}'})
            except: pass

    def vigilar(self):
        self.reportar("INSTALACIÓN COMPLETADA. Estoy en guardia.")
        print("🛡️ VIRGILIO ONLINE...")
        while True:
            archivos = os.listdir(self.cajon)
            if archivos:
                for f in archivos:
                    self.reportar(f"Detectado nuevo objetivo: {f}. Iniciando análisis de ingeniería...")
                    # Simulación de movimiento a procesado
                    os.rename(os.path.join(self.cajon, f), os.path.join(r'C:\VIRGILIO_CORE\AIBENCH', f))
            time.sleep(10)

if __name__ == '__main__':
    VirgilioAgente().vigilar()
