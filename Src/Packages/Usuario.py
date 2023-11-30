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
    
    def getFechaNac(self):
        return f"{self.__fechaNacimiento.day}/{self.__fechaNacimiento.month}/{self.__fechaNacimiento.year}"
    
    def sumTokens(self, t: int):
        self.__tokens += t
        with open("Src\Packages\Registros.txt") as Registro:
            reader = Registro.readlines()
        reader = [line.replace("\n", "").split(",") for line in reader]
        for line in reader:
            if self.__nick == line[0]:
                line[4] = str(self.__tokens)
                break
        nueva = []
        for line in reader:
            nueva.append(",".join(line))
        towrite = "\n".join(nueva)
        with open("Src\Packages\Registros.txt", "w") as Registro:
            Registro.write(towrite)