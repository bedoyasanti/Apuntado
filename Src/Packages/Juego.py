from Jugador import Jugador
from Partida import Partida
from random import shuffle

class Juego:
    def __init__(self, jugadores):          ### Método para crear un juego ##
        self.__jugadores = jugadores
        self.__tablaPuntajes = {}

    def jugarJuego(self):                   ### Método para iniciar el juego ###
        shuffle(self.__jugadores)   # Primero se randomiza la lista de jugadores, para escoger aleatoriamente al primer jugador y los turnos en la primera partida
        first = True            # Se crea un controlador para cuando sea la primera partida
        while True:
            if first:
                P = Partida(self.__jugadores)

# Ya continuaremos con la lógica