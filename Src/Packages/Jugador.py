from Src.Packages.Carta import Carta
class Jugador:                              # PD: Luego hay que crear la clase usuario y jugador heredará de usuario
    contador_jugadores = 0  # Variable de clase para contar jugadores

    def __init__(self):
        Jugador.contador_jugadores += 1  # Incrementar el contador de jugadores al crear una instancia
        self.__numero_jugador = Jugador.contador_jugadores  # Asignar el número de jugador restando 1 para empezar desde 0
        self.__mano = []
        self.__cartaTirada = None
        self.__cartaPorTirar = None
        self.__cartaTocar1 = None
        self.__cartaTocar2 = None
        self.__puntos = 0
        self.__ganador = False
        self.__perdedor = False

    def getnumJugador(self):
        return self.__numero_jugador
    
    def añadirCarta(self, carta: Carta):    ### Método para añadir una carta a la mano ###
        self.__mano.append(carta)
    
    def modificarMano(self, idx1, idx2):    ### Método que se invocará cada que el jugador modifique las posiciones de su mano ###
        self.__mano[idx1], self.__mano[idx2] = self.__mano[idx2], self.__mano[idx1]
    
    def getCartaTirada(self):               ### Método para acceder a la carta que el jugador anterior le tiró ###
        return self.__cartaTirada
    
    def setCartaTirada(self, carta): # : Carta ### Método para establecer la carta que el jugador anterior le tiró, útil para el método tirar() ###
        self.__cartaTirada = carta

    def tirar(self, jugador, carta: Carta): ### Método para tirar una carta al próximo jugador ###
        self.__mano.remove(carta)
        jugador.setCartaTirada(carta)

    def getCartaTocar1(self):               ### Método para acceder a la primera carta con la que el jugador desea tocar ###
        return self.__cartaTocar1
    
    def getCartaTocar2(self):               ### Método para acceder a la segunda carta con la que el jugador desea tocar ###
        return self.__cartaTocar2
    
    def tocar(self, idx1: int, idx2: int = None):
        if idx2 != None:
            self.__mano.append(self.__mano.pop(idx1))
            self.__mano.append(self.__mano.pop(idx2))
        else:
            self.__mano.append(self.__mano.pop(idx1))
    
    def getMano(self):                      ### Método para acceder a la mano del jugador ###
        return self.__mano
    
    def setMano(self, mano: list()):
        self.__mano = mano

    def getPuntaje(self):
        return self.__puntos
    
    def setPuntaje(self, puntaje):
        self.__puntos = puntaje

    def sumPuntos(self, pts: int):          ### Método para añadir puntos al jugador ###
        self.__puntos += pts

    def isGanador(self):
        return self.__ganador

    def setGanador(self, val: bool):
        self.__ganador = val
    
    def setPerdedor(self, valor: bool):
        self.__perdedor = valor

    def getPerdedor(self):
        return self.__perdedor