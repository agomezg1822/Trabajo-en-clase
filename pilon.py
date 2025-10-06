from tkinter import *
from PIL import Image, ImageTk, ImageSequence

def paso_derecha():

    global frame_index, x, y
    frame_index = (frame_index + 1) % len(frames)
    x += 10  # mueve 10 pixeles a la derecha
    canvas.itemconfig(image_on_canvas, image=frames[frame_index])
    canvas.coords(image_on_canvas, x, y)

def paso_izquierda():

    global frame_index, x, y
    frame_index = (frame_index + 1) % len(frames)
    x -= 10  # mueve 10 pixeles a la izquierda
    canvas.itemconfig(image_on_canvas, image=frames[frame_index])
    canvas.coords(image_on_canvas, x, y)

if __name__ == "__main__":
    Aplicacion = Tk()
    Aplicacion.title("GIF paso a paso")

   
    canvas = Canvas(Aplicacion, width=600, height=300, bg="white")
    canvas.pack()


    gif = Image.open("pika.gif")
    frames = [ImageTk.PhotoImage(frame.resize((100, 80))) for frame in ImageSequence.Iterator(gif)]
    frame_index = 0


    x, y = 50, 100  
    image_on_canvas = canvas.create_image(x, y, anchor=NW, image=frames[frame_index])

  
    btn_frame = Frame(Aplicacion)
    btn_frame.pack(pady=10)
    Button(btn_frame, text="Paso Derecha", command=paso_derecha).pack(side=LEFT, padx=10)
    Button(btn_frame, text="Paso Izquierda", command=paso_izquierda).pack(side=LEFT, padx=10)

    Aplicacion.mainloop()
