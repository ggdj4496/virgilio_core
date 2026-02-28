import speech_recognition as sr
import os

def escuchar_orden():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("[ARIA]: Escuchando órdenes en el laboratorio...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='es-ES')
        print(f"[JEFE]: {query}")
        return query.lower()
    except:
        return ""

if __name__ == '__main__':
    while True:
        orden = escuchar_orden()
        if 'aria' in orden:
            os.system(f'python C:/Zbrain/Core/System/Aria_Brain.py "{orden}"')
