import tkinter as tk
from tkinter import *
from PIL import ImageTk
from PIL import Image
from Src.Packages.Baraja import Baraja
from Src.Packages.Juego import Juego
import colorsys

def Apuntado():

    def center_window(root, width, height):
        # Obtener las dimensiones de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        # Configurar la posición de la ventana
        root.geometry(f"{width}x{height}+{x}+{y}")

    def start():
        global frame_inferior, altura_seccion, ancho_seccion
        for widget in root.winfo_children():
            widget.destroy()
        # Configurar el frame superior (verde)
        frame_superior = tk.Frame(root, bg="green", height=300, width=1300)
        frame_superior.pack(fill="both", expand=True, padx=4, pady=4)

        # Configurar el Label en la esquina izquierda del frame_superior
        label_info_partida = tk.Label(frame_superior, bg='darkgray', text = 'Partida #', height=3, width=10)
        label_info_partida.grid(row=0, column=0, sticky="nw")

        label_num_partida = tk.Label(frame_superior, bg='darkgreen', text = '1', height=3, width=10)
        label_num_partida.grid(row=0, column=1, sticky="nw")

        # Botón de Tirar
        botonTirar = tk.Button(frame_superior, text='Tirar', bg="gray", bd=5, height=3, width=10, command=tirar)
        botonTirar.grid(row=0, column=2, padx=10, pady=10, sticky="n")  # Alinear arriba

        # Botón de Arrastrar
        botonArrastrar = tk.Button(frame_superior, text='Arrastrar', bg="gray", bd=5, height=3, width=10, command=arrastrar)
        botonArrastrar.grid(row=0, column=3, padx=10, pady=10, sticky="n")  # Alinear arriba

        # Botón de Tocar
        botonTocar = tk.Button(frame_superior, text='Tocar', bg="gray", bd=5, height=3, width=10, command=tocar)
        botonTocar.grid(row=0, column=4, padx=10, pady=10, sticky="n")  # Alinear arriba

        # Botón de Bajarse
        botonBajarse = tk.Button(frame_superior, text='Bajarse', bg="gray", bd=5, height=3, width=10, command=bajarse)
        botonBajarse.grid(row=0, column=5, padx=10, pady=10, sticky="n")  # Alinear arriba

        # Configurar el frame inferior (gris)
        frame_inferior = tk.Frame(root, bg="gray", height=200, width=1300)
        frame_inferior.pack(fill="both", expand=True, padx=4, pady=4)

        # Centrar la ventana en la pantalla
        center_window(root, 1300, 500)
        # Calcular la altura de cada sección

        

        juego = Juego(5) # se inicia un juego con 5 jugadores

        juego.jugarJuego() # se reparten las cartas

        for j in juego.jugadores: # se establece quien es el jugador que comienza (el de las 11 cartas)
            if len(j.getMano()) == 11:
                mano_inicial = j.getMano()
                break
            
        altura_seccion = frame_inferior.winfo_reqheight()
        ancho_seccion = frame_inferior.winfo_reqwidth() // len(mano_inicial)

        mostrar_cartas_jugador(mano_inicial)

    def mostrar_cartas_jugador(mano_inicial):
        global frame_inferior, altura_seccion, ancho_seccion
        for carta in mano_inicial:
            
            # Crear un subframe para cada sección
            subframe = tk.Frame(frame_inferior, bg="gray", height=altura_seccion, width=ancho_seccion)
            subframe.pack_propagate(False)  # se evita que el subframe se ajuste automáticamente
            subframe.pack(side="left")  # se alinean los subframes uno al lado del otro

            # Cargar la imagen
            imagen_path = f'Src/img/Classic/{carta.getPinta()}/{carta.getPinta()}{carta.getDenominacion()}.png' 
            imagen = Image.open(imagen_path)
            image_redimensionada = imagen.resize((ancho_seccion - 2, altura_seccion - 2), Image.LANCZOS) # se redimensionan las imágenes al tamaño de los contenedores
            imagen = ImageTk.PhotoImage(image_redimensionada)

            # Mostrar la imagen en el botón
            boton = tk.Button(subframe, image=imagen, bg="gray", bd=4, command=lambda img=imagen: mostrar_imagen(img))
            boton.image = imagen  # Para evitar que la imagen sea recolectada por el recolector de basura
            boton.pack(fill="both", expand=True)

    def mostrar_imagen(imagen):
        # agregar aquí lo que pasará al hacer click en la img
        pass

    def tirar():
        # agregar aquí lo que pasará al hacer click en el botón 'tirar'
        pass

    def arrastrar():
        # agregar aquí lo que pasará al hacer click en el botón 'arrastrar'
        pass

    def tocar():
        # agregar aquí lo que pasará al hacer click en el botón 'tocar'
        pass

    def bajarse():
        # agregar aquí lo que pasará al hacer click en el botón 'bajarse'
        pass

    root = tk.Tk()
    iconp = Image.open('Src/img/Classic/Clubs/ClubsA.png')
    iconPhoto = ImageTk.PhotoImage(iconp)
    root.title("Apuntado")
    root.iconphoto(False, iconPhoto)

    acciones = ['tirar', 'arrastrar', 'bajarse', 'tocar']
    # Configurar el frame superior (verde)
    frame_info = tk.Frame(root, bg="green", height=300, width=600)
    frame_info.pack(fill="both", expand=True, padx=4, pady=4)

    boton_comenzar = tk.Button(frame_info, bg='red', text='Comenzar Juego', 
                            command=start, height=5, width=25)
    boton_comenzar.pack(padx = 80, pady = 30)
    boton_comenzar.pack()

    root.mainloop()

Apuntado()
