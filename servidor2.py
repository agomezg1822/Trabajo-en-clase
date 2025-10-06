# servidor.py
import socket
import threading
import tkinter as tk
from tkinter import Canvas, Frame, Button, LEFT, NW, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np
import json
from PIL import Image, ImageTk, ImageSequence

# -------- FUNCIONES DE LAS OPCIONES --------

def abrir_animacion():
    ventana_anim = tk.Toplevel()
    ventana_anim.title("GIF paso a paso (Servidor)")

    canvas = Canvas(ventana_anim, width=600, height=300, bg="white")
    canvas.pack()

    gif = Image.open("pika.gif")
    frames = [ImageTk.PhotoImage(frame.resize((100, 80))) for frame in ImageSequence.Iterator(gif)]
    frame_index = 0
    x, y = 50, 100
    image_on_canvas = canvas.create_image(x, y, anchor=NW, image=frames[frame_index])

    def paso_derecha():
        nonlocal frame_index, x, y
        frame_index = (frame_index + 1) % len(frames)
        x += 10
        canvas.itemconfig(image_on_canvas, image=frames[frame_index])
        canvas.coords(image_on_canvas, x, y)

    def paso_izquierda():
        nonlocal frame_index, x, y
        frame_index = (frame_index + 1) % len(frames)
        x -= 10
        canvas.itemconfig(image_on_canvas, image=frames[frame_index])
        canvas.coords(image_on_canvas, x, y)

    btn_frame = Frame(ventana_anim)
    btn_frame.pack(pady=10)
    Button(btn_frame, text="Paso Derecha", command=paso_derecha).pack(side=LEFT, padx=10)
    Button(btn_frame, text="Paso Izquierda", command=paso_izquierda).pack(side=LEFT, padx=10)

def abrir_graficos():
    with open("datos_trig.json") as f:
        datos = json.load(f)

    x = datos["x"]
    sin_vals = datos["sin"]
    tan_vals = datos["tan"]

    ventana_graficos = tk.Toplevel()
    ventana_graficos.title("Gráficos Trigonométricos (Servidor)")

    fig, ax = plt.subplots(figsize=(5, 4))
    canvas = FigureCanvasTkAgg(fig, master=ventana_graficos)
    canvas.get_tk_widget().pack()

    def graficar_seno():
        ax.clear()
        ax.plot(x, sin_vals, label="Seno", color="blue")
        ax.set_title("Gráfico de Seno")
        ax.legend()
        ax.grid(True)
        canvas.draw()

    def graficar_tangente():
        ax.clear()
        ax.plot(x, tan_vals, label="Tangente", color="red")
        ax.set_ylim(-10, 10)
        ax.set_title("Gráfico de Tangente")
        ax.legend()
        ax.grid(True)
        canvas.draw()

    frame_botones = ttk.Frame(ventana_graficos)
    frame_botones.pack(pady=10)

    ttk.Button(frame_botones, text="Seno", command=graficar_seno).pack(side="left", padx=10)
    ttk.Button(frame_botones, text="Tangente", command=graficar_tangente).pack(side="left", padx=10)

def abrir_barras():
    valor = 0
    ventana_barras = tk.Toplevel()
    ventana_barras.title("Gráfica de Barras Interactiva (Servidor)")
    ventana_barras.geometry("500x400")

    fig, ax = plt.subplots(figsize=(4, 3))
    canvas = FigureCanvasTkAgg(fig, master=ventana_barras)
    canvas.get_tk_widget().pack()

    def actualizar_grafica():
        ax.clear()
        ax.bar(["Valor"], [valor], color="blue")
        ax.set_ylim(0, 10)
        canvas.draw()

    def aumentar():
        nonlocal valor
        if valor < 10:
            valor += 1
        actualizar_grafica()

    def disminuir():
        nonlocal valor
        if valor > 0:
            valor -= 1
        actualizar_grafica()

    Button(ventana_barras, text="Aumentar", command=aumentar).pack(side=LEFT, padx=20, pady=10)
    Button(ventana_barras, text="Disminuir", command=disminuir).pack(side=LEFT, padx=20, pady=10)

    actualizar_grafica()

# -------- SERVIDOR --------

def manejar_cliente(conn, addr, root):
    print("Conectado con:", addr)
    while True:
        data = conn.recv(1024)
        if not data:
            break
        mensaje = data.decode("utf8")
        print("Cliente dice:", mensaje)

        if mensaje == "ejecutandoanimacionmodifico":
            root.after(0, abrir_animacion)
        elif mensaje == "ejecutandografico":
            root.after(0, abrir_graficos)
        elif mensaje == "ejecutandobarras":
            root.after(0, abrir_barras)
        elif mensaje == "cerrar":
            break
    conn.close()

def servidor(root):
    server_socket = socket.socket()
    server_socket.bind(("127.0.0.1", 1234))
    server_socket.listen(5)
    print("Servidor escuchando en 127.0.0.1:1234")

    while True:
        conn, addr = server_socket.accept()
        threading.Thread(target=manejar_cliente, args=(conn, addr, root), daemon=True).start()

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal
    threading.Thread(target=servidor, args=(root,), daemon=True).start()
    root.mainloop()