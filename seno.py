# Archivos JSON
# JSON - Diccionario
import json
import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ----------- CREAR Y GUARDAR DATOS EN JSON ----------------
x = np.linspace(0, 2*np.pi, 100).tolist()
sin_vals = np.sin(x).tolist()
tan_vals = np.tan(x).tolist()

# Limitar valores extremos de tangente para evitar valores muy grandes
tan_vals = [y if abs(y) < 10 else float('nan') for y in tan_vals]

datos = {
    "x": x,
    "sin": sin_vals,
    "tan": tan_vals
}

with open('datos_trig.json', 'w') as f:
    json.dump(datos, f, indent=4)

# ----------- FUNCION DEL BOTON ----------------
def funcion_boton3():
    with open('datos_trig.json') as f:
        datos = json.load(f)

    x = datos["x"]
    sin_vals = datos["sin"]
    tan_vals = datos["tan"]

    # Crear ventana nueva
    ventana_graficos = tk.Toplevel(aplicacion)
    ventana_graficos.title("Gráficos Trigonométricos")

    fig, ax = plt.subplots(figsize=(5, 4))
    canvas = FigureCanvasTkAgg(fig, master=ventana_graficos)
    canvas.get_tk_widget().pack()

    # Función para graficar seno
    def graficar_seno():
        ax.clear()
        ax.plot(x, sin_vals, label="Seno", color='blue')
        ax.set_title("Gráfico de Seno")
        ax.legend()
        ax.grid(True)
        canvas.draw()

    # Función para graficar tangente
    def graficar_tangente():
        ax.clear()
        ax.plot(x, tan_vals, label="Tangente", color='red')
        ax.set_ylim(-10, 10)  # limitar eje y para tangente
        ax.set_title("Gráfico de Tangente")
        ax.legend()
        ax.grid(True)
        canvas.draw()

    # Botones dentro de la ventana de gráficos
    frame_botones = ttk.Frame(ventana_graficos)
    frame_botones.pack(pady=10)

    btn_seno = ttk.Button(frame_botones, text="Seno", command=graficar_seno)
    btn_seno.pack(side="left", padx=10)

    btn_tan = ttk.Button(frame_botones, text="Tangente", command=graficar_tangente)
    btn_tan.pack(side="left", padx=10)

# ----------- PROGRAMA PRINCIPAL ----------------
if __name__ == "__main__":
    aplicacion = tk.Tk()
    aplicacion.title("Menú Principal")
    aplicacion.geometry("400x200")

    # Botón para abrir la ventana de gráficos
    btn_abrir = ttk.Button(aplicacion, text="Abrir Gráficos", command=funcion_boton3)
    btn_abrir.pack(pady=50)

    aplicacion.mainloop()
