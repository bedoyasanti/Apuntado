class Carta:
    def __init__(self, pinta, denominacion):    ### Método de creación de cada carta ###
        self.__pinta = pinta
        self.__denominacion = denominacion

        if denominacion == "A":
            self.__den2 = 14
        elif denominacion == "K":
            self.__den2 = 13
        elif denominacion == "Q":
            self.__den2 = 12
        elif denominacion == "J":
            self.__den2 = 11
        else:
            self.__den2 = int(denominacion)

        if denominacion in ("J","Q","K","A"):
            self.__valor = 10
        else:
            self.__valor = int(denominacion)

        self.__src = f"Apuntado/InGame/Src/img/Classic/{self.__pinta}/{self.__pinta}{self.__denominacion}.png"
    
    def cambiarEstilo(self, diseño):            ### Método para cambiar el estilo de la carta en caso de que el jugador tenga uno diferente ###
        self.__src = f"Apuntado/InGame/Src/img/{diseño}/{self.__pinta}/{self.__pinta}{self.__denominacion}.png"

    def getPinta(self):
        return self.__pinta
    
    def getDenominacion(self):
        return self.__denominacion # cambiar
                                                ### Métodos para acceder a las propiedades de la carta ###
    def getValor(self):
        return self.__valor
    
    def getSource(self):
        return self.__src
    
    def getDenominacion2(self):
        return self.__den2
    
    def getden2(self):
        return self.__den2