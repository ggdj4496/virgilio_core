import os

def inicializar_aria():

    ruta_raiz = "C:/zbrain"

    if not os.path.exists(ruta_raiz):

        os.makedirs(ruta_raiz)

    

    archivo_confirmacion = os.path.join(ruta_raiz, "hola.txt")

    with open(archivo_confirmacion, "w", encoding="utf-8") as f:

        f.write("ARIA funciona.\n")

        f.write("Estado: Conectada al ordenador Dell.\n")

        f.write("Sistema: Z_brain Core Activo.\n")

        f.write("Ajuste de voz: Calibrado al 100%.")

    

    print("Dime. ARIA está operativa en este sistema.")

if __name__ == "__main__":

    inicializar_aria()
