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
        first = True    # Se crea un controlador para asignarle al primer jugador 11 cartas
        for i in range(len(self.__turnos)):
            jugador : Jugador = self.__turnos[i]# Se itera sobre los turnos de jugadores, dada la prioridad
            while True:
                if len(jugador.getMano()) == 10:# Si el jugador ya tiene 10 cartas en su mano, se rompe el ciclo
                    if first:
                        while True:
                            carta11 = choice(self.__baraja.getBaraja())
                            if self.__mazo[carta11] > 0:
                                jugador.añadirCarta(carta11)
                                self.__mazo[carta11] -= 1
                                first = False
                                break
                    break
                
                #no entendí :(
                '''if first:                                       # En caso de que sea el primer jugador, se le dará primero la carta 11,
                    carta11 = choice(self.__baraja.getBaraja()) # es decir, la carta que se le da de más al jugador que comienza la partida
                    jugador.setCartaTirada(carta11)             # pero se le entrega como si fuera una carta que le tiraron por facilidad de la programación :)
                    self.__mazo[carta11] -= 1                   # y se actualiza el mazo de la partida
                    #first = False                               # También se actualiza el controlador del primer jugador
                    jugador.añadirCarta(carta11)'''

                carta = choice(self.__baraja.getBaraja())   # Se escoge una carta al azar de una baraja
                if self.__mazo[carta] > 0:                  # Si la carta está disponible en el mazo, es decir si aún hay al menos una carta (en el mazo) de la escogida en una baraja
                    jugador.añadirCarta(carta)              # Se le añade la carta al jugador
                    self.__mazo[carta] -= 1                 # Se actualiza el mazo de la partida
