from random import choice
from Src.Packages.Baraja import Baraja
from Src.Packages.Dealer import Dealer

class Partida:
    def __init__(self, turnos):                     ### Método para crear una partida ###
        self.__turnos = turnos
        self.__dealer = Dealer()
        self.__mazo = {}
        self.__baraja = Baraja()
        
        for carta in self.__baraja.getBaraja():
            self.__mazo[carta] = 2          # La partida comienza con 2 barajas, por lo que cada carta se muestra 2 veces
        
    def jugarPartida(self):                         ### Método para jugar una partida ###
        self.__dealer.repartirCartas(self.__turnos,self.__mazo)               # Se comienza repartiendo las cartas a los jugadores

    def getMazo(self):
        return self.__mazo

    def setMazo(self, mazo_nuevo : dict()):
        self.__mazo = mazo_nuevo

    def getDealer(self):
        return self.__dealer
    
    def getBaraja(self):
        return self.__baraja