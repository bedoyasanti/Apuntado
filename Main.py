import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from PIL import ImageTk
from PIL import Image
from Src.Packages.Juego import Juego
from Src.Packages.Partida import Partida
from Src.Packages.Dealer import Dealer
import colorsys
from random import shuffle, choice
import sys
import time

class Apuntado:

    def __init__(self, estiloCartas):

        self.__estiloCartas = estiloCartas

        self.root = tk.Tk()
        iconp = Image.open('Src/img/Classic/Clubs/ClubsA.png')
        iconPhoto = ImageTk.PhotoImage(iconp)
        self.root.iconphoto(False, iconPhoto)

        self.root.title("Apuntado")

        accion = ''
        # Configurar el frame superior (verde)
        self.frame_info = tk.Frame(self.root, bg="green", height=300, width=600, bd=5, relief="ridge")
        self.frame_info.pack(padx=10, pady=10)

        # Configurar la lista de jugadores posibles
        lista_cant_jug = list(range(2, 7))
        self.lista_jugadores = ttk.Combobox(self.frame_info, width=3, values=lista_cant_jug, state="readonly")
        self.lista_jugadores.set(2)  # Establece el valor predeterminado
        self.lista_jugadores.grid(row=0, column=1, padx=10, pady=10, sticky="sw")

        # Configurar el label de jugadores
        self.labelJugadores_iniciales = tk.Label(self.frame_info, width=40, text='Elige la cantidad de jugadores de la partida:', font=("Arial", 12, "bold"))
        self.labelJugadores_iniciales.grid(row=0, column=0, padx=10, pady=10, sticky="sw")

        # Configurar el boton de comenzar
        self.boton_comenzar = tk.Button(self.frame_info, bg='red', text='Comenzar Juego', command=self.start, height=2, width=30, font=("Helvetica", 14, "italic bold"), bd=3, relief="raised")
        self.boton_comenzar.grid(row=1, column=0, padx=10, columnspan=2, pady=10)

        self.root.mainloop()

    def center_window(self, root, width, height):
        '''sirve para centrar la interfaz de juego'''

        # Obtener las dimensiones de la pantalla
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calcular las coordenadas para centrar la ventana
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        # Configurar la posición de la ventana
        self.root.geometry(f"{width}x{height}+{x}+{y}")

    def start(self):
        '''Se crea la interfaz de juego'''

        global frame_inferior, frame_superior, altura_seccion, ancho_seccion, frame_puntajes, label_info_general
        global label_carta_seleccionada, label_carta_seleccionada2, label_num_partida, label_num_jugador
        global botonTirar, botonArrastrar, botonTocar, botonBajarse, botonCogerCarta, botonCambiarCartas
        global lista_desplegable1, lista_desplegable2, lista_tocar, num_jugadores_juego

        num_jugadores_juego = int(self.lista_jugadores.get())

        for widget in self.root.winfo_children():
            widget.destroy()
        # Configurar el frame superior (verde)
        frame_superior = tk.Frame(self.root, bg="green", height=300, width=1300, bd=3, relief="solid")
        frame_superior.pack(fill="both", expand=True, padx=4, pady=4)

        # Configurar el frame inferior (gris)
        frame_inferior = tk.Frame(self.root, bg="gray", height=200, width=1300)
        frame_inferior.pack(fill="both", expand=True, padx=4, pady=4)


        label_info_general = tk.Label(frame_superior, bg='darkgreen', text='info general', height=3, width=40)
        label_info_general.grid(row=2, column=4, columnspan = 2, rowspan = 3, padx=5, pady=5)
        
        ### Labels
        # label de info partida
        label_info_partida = tk.Label(frame_superior, bg='darkgray', text='Partida #', height=3, width=10, bd=5, relief="solid")
        label_info_partida.grid(row=0, column=0, padx=10, pady=(2, 0))

        label_num_partida = tk.Label(frame_superior, bg='darkgreen', text = '1', height=3, width=10, bd=5, relief="solid")
        label_num_partida.grid(row=0, column=1, padx=10, pady=(2, 0))


        # label de jugador
        label_info_jugador = tk.Label(frame_superior, text = 'Jugador #', bg='darkgray', height=3, width=10, bd=5, relief="solid")
        label_info_jugador.grid(row=1, column=0, padx=10, pady=(2, 0))

        label_num_jugador = tk.Label(frame_superior, text = 'nn', bg='darkgreen', height=3, width=10, bd=5, relief="solid")
        label_num_jugador.grid(row=1, column=1, padx=10, pady=(2, 0))


        ### Botones
        # Boton de Cambiar Cartas
        botonCambiarCartas = tk.Button(frame_superior, text='Cambiar Cartas', bg="gray", bd=5, height=1, width=15, command=self.habilitarCampos)
        botonCambiarCartas.grid(row=4, column=0, padx=10, pady=10, sticky="sw") # rowspan=2,

        # Botón de Tocar
        botonTocar = tk.Button(frame_superior, text='Tocar', bg="gray", bd=5, height=1, width=15, command=self.crearCampoTocar)
        botonTocar.grid(row=3, column=0, padx=10, pady=10, sticky="sw")  # Alinear arriba

        # Botón de Tirar
        botonTirar = tk.Button(frame_superior, text='Tirar', bg="gray", bd=5, height=3, width=10, command=self.tirar)
        botonTirar.grid(row=0, column=4, padx=10, pady=10, sticky="n")  # Alinear arriba

        # Botón de Arrastrar
        botonArrastrar = tk.Button(frame_superior, text='Arrastrar', bg="gray", bd=5, height=3, width=10, command=self.arrastrar)
        botonArrastrar.grid(row=0, column=3, padx=0, pady=10, sticky="n")  # Alinear arriba
        #botonArrastrar.config(state=tk.DISABLED)

        # Boton de Ordenar Cartas
        botonOrdenar = tk.Button(frame_superior, text='Ordenar Cartas', bg="gray", bd=5, height=3, width=15, command=self.ordenarCartas)
        botonOrdenar.grid(row=0, column=5, padx=10, pady=10, sticky="n") #row=0, column=2, padx=10, pady=10, sticky="n"

        # Botón de Bajarse
        botonBajarse = tk.Button(frame_superior, text='Bajarse', bg="gray", bd=5, height=3, width=10, command=self.bajarse)
        botonBajarse.grid(row=0, column=2, padx=10, pady=10, sticky="n")  # Alinear arriba

        # Botón de Coger Carta Tirada
        botonCogerCarta = tk.Button(frame_superior, text='Coger Carta Tirada', bg="gray", bd=5, height=3, width=15, command=self.coger_carta)
        botonCogerCarta.grid(row=0, column=6, padx=10, pady=10, sticky="n")  # Alinear arriba


        ### frame de tabla puntajes:
        frame_puntajes = tk.Frame(frame_superior, bg="lightblue", height=200, width=100)
        frame_puntajes.grid(row=0, column=10, padx=40, pady=2, sticky="e", rowspan=2)


        self.center_window(self.root, 1300, 500) # Centrar la ventana en la pantalla

        self.comenzarNuevoJuego()
    
    def widget_existe(self, widget):
        global lista_desplegable1, lista_desplegable1, lista_tocar, botonSwap, botonT
        try:
            widget.winfo_exists()  # Intenta obtener información sobre el widget
            return True
        except: #tk.NameError
            return False
        
    def crearCampoTocar(self):
        '''se crea la lista desplegable, donde el usuario ingresará el número de cartas con las que quier tocar
        (se le debe especificar que esta(s) carta(s) son las primeras 2 (a lo sumo) de su mazo)'''

        global lista_tocar, juego, j, botonTocar, habilitarTocar, frame_superior, botonT, label_info_general

        botonTocar.config(state='disabled') # SI 
        habilitarTocar = True

        texto = 'las cartas con las que quieres tocar, deben estar\nen la(s) primera(s) posicion(es) de tu mano'
        label_info_general.config(text = texto)
        self.root.after(4000, lambda: label_info_general.config(text = ''))
        lista_tocar = ttk.Combobox(frame_superior, width = 3, values=[1,2], state="readonly")
        lista_tocar.set(1)  # Establece el valor predeterminado
        lista_tocar.grid(row=3, column=1, padx=10, pady=10, sticky="sw")

        # Boton para Tocar
        botonT = tk.Button(frame_superior, text='Tocar', bg="gray", bd=5, height=1, width=15, command=self.tocar)
        botonT.grid(row=3, column=2, padx=10, pady=10, sticky="sw")

        botonTocar.config(state="disabled") # SI

    def tocar(self): # validar cuando el jugador tenga suficientes puntos para tocar con la(s) carta(s) elegidas
        global juego, j, habilitarTocar, partida, botonT, label_info_general

        cartas_tocar = int(lista_tocar.get())
        if len(juego.getJugadores()[j].getMano()) == 10:
            if cartas_tocar == 1:
                M = juego.getJugadores()[j].getMano().copy()
                Mano = M.copy()
                Mano.append(Mano.pop(0))
                juego.getJugadores()[j].setMano(Mano)
                if (juego.getJugadores()[j].getPuntaje() + Mano[-1].getValor()) >= 101:
                    texto = f'no puedes tocar con esa carta, tienes {juego.getJugadores()[j].getPuntaje()} puntos'
                    label_info_general.config(text = texto)
                    self.root.after(6000, lambda: label_info_general.config(text = ''))
                    return
                
                if partida.getDealer().validarTocar(juego.getJugadores()[j], Mano[-1]):
                    self.acabaPartida(1)
                else:
                    juego.getJugadores()[j].setMano(M)
                    texto = 'tu mano no es válida para tocar'
                    label_info_general.config(text = texto)
                    self.root.after(6000, lambda: label_info_general.config(text = ''))
            elif cartas_tocar == 2:
                M = juego.getJugadores()[j].getMano().copy() # se crea una copia de la mano del jugador (para reasignarsela al jugador si no se puede tocar)
                Mano = M.copy() # se crea una copia de la copia inicial
                Mano.append(Mano.pop(0)) # se pone como ultima carta la primera
                Mano.append(Mano.pop(0)) # se pone como ultima carta la primera
                juego.getJugadores()[j].setMano(Mano) # se actualiza la mano del jugador con la mano modificada
                if (juego.getJugadores()[j].getPuntaje() + Mano[-1].getValor() + Mano[-2].getValor()) >= 101:
                    texto = f'no puedes tocar con esas cartas, tienes {juego.getJugadores()[j].getPuntaje()} puntos'
                    label_info_general.config(text = texto)
                    self.root.after(4000, lambda: label_info_general.config(text = ''))
                    return
                
                if partida.getDealer().validarTocar(juego.getJugadores()[j], 
                                                    Mano[-1], Mano[-2]):
                    self.acabaPartida(2)
                else:
                    juego.getJugadores()[j].setMano(M) # en caso de que no se pueda tocar, se le vuelve a asignar la misma mano incial
                    texto = 'tu mano no es válida para tocar'
                    label_info_general.config(text = texto)
                    self.root.after(4000, lambda: label_info_general.config(text = ''))
        else:
            texto = 'debes tener 10 cartas para tocar'
            label_info_general.config(text = texto)
            self.root.after(4000, lambda: label_info_general.config(text = ''))
        # se eliminan los objetos de cambiar cartas
        lista_tocar.destroy()
        botonT.destroy()
        habilitarTocar = False

        botonTocar.config(state="normal")

    def habilitarCampos(self):
        '''se crean las dos listas desplegables para que el usuario ingrese las cartas que quiere intercambiar 
        de su mano, y el boton 'swap', que llama al metodo para intercambiar las cartas seleccionadas'''

        global lista_desplegable1, lista_desplegable2, botonSwap, juego, j, habilitar, botonCambiarCartas

        botonCambiarCartas.config(state="disabled") # SI
        habilitar = True
        valores = list(range(1, (len(juego.getJugadores()[j].getMano()) + 1)))
        lista_desplegable1 = ttk.Combobox(frame_superior, width = 3, values=valores, state="readonly")
        lista_desplegable1.set(valores[0])  # Establece el valor predeterminado
        lista_desplegable1.grid(row=4, column=1, padx=10, pady=10, sticky="sw")

        # lista 2
        # Listas Desplegables cambiar cartas
        valores = list(range(1, (len(juego.getJugadores()[j].getMano()) + 1)))
        lista_desplegable2 = ttk.Combobox(frame_superior, width = 3, values=valores, state="readonly")
        lista_desplegable2.set(valores[0])  # Establece el valor predeterminado
        lista_desplegable2.grid(row=4, column=2, padx=10, pady=10, sticky="sw")

        # Boton de Cambiar Cartas
        botonSwap = tk.Button(frame_superior, text='Swap', bg="gray", bd=5, height=1, width=15, command=self.swap)
        botonSwap.grid(row=4, column=3, padx=10, pady=10, sticky="sw")

        '''lista_desplegable1["state"] = "disabled"
        lista_desplegable2["state"] = "disabled"'''

    def swap(self):
        global juego, j, habilitar, botonCambiarCartas
        
        valor_seleccionado_1 = int(lista_desplegable1.get())
        valor_seleccionado_2 = int(lista_desplegable2.get())

        juego.getJugadores()[j].modificarMano((valor_seleccionado_1 - 1), (valor_seleccionado_2 - 1))

        # se eliminan los objetos de cambiar cartas
        lista_desplegable1.destroy()
        lista_desplegable2.destroy()
        botonSwap.destroy()
        habilitar = False

        botonCambiarCartas.config(state="normal")
        self.mostrar_cartas_jugador(juego.getJugadores()[j], True)

    def acabaPartida(self, cantTocar: int = 0):
        global botonTocar, juego, frame_inferior, j, subframeCartaTirada, partida

        otros_jugadores = juego.getJugadores()[:j] + juego.getJugadores()[j+1:]

        if cantTocar != 0:
            partida.getDealer().comprobarManos(juego.getJugadores()[j], otros_jugadores, cantTocar) # Método que comprueba las manos del ganador, y los otros jugadores de la partida
        else:
            partida.getDealer().comprobarManos(juego.getJugadores()[j], otros_jugadores)
        for widget in frame_inferior.winfo_children(): # se borra todo lo que esté en el frame inferior
            widget.destroy()
            
        for jugador in juego.getJugadores():
            jugador.setGanador(False) # se actualizan los valores de ganador para todos los jugadores
            jugador.setCartaTirada(None) # se pone None en el atributo de carta tirada de los jugadores

        juego.getJugadores()[j].setGanador(True) # se pone un valor de True en el atributo ganador del jugador

        subframeCartaTirada.destroy() # FALTA destruir todo lo del frame
        self.comenzarNuevaPartida()
        
    def comenzarNuevoJuego(self):
        '''se crea un juego, y se randomiza el orden de la lista de jugadores'''

        global j, num_jugadores_juego, juego, numero_partidas, num_jugadores_juego

        ### Se empieza un nuevo juego
        #num_jugadores_juego = 2

        juego = Juego(num_jugadores_juego) # se inicia un juego con (num_jugadores_juego) jugadores
        shuffle(juego.getJugadores()) # se randomiza el orden de la lista de jugadores

        juego.getJugadores()[0].setGanador(True) # se comienza como si el primer jugador hubiera ganado, por simplicidad, para darle a él 11 cartas

        numero_partidas = 0
        self.comenzarNuevaPartida()

    def comenzarNuevaPartida(self):
        '''se crea una nueva partida, se reparten las cartas y se establece qué jugador empieza de primero'''

        global juego, j, partida, numero_partidas, label_num_partida, ganador, mano_inicial, partida
        global botonTirar, botonArrastrar, botonTocar, botonBajarse, botonCogerCarta, turno1, mazo_auxiliar

        numero_partidas += 1
        label_num_partida.config(text = f"{numero_partidas}")

        # Crear y mostrar el mensaje temporizado
        #print(f'Partida # {numero_partidas}')

        for jugador in juego.getJugadores(): # se actualizan / borran las manos de los jugadores en cada partida
            jugador.setMano(list())

        partida = Partida(juego.getJugadores()) # se crea la partida

        mazo_auxiliar = partida.getMazo().copy()

        partida.getDealer().repartirCartas(juego.getJugadores(), partida.getMazo(), partida.getBaraja()) # se reparten las cartas

        for j in range(len(juego.getJugadores())): # se establece quien es el jugador que comienza (el de las 11 cartas)
            if len(juego.getJugadores()[j].getMano()) == 11:
                mano_inicial = juego.getJugadores()[j].getMano()
                break

            #while True:
        
        # el jugador que comienza la partida, solo puede tirar carta
        botonCogerCarta.config(state=tk.DISABLED) # SI
        botonArrastrar.config(state=tk.DISABLED) # SI
        botonTocar.config(state=tk.DISABLED) # SI
        botonBajarse.config(state=tk.DISABLED) # SI

        turno1 = True # para verificar si es el primer turno de una partida
        self.actualizarTablaPuntajes()
        self.mostrar_cartas_jugador(juego.getJugadores()[j], False)

    def actualizarTablaPuntajes(self):
        '''se crean labels con la info de los puntajes de los jugadores'''

        global juego, j, frame_puntajes

        self.definirGanador_Perdedores() # se actualizan ganadores y perdedores

        for widget in frame_puntajes.winfo_children(): # se borra todo lo que esté en el frame inferior
                widget.destroy()

        i = 0
        for jug in juego.getJugadores(): #FALTA destruir lo que halla dentro del frame
            label_jugador = tk.Label(frame_puntajes, text = f'Jugador # {jug.getnumJugador()}', bg='darkgray', height=1, width=10)
            label_jugador.grid(row=i, column=0, padx=0, pady=0)

            label_puntaje = tk.Label(frame_puntajes, text = f'{jug.getPuntaje()}', bg='darkgreen', height=1, width=10)
            label_puntaje.grid(row=i, column=1, padx=0, pady=0)
            i += 1

    def definirGanador_Perdedores(self):
        '''acá se verificarán cuales jugadores pueden seguir jugando, y cuales no'''

        global juego, j, label_info_general

        i = 0
        while i != len(juego.getJugadores()): # se sacan lo jugadores con mas de 101 puntos
            texto = ''
            if juego.getJugadores()[i].getPuntaje() >= 101: #cambiar
                texto = texto + f'Sale el jugador {juego.getJugadores()[i].getnumJugador()}, acumuló {juego.getJugadores()[i].getPuntaje()} puntos\n'
                juego.getJugadores().remove(juego.getJugadores()[i])
            else:
                i += 1
            if texto != '':
                label_info_general.config(text = texto)
                self.root.after(6000, lambda: label_info_general.config(text = ''))

        for jug2 in juego.getJugadores(): # se actualiza el valor de j, variable que itera en la lista de jugadores
            if jug2.isGanador():
                j = juego.getJugadores().index(jug2)
                break
        
        texto = 'Felicidades!!! El ganador del juego es el jugador número'

        if len(juego.getJugadores()) == 1: # se valida si queda solo un jugador en el juego
                texto = f'{texto} {juego.getJugadores()[0].getnumJugador()}, el último sobreviviente del juego!!!'
                label_info_general.config(text = texto)
                self.root.after(4000, lambda: label_info_general.config(text = ''))
                for widget in self.root.winfo_children(): # se borra toda la interfaz FALTA - error
                    widget.destroy()

                messagebox.showinfo('Hay un ganador en la partida!!!', texto)
                # Salir del programa
                sys.exit()

        for jug in juego.getJugadores():
            if jug.getPuntaje() <= -50:
                texto = f'{texto} {jug.getnumJugador()} acumuló {jug.getPuntaje()} puntos'
                label_info_general.config(text = texto)
                self.root.after(4000, lambda: label_info_general.config(text = ''))
                for widget in self.root.winfo_children(): # se borra toda la interfaz
                    widget.destroy()

                messagebox.showinfo('Hay un ganador en la partida!!!', texto)
                # Salir del programa
                sys.exit()

    def mostrar_cartas_jugador(self, jugador, orden):
        '''se muestran las cartas del jugador, poniéndolas en botones'''

        global frame_inferior, frame_superior, altura_seccion, ancho_seccion, label_num_jugador, carta, carta_seleccionada
        global subframeCartaTirada, turno1
        global label_carta_seleccionada, label_carta_seleccionada2, botones, cartas
        global botonTirar, botonArrastrar, botonTocar, botonBajarse, botonCogerCarta, ordenar

        if len(juego.getJugadores()[j].getMano()) == 10:
            ### habilitar todos los botones
            botonTirar.config(state=tk.NORMAL)
            botonArrastrar.config(state=tk.NORMAL)
            botonTocar.config(state=tk.NORMAL)
            botonBajarse.config(state=tk.NORMAL)
            botonCogerCarta.config(state=tk.NORMAL)
            botonCambiarCartas.config(state=tk.NORMAL)
        else:
            ### habilitar todos los botones
            #botonTirar.config(state=tk.DISABLED)
            botonArrastrar.config(state=tk.DISABLED)
            botonTocar.config(state=tk.DISABLED)
            botonBajarse.config(state=tk.DISABLED)
            botonCogerCarta.config(state=tk.DISABLED)

        mano_jugador = jugador.getMano()

        label_num_jugador.config(text=jugador.getnumJugador())
        
        # Calcular la altura y ancho de cada sección
        altura_seccion = frame_inferior.winfo_reqheight()
        ancho_seccion = 118 #frame_inferior.winfo_reqwidth() // 11

        # Listas para almacenar las referencias a los botones y a las cartas

        botones = list()
        cartas = list()

        carta_seleccionada = ''

        for widget in frame_inferior.winfo_children():
            widget.destroy()

        if jugador.getCartaTirada() != None and not orden: # se pone en el frame superior la carta que le tiraron anteriormente
            
            subframeCartaTirada = tk.Frame(frame_superior, bg="darkblue", height=altura_seccion, width=ancho_seccion)
            subframeCartaTirada.grid(row = 0, column=8, rowspan = 5, sticky="e", padx=10, pady=(15, 0))  # se alinean los subframes uno al lado del otro
        
            # Cargar la imagen
            imagen_path = f'Src/img/{self.__estiloCartas}/{jugador.getCartaTirada().getPinta()}/{jugador.getCartaTirada().getPinta()}{jugador.getCartaTirada().getDenominacion()}.png' 
            imagen = Image.open(imagen_path)
            image_redimensionada = imagen.resize((ancho_seccion - 8, altura_seccion - 8), Image.LANCZOS) # se redimensionan las imágenes al tamaño de los contenedores
            imagen = ImageTk.PhotoImage(image_redimensionada)

            ### botones con las cartas (no sé como se hace con un solo botón)
            # Mostrar la imagen en el botón
            label_cartaTirada = tk.Label(subframeCartaTirada, bg="gray", bd=4)
            label_cartaTirada.image = imagen  # Mantener una referencia a la imagen
            label_cartaTirada.config(image=imagen)  # Configurar la imagen en el botón
            label_cartaTirada.pack(fill="both", expand=True)


        else:
            if not turno1: # verificar esto
                # actualizo el valor de carta tirada del jugador, y elimino el frame
                juego.getJugadores()[j].setCartaTirada(None)
                for widget in subframeCartaTirada.winfo_children(): # se borra todo lo que esté en el frame inferior
                    widget.destroy()
                subframeCartaTirada.destroy()
                turno1 = False

        for carta in mano_jugador: # se pone cada carta del jugador en los botones
            
            # Crear un subframe para cada sección
            subframe = tk.Frame(frame_inferior, bg="gray", height=altura_seccion, width=ancho_seccion)
            subframe.pack_propagate(False)  # se evita que el subframe se ajuste automáticamente
            subframe.pack(side="left")  # se alinean los subframes uno al lado del otro

            # Cargar la imagen
            imagen_path = f'Src/img/{self.__estiloCartas}/{carta.getPinta()}/{carta.getPinta()}{carta.getDenominacion()}.png' 
            imagen = Image.open(imagen_path)
            image_redimensionada = imagen.resize((ancho_seccion - 8, altura_seccion - 8), Image.LANCZOS) # se redimensionan las imágenes al tamaño de los contenedores
            imagen = ImageTk.PhotoImage(image_redimensionada)

            ### 
            # Mostrar la imagen en el botón
            boton = tk.Button(subframe, bg="gray", bd=4, 
                              command=lambda img=imagen, c=carta: self.seleccionar_carta(img, c))
            boton.image = imagen  # Mantener una referencia a la imagen
            boton.config(image=imagen)  # Configurar la imagen en el botón
            boton.pack(fill="both", expand=True)

            # Agregar la referencia del botón a la lista
            botones.append(boton)
 

    def añadir_carta_adicional(self, carta):
        '''método para cuando el usuario coja una carta tirada, o cuando arrastre'''

        global frame_inferior, frame_superior, altura_seccion, ancho_seccion, label_num_jugador
        global label_carta_seleccionada, label_carta_seleccionada2, botones, cartas, subframeCartaTirada
        global botonTocar, botonBajarse, botonCogerCarta, label_carta_seleccionada, botones

        subframe = tk.Frame(frame_inferior, bg="gray", height=altura_seccion, width=ancho_seccion)
        subframe.pack_propagate(False)  # se evita que el subframe se ajuste automáticamente
        subframe.pack(side="left")  # se alinean los subframes uno al lado del otro

        # Cargar la imagen
        imagen_path = f'Src/img/{self.__estiloCartas}/{carta.getPinta()}/{carta.getPinta()}{carta.getDenominacion()}.png' 
        imagen = Image.open(imagen_path)
        image_redimensionada = imagen.resize((ancho_seccion - 8, altura_seccion - 8), Image.LANCZOS) # se redimensionan las imágenes al tamaño de los contenedores
        imagen = ImageTk.PhotoImage(image_redimensionada)

        ### botones con las cartas
        # Mostrar la imagen en el botón
        boton = tk.Button(subframe, bg="gray", bd=4, 
                            command=lambda img=imagen, c=carta: self.seleccionar_carta(img, c))
        boton.image = imagen  # Mantener una referencia a la imagen
        boton.config(image=imagen)  # Configurar la imagen en el botón
        boton.pack(fill="both", expand=True)

        # Agregar la referencia del botón a la lista, deshabilitar el boton y destruir el frame de carta adicional
        botones.append(boton)
        botonCogerCarta.config(state=tk.DISABLED) # SI
        botonArrastrar.config(state=tk.DISABLED) # SI
        botonTocar.config(state=tk.DISABLED) # SI
        botonBajarse.config(state=tk.DISABLED) # SI

        # actualizo el valor de carta tirada del jugador, y elimino el frame
        juego.getJugadores()[j].setCartaTirada(None)
        #subframeCartaTirada.destroy()

        for widget in subframeCartaTirada.winfo_children(): # se borra todo lo que esté en el frame inferior
                widget.destroy()
        subframeCartaTirada.destroy()

    def seleccionar_carta(self, imagen, carta):
        '''esta funcion sirve para seleccionar una carta'''

        global botonTocar, botonBajarse, carta_seleccionada, label_carta_seleccionada, botones
        for b in botones: # para que al dar click en una carta, esta tenga un marco rojo
            if str(b.cget("image")) == str(imagen): # and carta != carta_seleccionada
                b.config(bg="red", bd=7)
            else:
                b.config(bg="green", bd=3)
        
        #botonBajarse.config(state=tk.DISABLED)

        #label_carta_seleccionada.config(image=imagen)

        carta_seleccionada = carta


    def ordenarCartas(self):
        global j, juego, ordenar

        ordenar = True
        i = (len(juego.getJugadores()[j].getMano()) - 1) #bubblesorting para ordenar la mano
        while i != 0:
            for e in range(0, i):
                if juego.getJugadores()[j].getMano()[e].getden2() > juego.getJugadores()[j].getMano()[e+1].getden2():
                    juego.getJugadores()[j].modificarMano(e,e+1)
            i -= 1

        self.mostrar_cartas_jugador(juego.getJugadores()[j], True)


    def siguienteTurno(self, jugador):
        global lista_desplegable1, lista_desplegable2, botonSwap, habilitar, habilitarTocar, turno1, label_info_general
        global botonT, listaTocar
        # se eliminan los objetos de cambiar cartas

        try:
            if self.widget_existe(lista_desplegable1):
                lista_desplegable1.destroy()
        except:
            pass
        try:
            if self.widget_existe(lista_desplegable2):
                lista_desplegable2.destroy()
        except:
            pass
        try:
            if self.widget_existe(botonSwap):
                botonSwap.destroy()
        except:
            pass
        try:
            if self.widget_existe(lista_tocar):
                lista_tocar.destroy()
        except:
            pass
        try:
            if self.widget_existe(botonT):
                botonT.destroy()
        except:
            pass
        
        #time.sleep(5)
        '''texto = f"Turno del jugador {juego.getJugadores()[j].getnumJugador()}"
        label_info_general.config(text=texto)

        #time.sleep(5)
        self.root.after(4000, lambda: label_info_general.config(text = ''))'''

        #self.mostrar_contador(juego.getJugadores()[j].getnumJugador())
        #time.sleep(1)
        texto = f"Turno del jugador {juego.getJugadores()[j].getnumJugador()}"

        messagebox.showinfo('Siguiente Turno', texto)

        label_info_general.config(text=texto)
        self.root.after(4000, lambda: label_info_general.config(text = ''))
        #time.sleep(4)
        #self.root.after(4000, lambda: label_info_general.config(text = ''))
        botonCambiarCartas.config(state="normal")
        self.mostrar_cartas_jugador(jugador, False)

    def tirar(self):
        '''instrucciones cada que el jugador tira una carta'''

        global carta_seleccionada, j, num_jugadores_juego, juego, ordenar, label_info_general
        accion = 'tirar'
        if carta_seleccionada != '':
            if len(juego.getJugadores()[j].getMano()) == 11:
                if j != (len(juego.getJugadores()) - 1): # se valida que el jugador no sea el último de la lista juego.getJugadores()
                    juego.getJugadores()[j].tirar(juego.getJugadores()[j+1], carta_seleccionada)
                    j += 1
                else:
                    juego.getJugadores()[j].tirar(juego.getJugadores()[0], carta_seleccionada)
                    j = 0

                ordenar = False
                self.siguienteTurno(juego.getJugadores()[j])
            else:
                texto = 'debes tener 11 cartas en tu mano para tirar'
                label_info_general.config(text = texto)
                self.root.after(4000, lambda: label_info_general.config(text = ''))
        else:
            texto = 'selecciona una carta primero'
            label_info_general.config(text = texto)
            self.root.after(4000, lambda: label_info_general.config(text = ''))

    def arrastrar(self): # FALTA verificar que el mazo no esté casi vacío
        '''instrucciones cada que el jugador arrastra una carta'''

        accion = 'arrastrar'
        global carta_seleccionada, j, num_jugadores_juego, juego, partida, label_info_general, mazo_auxiliar

        if len(juego.getJugadores()[j].getMano()) == 10:
            juego.getJugadores()[j].setCartaTirada(None) # se borra la carta que tenía en el atributo de cartaTirada
            contador = 0
            while True:
                if contador == 3:
                    partida.setMazo(mazo_auxiliar)
                carta = choice(partida.getBaraja().getBaraja())    # Se escoge una carta al azar de una baraja
                if partida.getMazo()[carta] > 0:                   # Si la carta está disponible en el mazo, es decir si aún hay al menos una carta (en el mazo) de la escogida en una baraja
                    juego.getJugadores()[j].añadirCarta(carta)     # Se le añade la carta al jugador
                    partida.getMazo()[carta] -= 1
                    #print(carta.getPinta(), carta.getDenominacion())
                    self.añadir_carta_adicional(carta)
                    break
                contador += 1
            
        else:
            texto = 'debes tener 10 cartas en tu mazo para poder arrastrar o coger la carta tirada'
            label_info_general.config(text = texto)
            self.root.after(4000, lambda: label_info_general.config(text = ''))

    def bajarse(self):
        '''acá se actualizará el valor del puntaje de cada uno de los juagdores, y se comenzará una nueva partida
        (falta validar quien gana el juego y quien sale de él)'''

        global botonTocar, juego, frame_inferior, j, subframeCartaTirada, partida, label_info_general

        accion = 'bajarse'
        if partida.getDealer().validarBajarse(juego.getJugadores()[j]): # con esta función se garantiza que el jugador se puede bajar
            otros_jugadores = juego.getJugadores()[:j] + juego.getJugadores()[j+1:]
            partida.getDealer().comprobarManos(juego.getJugadores()[j], otros_jugadores) # Método que comprueba las manos del ganador, y los otros jugadores de la partida

            for widget in frame_inferior.winfo_children(): # se borra todo lo que esté en el frame inferior
                widget.destroy()
            
            for jugador in juego.getJugadores():
                jugador.setGanador(False) # se actualizan los valores de ganador para todos los jugadores
                jugador.setCartaTirada(None) # se pone None en el atributo de carta tirada de los jugadores

            juego.getJugadores()[j].setGanador(True) # se pone un valor de True en el atributo ganador del jugador

            subframeCartaTirada.destroy() # FALTA destruir todo lo del frame
            self.comenzarNuevaPartida()

        else:
            texto = 'Todavía no te puedes bajar'
            label_info_general.config(text = texto)
            self.root.after(4000, lambda: label_info_general.config(text = ''))
    
    def coger_carta(self):
        # agregar aquí lo que pasará al hacer click en el botón 'cogerCarta'
        global carta_seleccionada, j, num_jugadores_juego, juego, label_info_general
        accion = 'cogerCarta'
        if len(juego.getJugadores()[j].getMano()) == 10:
            juego.getJugadores()[j].añadirCarta(juego.getJugadores()[j].getCartaTirada())
            self.añadir_carta_adicional(juego.getJugadores()[j].getCartaTirada())
        else:
            texto = 'debes tener 10 cartas en tu mazo para poder arrastrar o coger la carta tirada'
            label_info_general.config(text = texto)
            self.root.after(4000, lambda: label_info_general.config(text = ''))

    def mostrar_contador(self, numero_jugador):
        global ventana, mensaje_label
        ventana = tk.Tk()
        ventana.title(f"Felicidades!!!")

        frame = tk.Frame(ventana, padx=20, pady=20, height = 300, width = 800)
        frame.pack()

        mensaje_label = tk.Label(frame, text="")
        mensaje_label.pack()

        def cerrar_ventana():
            global ventana
            ventana.destroy()

        def iniciar_cuenta_regresiva(n):
            global ventana, mensaje_label
            mensaje_label.config(text=f"Turno del jugador {n} en:")
            ventana.update()

            for i in range(5, 0, -1):
                mensaje_label.config(text=f"Turno del jugador {n} en: {i} segundos")
                ventana.update()
                time.sleep(1)

            ventana.after(0, cerrar_ventana)

        iniciar_cuenta_regresiva(numero_jugador)
        #ventana.mainloop()

