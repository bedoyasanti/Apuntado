import tkinter as tk
from tkinter import *
from PIL import ImageTk
from PIL import Image
from Src.Packages.Baraja import Baraja
from Src.Packages.Juego import Juego
import colorsys

def Apuntado():

    def center_window(root, width, height):
        '''sirve para centrar la interfaz de juego'''

        # Obtener las dimensiones de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        # Configurar la posición de la ventana
        root.geometry(f"{width}x{height}+{x}+{y}")

    def start():
        '''Se crea la interfaz de juego, un juego (por defecto de 5 jugadores), 
        se define el jugador que empieza primero, y se establece el estado de los botones para él'''

        global frame_inferior, altura_seccion, ancho_seccion, label_num_jugador, botonTocar, botonBajarse
        global label_carta_seleccionada, label_carta_seleccionada2

        for widget in root.winfo_children():
            widget.destroy()
        # Configurar el frame superior (verde)
        frame_superior = tk.Frame(root, bg="green", height=300, width=1300)
        frame_superior.pack(fill="both", expand=True, padx=4, pady=4)

        ### Labels
        # label de info partida
        label_info_partida = tk.Label(frame_superior, bg='darkgray', text = 'Partida #', height=3, width=10)
        label_info_partida.grid(row=0, column=0, sticky="nw", padx=3, pady=3)

        label_num_partida = tk.Label(frame_superior, bg='darkgreen', text = '1', height=3, width=10)
        label_num_partida.grid(row=0, column=1, sticky="nw", padx=3, pady=3)


        # label de jugador
        label_info_jugador = tk.Label(frame_superior, text = 'Jugador #', bg='darkgray', height=3, width=10)
        label_info_jugador.grid(row=1, column=0, padx=3, pady=3)

        label_num_jugador = tk.Label(frame_superior, text = 'nn', bg='darkgreen', height=3, width=10)
        label_num_jugador.grid(row=1, column=1, padx=3, pady=3)


        ### Botones
        # Botón de Tirar
        botonTirar = tk.Button(frame_superior, text='Tirar', bg="gray", bd=5, height=3, width=10, command=tirar)
        botonTirar.grid(row=0, column=2, padx=10, pady=10, sticky="n")  # Alinear arriba

        # Botón de Arrastrar
        botonArrastrar = tk.Button(frame_superior, text='Arrastrar', bg="gray", bd=5, height=3, width=10, command=arrastrar)
        botonArrastrar.grid(row=0, column=3, padx=10, pady=10, sticky="n")  # Alinear arriba
        botonArrastrar.config(state=tk.DISABLED)

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
        altura_seccion = frame_inferior.winfo_reqheight()
        ancho_seccion = frame_inferior.winfo_reqwidth() // 11

        '''# label de cartas seleccionadas (teniendo en cuenta tocar)
        label_carta_seleccionada = tk.Label(frame_superior, bg='darkblue', height=altura_seccion, width=ancho_seccion)
        label_carta_seleccionada.grid(row=0, column=6, padx=10, pady=10) #, sticky="e")

        label_carta_seleccionada2 = tk.Label(frame_superior, bg='darkblue', height=altura_seccion, width=ancho_seccion)
        label_carta_seleccionada2.grid(row=0, column=7, padx=10, pady=10) #, sticky="e")'''


        ### Se empieza un nuevo juego
        num_jugadores_juego = 5
        juego = Juego(num_jugadores_juego) # se inicia un juego con 5 jugadores


        juego.jugarJuego() # se reparten las cartas

        for j in range(len(juego.getJugadores())): # se establece quien es el jugador que comienza (el de las 11 cartas)
                if len(juego.getJugadores()[j].getMano()) == 11:
                    #mano_inicial = j.getMano()
                    break

        #while True:

        mostrar_cartas_jugador(juego.getJugadores()[j])


    def mostrar_cartas_jugador(jugador):
        '''se muestran las cartas del jugador, poniéndolas encima de botones'''

        global frame_inferior, altura_seccion, ancho_seccion, label_num_jugador, botones, carta, carta_seleccionada
        global label_carta_seleccionada, label_carta_seleccionada2

        mano_inicial = jugador.getMano()

        label_num_jugador.config(text=jugador.getnumJugador())

        # Lista para almacenar las referencias a los botones
        botones = list()

        for carta in mano_inicial:

            # Crear un subframe para cada sección
            subframe = tk.Frame(frame_inferior, bg="gray", height=altura_seccion, width=ancho_seccion)
            subframe.pack_propagate(False)  # se evita que el subframe se ajuste automáticamente
            subframe.pack(side="left")  # se alinean los subframes uno al lado del otro

            # Cargar la imagen
            imagen_path = f'Src/img/Classic/{carta.getPinta()}/{carta.getPinta()}{carta.getDenominacion()}.png' 
            imagen = Image.open(imagen_path)
            image_redimensionada = imagen.resize((ancho_seccion - 8, altura_seccion - 8), Image.LANCZOS) # se redimensionan las imágenes al tamaño de los contenedores
            imagen = ImageTk.PhotoImage(image_redimensionada)

            # Mostrar la imagen en el botón
            boton = tk.Button(subframe, bg="gray", bd=4, command=lambda img=imagen: mostrar_imagen(img))
            boton.image = imagen  # Mantener una referencia a la imagen
            boton.config(image=imagen)  # Configurar la imagen en el botón
            boton.pack(fill="both", expand=True)

            # Agregar la referencia del botón a la lista
            botones.append(boton)

    def mostrar_imagen(imagen):
        '''esta funcion sirve para seleccionar una carta, y darle un formato especial al boton que contiene la 
        carta cada vez que se hace click en él'''

        global botonTocar, botonBajarse, carta, carta_seleccionada, label_carta_seleccionada
        for b in botones: # para que al dar click en una carta, esta tenga un marco rojo (no funciona)
            if b.cget("image") == imagen:
                b.config(bg="red", bd=15)
        
        botonBajarse.config(state=tk.DISABLED) # Cambiar el color de fondo y borde del botón bajarse

        carta_seleccionada = carta

        label_carta_seleccionada.config(image=imagen)


    def tirar():
        # agregar aquí lo que pasará al hacer click en el botón 'tirar'
        global carta_seleccionada
        accion = 'tirar'
        pass

    def arrastrar():
        # agregar aquí lo que pasará al hacer click en el botón 'arrastrar'
        accion = 'arrastrar'
        pass

    def tocar():
        # agregar aquí lo que pasará al hacer click en el botón 'tocar'
        global carta_seleccionada
        accion = 'tocar'
        pass

    def bajarse():
        global botonTocar
        # agregar aquí lo que pasará al hacer click en el botón 'bajarse'
        accion = 'bajarse'
        botonTocar.config(state=tk.DISABLED)
        pass

    root = tk.Tk()
    iconp = Image.open('Src/img/Classic/Clubs/ClubsA.png')
    iconPhoto = ImageTk.PhotoImage(iconp)
    root.title("Apuntado")
    root.iconphoto(False, iconPhoto)

    accion = ''
    # Configurar el frame superior (verde)
    frame_info = tk.Frame(root, bg="green", height=300, width=600)
    frame_info.pack(fill="both", expand=True, padx=4, pady=4)

    boton_comenzar = tk.Button(frame_info, bg='red', text='Comenzar Juego', 
                            command=start, height=5, width=25)
    boton_comenzar.pack(padx = 80, pady = 30)
    boton_comenzar.pack()

    root.mainloop()

Apuntado()
