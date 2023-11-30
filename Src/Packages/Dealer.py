from Src.Packages.ReglasJuego import Reglas
from random import choice
from Src.Packages.Jugador import Jugador
from Src.Packages.Carta import Carta
from Src.Packages.Baraja import Baraja

class Dealer:
    def __init__(self):
        pass

    def repartirCartas(self, turnos, mazo, baraja : Baraja):                             ### Método para repartir cartas a los jugadores ###
        #baraja = Baraja()
        for i in range(len(turnos)):
            jugador : Jugador = turnos[i]# Se itera sobre los turnos de jugadores, dada la prioridad
            while True:
                if len(jugador.getMano()) == 10:# Si el jugador ya tiene 10 cartas en su mano, se le añade otra si es el ganador
                    if jugador.isGanador():
                        while True:
                            carta11 = choice(baraja.getBaraja())
                            if mazo[carta11] > 0:
                                jugador.añadirCarta(carta11)
                                mazo[carta11] -= 1
                                break
                    break
                carta = choice(baraja.getBaraja())   # Se escoge una carta al azar de una baraja
                if mazo[carta] > 0:                  # Si la carta está disponible en el mazo, es decir si aún hay al menos una carta (en el mazo) de la escogida en una baraja
                    jugador.añadirCarta(carta)              # Se le añade la carta al jugador
                    mazo[carta] -= 1
    
    def comprobarManos(self, ganador: Jugador, otros, tocar = 0):       ### Método que comprueba las manos del ganador, y los otros jugadores de la partida ###
        MG = ganador.getMano()
        ManoG = MG.copy()
        if tocar == 1:
            ganador.sumPuntos(ManoG[9].getValor())
        elif tocar == 2:
            ganador.sumPuntos((ManoG[8].getValor() + ManoG[9].getValor()))
        elif Reglas.pinta(ManoG):
            ganador.sumPuntos(-25)
        else:
            ganador.sumPuntos(-10)

        for i in range(len(otros)):
            jugador: Jugador = otros[i]
            M = jugador.getMano()
            Mano = M.copy()
            pts = 0
            if Reglas.septima_1_7(Mano):
                Mano[0], Mano[1], Mano[2], Mano[3], Mano[4], Mano[5], Mano[6] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.septima_4_10(Mano):
                Mano[3], Mano[4], Mano[5], Mano[6], Mano[7], Mano[8], Mano[9] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            
            if Reglas.sexta_1_6(Mano):
                Mano[0], Mano[1], Mano[2], Mano[3], Mano[4], Mano[5] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.sexta_4_9(Mano):
                Mano[3], Mano[4], Mano[5], Mano[6], Mano[7], Mano[8] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.sexta_5_10(Mano):
                Mano[4], Mano[5], Mano[6], Mano[7], Mano[8], Mano[9] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            
            if Reglas.quinta_1_5(Mano):
                Mano[0], Mano[1], Mano[2], Mano[3], Mano[4] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.quinta_4_8(Mano):
                Mano[3], Mano[4], Mano[5], Mano[6], Mano[7] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.quinta_5_9(Mano):
                Mano[4], Mano[5], Mano[6], Mano[7], Mano[8] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.quinta_6_10(Mano):
                Mano[5], Mano[6], Mano[7], Mano[8], Mano[9] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            
            if Reglas.cuarta_1_4(Mano):
                Mano[0], Mano[1], Mano[2], Mano[3] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.cuarta_4_7(Mano):
                Mano[3], Mano[4], Mano[5], Mano[6] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.cuarta_5_8(Mano):
                Mano[4], Mano[5], Mano[6], Mano[7] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.cuarta_6_9(Mano):
                Mano[5], Mano[6], Mano[7], Mano[8] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.cuarta_7_10(Mano):
                Mano[6], Mano[7], Mano[8], Mano[9] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            
            if Reglas.terna_1_3(Mano):
                Mano[0], Mano[1], Mano[2] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.terna_4_6(Mano):
                Mano[3], Mano[4], Mano[5] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.terna_5_7(Mano):
                Mano[4], Mano[5], Mano[6] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.terna_6_8(Mano):
                Mano[5], Mano[6], Mano[7] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.terna_7_9(Mano):
                Mano[6], Mano[7], Mano[8] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.terna_8_10(Mano):
                Mano[7], Mano[8], Mano[9] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            
            for carta in Mano:
                if carta.getPinta() != "Replaced":
                    pts += carta.getValor()
            jugador.sumPuntos(pts)

    def validarBajarse(self, jugador: Jugador):         ### Método para validar si un jugador se puede bajar ###
        M = jugador.getMano()
        Mano = M.copy()
        if Reglas.septima_1_7(Mano):
            Mano[0], Mano[1], Mano[2], Mano[3], Mano[4], Mano[5], Mano[6] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
        if Reglas.septima_4_10(Mano):
            Mano[3], Mano[4], Mano[5], Mano[6], Mano[7], Mano[8], Mano[9] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
        
        if Reglas.sexta_1_6(Mano):
            Mano[0], Mano[1], Mano[2], Mano[3], Mano[4], Mano[5] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
        if Reglas.sexta_4_9(Mano):
            Mano[3], Mano[4], Mano[5], Mano[6], Mano[7], Mano[8] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
        if Reglas.sexta_5_10(Mano):
            Mano[4], Mano[5], Mano[6], Mano[7], Mano[8], Mano[9] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
        
        if Reglas.quinta_1_5(Mano):
            Mano[0], Mano[1], Mano[2], Mano[3], Mano[4] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
        if Reglas.quinta_4_8(Mano):
            Mano[3], Mano[4], Mano[5], Mano[6], Mano[7] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
        if Reglas.quinta_5_9(Mano):
            Mano[4], Mano[5], Mano[6], Mano[7], Mano[8] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
        if Reglas.quinta_6_10(Mano):
            Mano[5], Mano[6], Mano[7], Mano[8], Mano[9] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
        
        if Reglas.cuarta_1_4(Mano):
            Mano[0], Mano[1], Mano[2], Mano[3] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
        if Reglas.cuarta_4_7(Mano):
            Mano[3], Mano[4], Mano[5], Mano[6] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
        if Reglas.cuarta_5_8(Mano):
            Mano[4], Mano[5], Mano[6], Mano[7] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
        if Reglas.cuarta_6_9(Mano):
            Mano[5], Mano[6], Mano[7], Mano[8] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
        if Reglas.cuarta_7_10(Mano):
            Mano[6], Mano[7], Mano[8], Mano[9] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
        
        if Reglas.terna_1_3(Mano):
            Mano[0], Mano[1], Mano[2] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
        if Reglas.terna_4_6(Mano):
            Mano[3], Mano[4], Mano[5] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
        if Reglas.terna_5_7(Mano):
            Mano[4], Mano[5], Mano[6] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
        if Reglas.terna_6_8(Mano):
            Mano[5], Mano[6], Mano[7] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
        if Reglas.terna_7_9(Mano):
            Mano[6], Mano[7], Mano[8] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
        if Reglas.terna_8_10(Mano):
            Mano[7], Mano[8], Mano[9] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
        
        if any(carta.getPinta() != "Replaced" for carta in Mano):
            return False
        else:
            return True
        
    def validarTocar(self, jugador: Jugador, carta1: Carta, carta2:Carta = None):
        if (carta2 != None) and ((carta1.getValor() + carta2.getValor()) > 5):
            return False
        elif (carta2 == None) and (carta1.getValor() > 5):
            return False
        else:
            M = jugador.getMano()
            Mano = M.copy()
            if carta2 != None:
                pts = carta1.getValor() + carta2.getValor()
                Mano[Mano.index(carta1)] = Carta("Replaced", "20")
                Mano[Mano.index(carta2)] = Carta("Replaced", "20")
            else:
                pts = carta1.getValor()
                Mano[Mano.index(carta1)] = Carta("Replaced", "20")
        if carta2 == None:
            if Reglas.septima_1_7(Mano):
                Mano[0], Mano[1], Mano[2], Mano[3], Mano[4], Mano[5], Mano[6] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            
            if Reglas.sexta_1_6(Mano):
                Mano[0], Mano[1], Mano[2], Mano[3], Mano[4], Mano[5] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.sexta_4_9(Mano):
                Mano[3], Mano[4], Mano[5], Mano[6], Mano[7], Mano[8] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            
            if Reglas.quinta_1_5(Mano):
                Mano[0], Mano[1], Mano[2], Mano[3], Mano[4] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.quinta_4_8(Mano):
                Mano[3], Mano[4], Mano[5], Mano[6], Mano[7] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.quinta_5_9(Mano):
                Mano[4], Mano[5], Mano[6], Mano[7], Mano[8] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            
            if Reglas.cuarta_1_4(Mano):
                Mano[0], Mano[1], Mano[2], Mano[3] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.cuarta_4_7(Mano):
                Mano[3], Mano[4], Mano[5], Mano[6] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.cuarta_5_8(Mano):
                Mano[4], Mano[5], Mano[6], Mano[7] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.cuarta_6_9(Mano):
                Mano[5], Mano[6], Mano[7], Mano[8] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            
            if Reglas.terna_1_3(Mano):
                Mano[0], Mano[1], Mano[2] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.terna_4_6(Mano):
                Mano[3], Mano[4], Mano[5] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.terna_5_7(Mano):
                Mano[4], Mano[5], Mano[6] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.terna_6_8(Mano):
                Mano[5], Mano[6], Mano[7] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.terna_7_9(Mano):
                Mano[6], Mano[7], Mano[8] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
        else:
            if Reglas.septima_1_7(Mano):
                Mano[0], Mano[1], Mano[2], Mano[3], Mano[4], Mano[5], Mano[6] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            
            if Reglas.sexta_1_6(Mano):
                Mano[0], Mano[1], Mano[2], Mano[3], Mano[4], Mano[5] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            
            if Reglas.quinta_1_5(Mano):
                Mano[0], Mano[1], Mano[2], Mano[3], Mano[4] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.quinta_4_8(Mano):
                Mano[3], Mano[4], Mano[5], Mano[6], Mano[7] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            
            if Reglas.cuarta_1_4(Mano):
                Mano[0], Mano[1], Mano[2], Mano[3] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.cuarta_4_7(Mano):
                Mano[3], Mano[4], Mano[5], Mano[6] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.cuarta_5_8(Mano):
                Mano[4], Mano[5], Mano[6], Mano[7] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            
            if Reglas.terna_1_3(Mano):
                Mano[0], Mano[1], Mano[2] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.terna_4_6(Mano):
                Mano[3], Mano[4], Mano[5] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.terna_5_7(Mano):
                Mano[4], Mano[5], Mano[6] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            if Reglas.terna_6_8(Mano):
                Mano[5], Mano[6], Mano[7] = Carta("Replaced", "20"), Carta("Replaced", "20"), Carta("Replaced", "20")
            
        if any(carta.getPinta() != "Replaced" for carta in Mano):
            return False
        else:
            return True