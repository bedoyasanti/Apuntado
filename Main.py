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

    def comenzarNuevoJuego():
        '''se crea un juego (por defecto de 5 jugadores), y se define el jugador que empieza primero'''

        global j, num_jugadores_juego, juego

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

    def start():
        '''Se crea la interfaz de juego'''

        global frame_inferior, frame_superior, altura_seccion, ancho_seccion, label_num_jugador
        global label_carta_seleccionada, label_carta_seleccionada2
        global botonTirar, botonArrastrar, botonTocar, botonBajarse, botonCogerCarta

        for widget in root.winfo_children():
            widget.destroy()
        # Configurar el frame superior (verde)
        frame_superior = tk.Frame(root, bg="green", height=300, width=1300)
        frame_superior.pack(fill="both", expand=True, padx=4, pady=4)

        ### Labels
        # label de info partida
        label_info_partida = tk.Label(frame_superior, bg='darkgray', text = 'Partida #', height=3, width=10)
        label_info_partida.grid(row=0, column=0, sticky="nw", padx=10, pady=5)

        label_num_partida = tk.Label(frame_superior, bg='darkgreen', text = '1', height=3, width=10)
        label_num_partida.grid(row=0, column=1, sticky="nw", padx=10, pady=5)


        # label de jugador
        label_info_jugador = tk.Label(frame_superior, text = 'Jugador #', bg='darkgray', height=3, width=10)
        label_info_jugador.grid(row=1, column=0, padx=10, pady=5)

        label_num_jugador = tk.Label(frame_superior, text = 'nn', bg='darkgreen', height=3, width=10)
        label_num_jugador.grid(row=1, column=1, padx=10, pady=5)


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

        # Botón de Coger Carta Tirada
        botonCogerCarta = tk.Button(frame_superior, text='Coger Carta Tirada', bg="gray", bd=5, height=3, width=15, command=coger_carta)
        botonCogerCarta.grid(row=0, column=6, padx=10, pady=10, sticky="n")  # Alinear arriba

        # Configurar el frame inferior (gris)
        frame_inferior = tk.Frame(root, bg="gray", height=200, width=1300)
        frame_inferior.pack(fill="both", expand=True, padx=4, pady=4)

        # Centrar la ventana en la pantalla
        center_window(root, 1300, 500)


        comenzarNuevoJuego()
        '''# label de cartas seleccionadas (teniendo en cuenta tocar)
        label_carta_seleccionada = tk.Label(frame_superior, bg='darkblue', height=altura_seccion, width=ancho_seccion)
        label_carta_seleccionada.grid(row=0, column=6, padx=10, pady=10) #, sticky="e")

        label_carta_seleccionada2 = tk.Label(frame_superior, bg='darkblue', height=altura_seccion, width=ancho_seccion)
        label_carta_seleccionada2.grid(row=0, column=7, padx=10, pady=10) #, sticky="e")'''


    def mostrar_cartas_jugador(jugador):
        '''se muestran las cartas del jugador, poniéndolas en botones'''

        global frame_inferior, frame_superior, altura_seccion, ancho_seccion, label_num_jugador, carta, carta_seleccionada
        global label_carta_seleccionada, label_carta_seleccionada2, botones, cartas
        global botonTirar, botonArrastrar, botonTocar, botonBajarse, botonCogerCarta

        ### habilitar todos los botones
        botonTirar.config(state=tk.NORMAL)
        botonArrastrar.config(state=tk.NORMAL)
        botonTocar.config(state=tk.NORMAL)
        botonBajarse.config(state=tk.NORMAL)
        botonCogerCarta.config(state=tk.NORMAL)

        mano_jugador = jugador.getMano()

        label_num_jugador.config(text=jugador.getnumJugador())
        
        # Calcular la altura de cada sección
        altura_seccion = frame_inferior.winfo_reqheight()
        ancho_seccion = frame_inferior.winfo_reqwidth() // 11 #len(mano_jugador)

        # Listas para almacenar las referencias a los botones y a las cartas

        botones = list()
        cartas = list()

        carta_seleccionada = ''

        for widget in frame_inferior.winfo_children():
            widget.destroy()

        if jugador.getCartaTirada() != None: # se pone en el frame superior la carta que le tiraron anteriormente

            global subframeCartaTirada
            subframeCartaTirada = tk.Frame(frame_superior, bg="darkblue", height=altura_seccion, width=ancho_seccion)
            subframeCartaTirada.grid(row = 0, column=8, rowspan=2, sticky="e", padx=0, pady=0)  # se alinean los subframes uno al lado del otro

            # Cargar la imagen
            imagen_path = f'Src/img/Classic/{jugador.getCartaTirada().getPinta()}/{jugador.getCartaTirada().getPinta()}{jugador.getCartaTirada().getDenominacion()}.png' 
            imagen = Image.open(imagen_path)
            image_redimensionada = imagen.resize((ancho_seccion - 8, altura_seccion - 8), Image.LANCZOS) # se redimensionan las imágenes al tamaño de los contenedores
            imagen = ImageTk.PhotoImage(image_redimensionada)

            ### botones con las cartas (no sé como se hace con un solo botón)
            # Mostrar la imagen en el botón
            label_cartaTirada = tk.Label(subframeCartaTirada, bg="gray", bd=4)
            label_cartaTirada.image = imagen  # Mantener una referencia a la imagen
            label_cartaTirada.config(image=imagen)  # Configurar la imagen en el botón
            label_cartaTirada.pack(fill="both", expand=True)


        for carta in mano_jugador: # se pone cada carta del jugador en los botones
            
            #cartas.append(carta)
            # Crear un subframe para cada sección
            subframe = tk.Frame(frame_inferior, bg="gray", height=altura_seccion, width=ancho_seccion)
            subframe.pack_propagate(False)  # se evita que el subframe se ajuste automáticamente
            subframe.pack(side="left")  # se alinean los subframes uno al lado del otro

            # Cargar la imagen
            imagen_path = f'Src/img/Classic/{carta.getPinta()}/{carta.getPinta()}{carta.getDenominacion()}.png' 
            imagen = Image.open(imagen_path)
            image_redimensionada = imagen.resize((ancho_seccion - 8, altura_seccion - 8), Image.LANCZOS) # se redimensionan las imágenes al tamaño de los contenedores
            imagen = ImageTk.PhotoImage(image_redimensionada)

            ### botones con las cartas (no sé como se hace con un solo botón)
            # Mostrar la imagen en el botón
            boton = tk.Button(subframe, bg="gray", bd=4, 
                              command=lambda img=imagen, c=carta: seleccionar_carta(img, c))
            boton.image = imagen  # Mantener una referencia a la imagen
            boton.config(image=imagen)  # Configurar la imagen en el botón
            boton.pack(fill="both", expand=True)

            # Agregar la referencia del botón a la lista
            botones.append(boton)
 

    def añadir_carta_adicional(carta):
        '''método para la cuando el usuario coja una carta tirada, o cuando arrastre'''

        global frame_inferior, frame_superior, altura_seccion, ancho_seccion, label_num_jugador
        global label_carta_seleccionada, label_carta_seleccionada2, botones, cartas, subframeCartaTirada
        global botonTocar, botonBajarse, botonCogerCarta, carta_seleccionada, label_carta_seleccionada, botones

        subframe = tk.Frame(frame_inferior, bg="gray", height=altura_seccion, width=ancho_seccion)
        subframe.pack_propagate(False)  # se evita que el subframe se ajuste automáticamente
        subframe.pack(side="left")  # se alinean los subframes uno al lado del otro

        # Cargar la imagen
        imagen_path = f'Src/img/Classic/{carta.getPinta()}/{carta.getPinta()}{carta.getDenominacion()}.png' 
        imagen = Image.open(imagen_path)
        image_redimensionada = imagen.resize((ancho_seccion - 8, altura_seccion - 8), Image.LANCZOS) # se redimensionan las imágenes al tamaño de los contenedores
        imagen = ImageTk.PhotoImage(image_redimensionada)

        ### botones con las cartas (no sé como se hace con un solo botón)
        # Mostrar la imagen en el botón
        boton = tk.Button(subframe, bg="gray", bd=4, 
                            command=lambda img=imagen, c=carta: seleccionar_carta(img, c))
        boton.image = imagen  # Mantener una referencia a la imagen
        boton.config(image=imagen)  # Configurar la imagen en el botón
        boton.pack(fill="both", expand=True)

        # Agregar la referencia del botón a la lista, deshabilitar el boton y destruir el frame de carta adicional
        botones.append(boton)
        botonCogerCarta.config(state=tk.DISABLED)
        botonArrastrar.config(state=tk.DISABLED)
        botonTocar.config(state=tk.DISABLED)
        botonBajarse.config(state=tk.DISABLED)
        subframeCartaTirada.destroy()

    def seleccionar_carta(imagen, carta):
        '''esta funcion sirve para seleccionar una carta'''

        global botonTocar, botonBajarse, carta_seleccionada, label_carta_seleccionada, botones
        for b in botones: # para que al dar click en una carta, esta tenga un marco rojo
            if str(b.cget("image")) == str(imagen):
                b.config(bg="red", bd=7)
            else:
                b.config(bg="green", bd=3)
        
        botonBajarse.config(state=tk.DISABLED) # Cambiar el color de fondo y borde del botón bajarse

        #label_carta_seleccionada.config(image=imagen)

        carta_seleccionada = carta


    def siguienteTurno(jugador):
        mostrar_cartas_jugador(jugador)

    def tirar():
        '''instrucciones cada que el jugador tira una carta'''

        global carta_seleccionada, j, num_jugadores_juego, juego
        accion = 'tirar'
        if carta_seleccionada != '':
            if len(juego.getJugadores()[j].getMano()) == 11:
                if j != (num_jugadores_juego - 1): # se valida que el jugador no sea el último de la lista juego.getJugadores()
                    juego.getJugadores()[j].tirar(juego.getJugadores()[j+1], carta_seleccionada)
                    j += 1
                else:
                    juego.getJugadores()[j].tirar(juego.getJugadores()[0], carta_seleccionada)
                    j = 0
                siguienteTurno(juego.getJugadores()[j])
            else:
                print('debes tener 11 cartas en tu mano para tirar')
        else:
            print('selecciona una carta')
                

    def arrastrar(): #falta
        # agregar aquí lo que pasará al hacer click en el botón 'arrastrar'
        accion = 'arrastrar'
        global carta_seleccionada, j, num_jugadores_juego, juego
        if len(juego.getJugadores()[j].getMano()) == 10:

            '''carta = choice(self.__baraja.getBaraja())   # Se escoge una carta al azar de una baraja
            if self.__mazo[carta] > 0:                  # Si la carta está disponible en el mazo, es decir si aún hay al menos una carta (en el mazo) de la escogida en una baraja
            jugador.añadirCarta(carta)                  # Se le añade la carta al jugador
            self.__mazo[carta] -= 1'''

            juego.getJugadores()[j].añadirCarta(juego.getJugadores()[j].getCartaTirada())
            añadir_carta_adicional(juego.getJugadores()[j].getCartaTirada())
        else:
            print('debes tener 10 cartas en tu mazo para poder arrastrar o coger la carta tirada')

    def tocar():
        # agregar aquí lo que pasará al hacer click en el botón 'tocar'
        global carta_seleccionada
        accion = 'tocar'
        pass

    def bajarse():
        global botonTocar
        # agregar aquí lo que pasará al hacer click en el botón 'bajarse'
        accion = 'bajarse'
        #botonTocar.config(state=tk.DISABLED)
        pass
    
    def coger_carta():
        # agregar aquí lo que pasará al hacer click en el botón 'cogerCarta'
        global carta_seleccionada, j, num_jugadores_juego, juego
        accion = 'cogerCarta'
        if len(juego.getJugadores()[j].getMano()) == 10:
            juego.getJugadores()[j].añadirCarta(juego.getJugadores()[j].getCartaTirada())
            añadir_carta_adicional(juego.getJugadores()[j].getCartaTirada())
        else:
            print('debes tener 10 cartas en tu mazo para poder arrastrar o coger la carta tirada')



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
