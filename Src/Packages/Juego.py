from Src.Packages.Jugador import Jugador
from Src.Packages.Partida import Partida
from random import shuffle

class Juego:
    def __init__(self, jugadores):          ### Método para crear un juego ##
        self.__tablaPuntajes = {}
        self.__jugadores = list()
        for i in range(jugadores):
            self.__jugadores.append(Jugador())

    def getJugadores(self):
        return self.__jugadores

    def jugarJuego(self):                 ### Método para iniciar el juego ###
        shuffle(self.__jugadores)   # Primero se randomiza la lista de jugadores, para escoger aleatoriamente al primer jugador y los turnos en la primera partida
        first = True            # Se crea un controlador para cuando sea la primera partida
        P = Partida(self.__jugadores)
        P.jugarPartida()
        '''while True:
            if first:
                P = Partida(self.jugadores)
                P.jugarPartida()'''

                
# Ya continuaremos con la lógica