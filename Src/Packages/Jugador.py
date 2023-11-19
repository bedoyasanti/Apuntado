from Carta import Carta
class Jugador:                              # PD: Luego hay que crear la clase usuario y jugador heredará de usuario
    def __init__(self):                     ### Método para inicializar un jugador ###
        self.__mano = []
        self.__cartaTirada = None
        self.__cartaPorTirar = None
        self.__cartaTocar1 = None
        self.__cartaTocar2 = None
        self.__puntos = 0

    def añadirCarta(self, carta: Carta):    ### Método para añadir una carta a la mano ###
        self.__mano.append(carta)
    
    def modificarMano(self, idx1, idx2):    ### Método que se invocará cada que el jugador modifique las posiciones de su mano ###
        self.__mano[idx1], self.__mano[idx2] = self.__mano[idx2], self.__mano[idx1]
    
    def getCartaTirada(self):               ### Método para acceder a la carta que el jugador anterior le tiró ###
        return self.__cartaTirada
    
    def setCartaTirada(self, carta: Carta): ### Método para establecer la carta que el jugador anterior le tiró, útil para el método tirar() ###
        self.__cartaTirada = carta

    def tirar(self, jugador, carta: Carta): ### Método para tirar una carta al próximo jugador ###
        jugador.setCartaTirada(carta)

    def getCartaTocar1(self):               ### Método para acceder a la primera carta con la que el jugador desea tocar ###
        return self.__cartaTocar1
    
    def getCartaTocar2(self):               ### Método para acceder a la segunda carta con la que el jugador desea tocar ###
        return self.__cartaTocar2
    

    def getMano(self):                      ### Método para acceder a la mano del jugador ###
        return self.__mano
    