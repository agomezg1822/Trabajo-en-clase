# cliente.py
import socket
import tkinter as tk
from tkinter import Button

IP_SERVIDOR = "127.0.0.1"
PUERTO = 1234

def enviar_orden(orden):
    try:
        s = socket.socket()
        s.connect((IP_SERVIDOR, PUERTO))
        s.send(orden.encode("utf8"))
        print(f"Orden enviada: {orden}")
        s.close()
    except Exception as e:
        print("Error al conectar con el servidor:", e)

if __name__ == "__main__":
    app = tk.Tk()
    app.title("Cliente - Menú de Opciones")

    Button(app, text="Animación", command=lambda: enviar_orden("ejecutandoanimacionmodifico")).pack(pady=10)
    Button(app, text="Gráfico Seno/Tangente", command=lambda: enviar_orden("ejecutandografico")).pack(pady=10)
    Button(app, text="Barras Interactivas", command=lambda: enviar_orden("ejecutandobarras")).pack(pady=10)
    Button(app, text="Salir", command=lambda: enviar_orden("cerrar")).pack(pady=10)

    app.mainloop()
