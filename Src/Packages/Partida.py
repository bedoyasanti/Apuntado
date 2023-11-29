from random import choice
from Src.Packages.Baraja import Baraja
from Src.Packages.Jugador import Jugador

class Partida:
    def __init__(self, turnos):                     ### Método para crear una partida ###
        self.__turnos = turnos
        self.__baraja = Baraja()
        self.__mazo = {}
        for carta in self.__baraja.getBaraja():
            self.__mazo[carta] = 2          # La partida comienza con 2 barajas, por lo que cada carta se muestra 2 veces
        
    def jugarPartida(self):                         ### Método para jugar una partida ###
        self.repartirCartas()               # Se comienza repartiendo las cartas a los jugadores

    def getMazo(self):
        return self.__mazo
    
    def getBaraja(self):
        return self.__baraja
    
    def repartirCartas(self):                       ### Método para repartir cartas a los jugadores ###
        for i in range(len(self.__turnos)):
            jugador : Jugador = self.__turnos[i]# Se itera sobre los turnos de jugadores, dada la prioridad
            while True:
                if len(jugador.getMano()) == 10:# Si el jugador ya tiene 10 cartas en su mano, se le añade otra si es el ganador
                    if jugador.getGanador():
                        while True:
                            carta11 = choice(self.__baraja.getBaraja())
                            if self.__mazo[carta11] > 0:
                                jugador.añadirCarta(carta11)
                                self.__mazo[carta11] -= 1
                                break
                    break

                carta = choice(self.__baraja.getBaraja())   # Se escoge una carta al azar de una baraja
                if self.__mazo[carta] > 0:                  # Si la carta está disponible en el mazo, es decir si aún hay al menos una carta (en el mazo) de la escogida en una baraja
                    jugador.añadirCarta(carta)              # Se le añade la carta al jugador
                    self.__mazo[carta] -= 1                 # Se actualiza el mazo de la partida
