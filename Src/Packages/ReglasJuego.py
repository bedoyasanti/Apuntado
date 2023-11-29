class Reglas:
    def pinta(Mano):           ### Método que comprueba si toda la mano es de una misma pinta ###
        if all(carta.getPinta() == "Clubs" for carta in Mano) or all(carta.getPinta() == "Diamonds" for carta in Mano) or all(carta.getPinta() == "Hearts" for carta in Mano) or all(carta.getPinta() == "Spades" for carta in Mano):
            return True
        return False
    



    ############################

    def novena(Mano):          ### Método que comprueba si 9 de las cartas son de la misma pinta ###
        if Mano[0].getPinta() == Mano[1].getPinta() == Mano[2].getPinta() == Mano[3].getPinta() == Mano[4].getPinta() == Mano[5].getPinta() == Mano[6].getPinta() == Mano[7].getPinta() == Mano[8].getPinta():
            return True
        return False
    
    def octava(Mano):          ### Método que comprueba si 8 de las cartas son de la misma pinta ###
        if Mano[0].getPinta() == Mano[1].getPinta() == Mano[2].getPinta() == Mano[3].getPinta() == Mano[4].getPinta() == Mano[5].getPinta() == Mano[6].getPinta() == Mano[7].getPinta():
            return True
        return False
    
    ############################

    # Preguntar por este fragmento a Alejandra



    def septima_1_7(Mano):        ### Método que comprueba si las cartas de la 1 a la 7 son una séptima ###
        if (Mano[0].getDenominacion2() == (Mano[1].getDenominacion2() - 1) == (Mano[2].getDenominacion2() - 2) == (Mano[3].getDenominacion2() - 3) == (Mano[4].getDenominacion2() - 4) == (Mano[5].getDenominacion2() - 5) == (Mano[6].getDenominacion2() - 6)) and (Mano[0].getPinta() == (Mano[1].getPinta()) == (Mano[2].getPinta()) == (Mano[3].getPinta()) == (Mano[4].getPinta()) == (Mano[5].getPinta()) == (Mano[6].getPinta())):
            return True
        elif Mano[0].getDenominacion() == Mano[1].getDenominacion() == Mano[2].getDenominacion() == Mano[3].getDenominacion() == Mano[4].getDenominacion() == Mano[5].getDenominacion() == Mano[6].getDenominacion():
            return True
        return False
    
    def septima_4_10(Mano):        ### Método que comprueba si las cartas de la 4 a la 10 son una séptima ###
        if (Mano[3].getDenominacion2() == (Mano[4].getDenominacion2() - 1) == (Mano[5].getDenominacion2() - 2) == (Mano[6].getDenominacion2() - 3) == (Mano[7].getDenominacion2() - 4) == (Mano[8].getDenominacion2() - 5) == (Mano[9].getDenominacion2() - 6)) and (Mano[3].getPinta() == (Mano[4].getPinta()) == (Mano[5].getPinta()) == (Mano[6].getPinta()) == (Mano[7].getPinta()) == (Mano[8].getPinta()) == (Mano[9].getPinta())):
            return True
        elif Mano[3].getDenominacion() == Mano[4].getDenominacion() == Mano[5].getDenominacion() == Mano[6].getDenominacion() == Mano[7].getDenominacion() == Mano[8].getDenominacion() == Mano[9].getDenominacion():
            return True
        return False
    




    def sexta_1_6(Mano):        ### Método que comprueba si las cartas de la 1 a la 6 son una sexta ###
        if (Mano[0].getDenominacion2() == (Mano[1].getDenominacion2() - 1) == (Mano[2].getDenominacion2() - 2) == (Mano[3].getDenominacion2() - 3) == (Mano[4].getDenominacion2() - 4) == (Mano[5].getDenominacion2() - 5)) and (Mano[0].getPinta() == (Mano[1].getPinta()) == (Mano[2].getPinta()) == (Mano[3].getPinta()) == (Mano[4].getPinta()) == (Mano[5].getPinta())):
            return True
        elif Mano[0].getDenominacion() == Mano[1].getDenominacion() == Mano[2].getDenominacion() == Mano[3].getDenominacion() == Mano[4].getDenominacion() == Mano[5].getDenominacion():
            return True
        return False
    
    def sexta_4_9(Mano):        ### Método que comprueba si las cartas de la 4 a la 9 son una sexta ###
        if (Mano[3].getDenominacion2() == (Mano[4].getDenominacion2() - 1) == (Mano[5].getDenominacion2() - 2) == (Mano[6].getDenominacion2() - 3) == (Mano[7].getDenominacion2() - 4) == (Mano[8].getDenominacion2() - 5)) and (Mano[3].getPinta() == (Mano[4].getPinta()) == (Mano[5].getPinta()) == (Mano[6].getPinta()) == (Mano[7].getPinta()) == (Mano[8].getPinta())):
            return True
        elif Mano[3].getDenominacion() == Mano[4].getDenominacion() == Mano[5].getDenominacion() == Mano[6].getDenominacion() == Mano[7].getDenominacion() == Mano[8].getDenominacion():
            return True
        return False
    
    def sexta_5_10(Mano):        ### Método que comprueba si las cartas de la 5 a la 10 son una sexta ###
        if (Mano[4].getDenominacion2() == (Mano[5].getDenominacion2() - 1) == (Mano[6].getDenominacion2() - 2) == (Mano[7].getDenominacion2() - 3) == (Mano[8].getDenominacion2() - 4) == (Mano[9].getDenominacion2() - 5)) and (Mano[4].getPinta() == (Mano[5].getPinta()) == (Mano[6].getPinta()) == (Mano[7].getPinta()) == (Mano[8].getPinta()) == (Mano[9].getPinta())):
            return True
        elif Mano[4].getDenominacion() == Mano[5].getDenominacion() == Mano[6].getDenominacion() == Mano[7].getDenominacion() == Mano[8].getDenominacion() == Mano[9].getDenominacion():
            return True
        return False
    


    

    def quinta_1_5(Mano):        ### Método que comprueba si las cartas de la 1 a la 5 son una quinta ###
        if (Mano[0].getDenominacion2() == (Mano[1].getDenominacion2() - 1) == (Mano[2].getDenominacion2() - 2) == (Mano[3].getDenominacion2() - 3) == (Mano[4].getDenominacion2() - 4)) and (Mano[0].getPinta() == (Mano[1].getPinta()) == (Mano[2].getPinta()) == (Mano[3].getPinta()) == (Mano[4].getPinta())):
            return True
        elif Mano[0].getDenominacion() == Mano[1].getDenominacion() == Mano[2].getDenominacion() == Mano[3].getDenominacion() == Mano[4].getDenominacion():
            return True
        return False
    
    def quinta_4_8(Mano):        ### Método que comprueba si las cartas de la 4 a la 8 son una quinta ###
        if (Mano[3].getDenominacion2() == (Mano[4].getDenominacion2() - 1) == (Mano[5].getDenominacion2() - 2) == (Mano[6].getDenominacion2() - 3) == (Mano[7].getDenominacion2() - 4)) and (Mano[3].getPinta() == (Mano[4].getPinta()) == (Mano[5].getPinta()) == (Mano[6].getPinta()) == (Mano[7].getPinta())):
            return True
        elif Mano[3].getDenominacion() == Mano[4].getDenominacion() == Mano[5].getDenominacion() == Mano[6].getDenominacion() == Mano[7].getDenominacion():
            return True
        return False
    
    def quinta_5_9(Mano):        ### Método que comprueba si las cartas de la 5 a la 9 son una quinta ###
        if (Mano[4].getDenominacion2() == (Mano[5].getDenominacion2() - 1) == (Mano[6].getDenominacion2() - 2) == (Mano[7].getDenominacion2() - 3) == (Mano[8].getDenominacion2() - 4)) and (Mano[4].getPinta() == (Mano[5].getPinta()) == (Mano[6].getPinta()) == (Mano[7].getPinta()) == (Mano[8].getPinta())):
            return True
        elif Mano[4].getDenominacion() == Mano[5].getDenominacion() == Mano[6].getDenominacion() == Mano[7].getDenominacion() == Mano[8].getDenominacion():
            return True
        return False
    
    def quinta_6_10(Mano):        ### Método que comprueba si las cartas de la 6 a la 10 son una quinta ###
        if (Mano[5].getDenominacion2() == (Mano[6].getDenominacion2() - 1) == (Mano[7].getDenominacion2() - 2) == (Mano[8].getDenominacion2() - 3) == (Mano[9].getDenominacion2() - 4)) and (Mano[5].getPinta() == (Mano[6].getPinta()) == (Mano[7].getPinta()) == (Mano[8].getPinta()) == (Mano[9].getPinta())):
            return True
        elif Mano[5].getDenominacion() == Mano[6].getDenominacion() == Mano[7].getDenominacion() == Mano[8].getDenominacion() == Mano[9].getDenominacion():
            return True
        return False
    
    



    def cuarta_1_4(Mano):        ### Método que comprueba si las cartas de la 1 a la 4 son una cuarta ###
        if (Mano[0].getDenominacion2() == (Mano[1].getDenominacion2() - 1) == (Mano[2].getDenominacion2() - 2) == (Mano[3].getDenominacion2() - 3)) and (Mano[0].getPinta() == (Mano[1].getPinta()) == (Mano[2].getPinta()) == (Mano[3].getPinta())):
            return True
        elif Mano[0].getDenominacion() == Mano[1].getDenominacion() == Mano[2].getDenominacion() == Mano[3].getDenominacion():
            return True
        return False
    
    def cuarta_4_7(Mano):        ### Método que comprueba si las cartas de la 4 a la 7 son una cuarta ###
        if (Mano[3].getDenominacion2() == (Mano[4].getDenominacion2() - 1) == (Mano[5].getDenominacion2() - 2) == (Mano[6].getDenominacion2() - 3)) and (Mano[3].getPinta() == (Mano[4].getPinta()) == (Mano[5].getPinta()) == (Mano[6].getPinta())):
            return True
        elif Mano[3].getDenominacion() == Mano[4].getDenominacion() == Mano[5].getDenominacion() == Mano[6].getDenominacion():
            return True
        return False
    
    def cuarta_5_8(Mano):        ### Método que comprueba si las cartas de la 5 a la 8 son una cuarta ###
        if (Mano[4].getDenominacion2() == (Mano[5].getDenominacion2() - 1) == (Mano[6].getDenominacion2() - 2) == (Mano[7].getDenominacion2() - 3)) and (Mano[4].getPinta() == (Mano[5].getPinta()) == (Mano[6].getPinta()) == (Mano[7].getPinta())):
            return True
        elif Mano[4].getDenominacion() == Mano[5].getDenominacion() == Mano[6].getDenominacion() == Mano[7].getDenominacion():
            return True
        return False
    
    def cuarta_6_9(Mano):        ### Método que comprueba si las cartas de la 6 a la 9 son una cuarta ###
        if (Mano[5].getDenominacion2() == (Mano[6].getDenominacion2() - 1) == (Mano[7].getDenominacion2() - 2) == (Mano[8].getDenominacion2() - 3)) and (Mano[5].getPinta() == (Mano[6].getPinta()) == (Mano[7].getPinta()) == (Mano[8].getPinta())):
            return True
        elif Mano[5].getDenominacion() == Mano[6].getDenominacion() == Mano[7].getDenominacion() == Mano[8].getDenominacion():
            return True
        return False
    
    def cuarta_7_10(Mano):        ### Método que comprueba si las cartas de la 7 a la 10 son una cuarta ###
        if (Mano[6].getDenominacion2() == (Mano[7].getDenominacion2() - 1) == (Mano[8].getDenominacion2() - 2) == (Mano[9].getDenominacion2() - 3)) and (Mano[6].getPinta() == (Mano[7].getPinta()) == (Mano[8].getPinta()) == (Mano[9].getPinta())):
            return True
        elif Mano[6].getDenominacion() == Mano[7].getDenominacion() == Mano[8].getDenominacion() == Mano[9].getDenominacion():
            return True
        return False
    




    def terna_1_3(Mano):        ### Método que comprueba si las cartas de la 1 a la 3 son una terna ###
        if (Mano[0].getDenominacion2() == (Mano[1].getDenominacion2() - 1) == (Mano[2].getDenominacion2() - 2)) and (Mano[0].getPinta() == (Mano[1].getPinta()) == (Mano[2].getPinta())):
            return True
        elif Mano[0].getDenominacion() == Mano[1].getDenominacion() == Mano[2].getDenominacion():
            return True
        return False
    
    def terna_4_6(Mano):        ### Método que comprueba si las cartas de la 4 a la 6 son una terna ###
        if (Mano[3].getDenominacion2() == (Mano[4].getDenominacion2() - 1) == (Mano[5].getDenominacion2() - 2)) and (Mano[3].getPinta() == (Mano[4].getPinta()) == (Mano[5].getPinta())):
            return True
        elif Mano[3].getDenominacion() == Mano[4].getDenominacion() == Mano[5].getDenominacion():
            return True
        return False
    
    def terna_5_7(Mano):        ### Método que comprueba si las cartas de la 5 a la 7 son una terna ###
        if (Mano[4].getDenominacion2() == (Mano[5].getDenominacion2() - 1) == (Mano[6].getDenominacion2() - 2)) and (Mano[4].getPinta() == (Mano[5].getPinta()) == (Mano[6].getPinta())):
            return True
        elif Mano[4].getDenominacion() == Mano[5].getDenominacion() == Mano[6].getDenominacion():
            return True
        return False
    
    def terna_6_8(Mano):        ### Método que comprueba si las cartas de la 6 a la 8 son una terna ###
        if (Mano[5].getDenominacion2() == (Mano[6].getDenominacion2() - 1) == (Mano[7].getDenominacion2() - 2)) and (Mano[5].getPinta() == (Mano[6].getPinta()) == (Mano[7].getPinta())):
            return True
        elif Mano[5].getDenominacion() == Mano[6].getDenominacion() == Mano[7].getDenominacion():
            return True
        return False
    
    def terna_7_9(Mano):        ### Método que comprueba si las cartas de la 7 a la 9 son una terna ###
        if (Mano[6].getDenominacion2() == (Mano[7].getDenominacion2() - 1) == (Mano[8].getDenominacion2() - 2)) and (Mano[6].getPinta() == (Mano[7].getPinta()) == (Mano[8].getPinta())):
            return True
        elif Mano[6].getDenominacion() == Mano[7].getDenominacion() == Mano[8].getDenominacion():
            return True
        return False
    
    def terna_8_10(Mano):        ### Método que comprueba si las cartas de la 8 a la 10 son una terna ###
        if (Mano[7].getDenominacion2() == (Mano[8].getDenominacion2() - 1) == (Mano[9].getDenominacion2() - 2)) and (Mano[7].getPinta() == (Mano[8].getPinta()) == (Mano[9].getPinta())):
            return True
        elif Mano[7].getDenominacion() == Mano[8].getDenominacion() == Mano[9].getDenominacion():
            return True
        return False