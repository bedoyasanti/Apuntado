from datetime import datetime, date

class Usuario:
    def __init__(self, nickname: str, nombre: str, fechaNacimiento: date, contraseña: str, tokens: int = 0):
        self.__nombre = nombre
        self.__nick = nickname
        self.__contraseña = contraseña
        self.__fechaNacimiento = fechaNacimiento
        self.__tokens = tokens

    def getNombre(self):
        return self.__nombre
    
    def getNick(self):
        return self.__nick
    
    def getContraseña(self):
        return self.__contraseña
    
    def getTokens(self):
        return self.__tokens 
    