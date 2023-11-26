from Src.Packages.Carta import Carta

class Baraja:
    def __init__(self):             ### Método para creación de una baraja ###
        self.__baraja = []
        Pintas = ["Clubs", "Diamonds","Hearts", "Spades"]
        for pinta in Pintas:
            for i in range(2,15):
                if i == 14:
                    self.__baraja.append(Carta(pinta, "A"))
                elif i == 13:
                    self.__baraja.append(Carta(pinta, "K"))
                elif i == 12:
                    self.__baraja.append(Carta(pinta,"Q"))
                elif i == 11:
                    self.__baraja.append(Carta(pinta, "J"))
                else:
                    self.__baraja.append(Carta(pinta, str(i)))
    
    def getBaraja(self):            ### Método para obtener la baraja ###
        return self.__baraja