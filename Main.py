import tkinter as tk
from tkinter import *
from PIL import ImageTk
from PIL import Image
from Src.Packages.Baraja import Baraja
from Src.Packages.Juego import Juego
import colorsys

def Apuntado():

    def start():
        
        for i in range(11):
            width = 1000 // 11
            image = Image.open('Src/img/Classic/Clubs/ClubsA.png')
            image = image.resize((width, 500), Image.ANTIALIAS)  # Ajusta el tamaño de la imagen al rectángulo
            photo = ImageTk.PhotoImage(image)
            frame_list[1].create_image(i * width, 0, anchor=tk.NW, image=photo)
        juego.jugarJuego()
        

    root = tk.Tk()
    iconp = Image.open('Src/img/Classic/Clubs/ClubsA.png')
    iconPhoto = ImageTk.PhotoImage(iconp)
    root.title("Apuntado")
    root.iconphoto(False, iconPhoto)


    juego = Juego(5)
    frame_list = []
    for _ in range(0, 1700):
        frame_list.append(Canvas(root, width=1000, height=250, 
            background='darkgray', highlightthickness=2, highlightbackground='black'))

    frame_list[0].pack()
    frame_list[1].pack()

    boton_comenzar = Button(root, bg='blue', text='Comenzar Juego', command=start)
    boton_comenzar.pack()

    root.mainloop()

Apuntado()
