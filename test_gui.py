import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Prueba ZLab")
root.geometry("400x200")

label = tk.Label(root, text="¡ZLab AI funciona correctamente!")
label.pack(pady=50)

button = tk.Button(root, text="Cerrar", command=root.quit)
button.pack()

root.mainloop()
