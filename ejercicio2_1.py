from tkinter import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Variable global que representa el valor de la barra
valor = 0

def actualizar_grafica():
    ax.clear()
    ax.bar(["Valor"], [valor], color="blue")
    ax.set_ylim(0, 10)  
    canvas.draw()

def aumentar():
    global valor
    if valor < 10:  # límite superior
        valor += 1
    actualizar_grafica()

def disminuir():
    global valor
    if valor > 0:  # límite inferior
        valor -= 1
    actualizar_grafica()

if __name__ == "__main__":
    Aplicacion = Tk()
    Aplicacion.title("Gráfica de Barras Interactiva")
    Aplicacion.geometry("500x400")

    # Crear figura matplotlib
    fig, ax = plt.subplots(figsize=(4,3))
    canvas = FigureCanvasTkAgg(fig, master=Aplicacion)
    canvas.get_tk_widget().pack()

    # Botones
    boton_aumentar = Button(Aplicacion, text="Aumentar", command=aumentar)
    boton_aumentar.pack(side=LEFT, padx=20, pady=10)

    boton_disminuir = Button(Aplicacion, text="Disminuir", command=disminuir)
    boton_disminuir.pack(side=RIGHT, padx=20, pady=10)

    # Inicializar la gráfica
    actualizar_grafica()

    Aplicacion.mainloop()