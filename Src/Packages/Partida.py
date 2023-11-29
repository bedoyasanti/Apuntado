from random import choice
from Src.Packages.Baraja import Baraja
from Src.Packages.Dealer import Dealer

class Partida:
    def __init__(self, turnos):                     ### Método para crear una partida ###
        self.__turnos = turnos
        self.__dealer = Dealer()
        self.__mazo = {}
        baraja = Baraja()
        for carta in baraja.getBaraja():
            self.__mazo[carta] = 2          # La partida comienza con 2 barajas, por lo que cada carta se muestra 2 veces
        
    def jugarPartida(self):                         ### Método para jugar una partida ###
        self.__mazo = self.__dealer.repartirCartas(self.__turnos,self.__mazo)               # Se comienza repartiendo las cartas a los jugadores

    def getMazo(self):
        mazo = []
        for carta, disp in self.__mazo.items():
            if disp > 0:
                mazo.append(carta)
        return mazo