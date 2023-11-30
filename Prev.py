from tkinter import *
from tkinter import ttk
from Main import Apuntado
from Src.Packages.Usuario import Usuario

class Previous:
    def __init__(self, user: Usuario):
        self.estiloCartas = "Classic"
        self.usuario = user

        with open("Src\Packages\Registros.txt") as Registro:
            reader = Registro.readlines()
        
        reader = [line.replace("\n", "") for line in reader]
        

        self.root = Tk()
        self.root.title(f"Apuntado")
        self.root.geometry("800x400")
        self.notebook = ttk.Notebook(self.root)


        self.frameJuego = Frame(self.notebook, bg="#007b00")
        solitario = PhotoImage("Solitario", file = "Src\img\Others\SinglePlayer.png")
        multijugador = PhotoImage("Multijugador", file = "Src\img\Others\MultiPlayer.png")



        self.frameSolitario = Frame(self.frameJuego, bg = "#007b00")        # Frame para poder jugar solitario

        SolitarioLbl = Label(self.frameSolitario, text = "SOLITARIO", font = ("Fixedsys",18,"bold"), bg = "#007b00", fg = "#005200")
        SolitarioLbl.pack(fill=X)

        solitarioImg = Label(self.frameSolitario, image = solitario, bg = "#007b00")
        solitarioImg.pack()
        
        SolitarioDescriptionLbl = Label(self.frameSolitario, text = "Modo de juego para jugar PvE", font = ("Times", 9), bg = "#007b00", fg = "#b4ff9a")
        SolitarioDescriptionLbl.pack(fill = X, pady = (10,5))

        SolitarioBtn = Button(self.frameSolitario, text = "Jugar en solitario", font = ("Fixedsys"), relief = GROOVE, bg = "#005c00", cursor = "hand2", activebackground = "#006600", command = self.jugarSolitario)
        SolitarioBtn.pack(fill=X, pady= 10)
        SolitarioBtn.bind("<Enter>", lambda event: self.onhover(SolitarioBtn))
        SolitarioBtn.bind("<Leave>", lambda event: self.outhover(SolitarioBtn))

        self.frameSolitario.pack(side = LEFT, padx=(150,0))



        self.frameMultijugador = Frame(self.frameJuego, bg = "#007b00")     # Frame para poder jugar multijugador

        MultijugadorLbl = Label(self.frameMultijugador, text = "MULTIJUGADOR", font = ("Fixedsys",18,"bold"), bg = "#007b00", fg = "#005200")
        MultijugadorLbl.pack(fill=X)

        multijugadorImg = Label(self.frameMultijugador, image = multijugador, bg = "#007b00")
        multijugadorImg.pack()

        MultijugadorDescriptionLbl = Label(self.frameMultijugador, text = "Modo de juego para jugar PvP\n con hasta 6 amigos", font = ("Times", 9), bg = "#007b00", fg = "#b4ff9a")
        MultijugadorDescriptionLbl.pack(fill = X)

        MultijugadorBtn = Button(self.frameMultijugador, text = "Jugar multijugador", font = ("Fixedsys"), relief = GROOVE, bg = "#005c00", cursor = "hand2", activebackground = "#006600", command = self.jugarMultijugador)
        MultijugadorBtn.pack(fill=X, pady= 10)
        MultijugadorBtn.bind("<Enter>", lambda event: self.onhover(MultijugadorBtn))
        MultijugadorBtn.bind("<Leave>", lambda event: self.outhover(MultijugadorBtn))

        self.frameMultijugador.pack(side = RIGHT, padx=(0,150))



        self.frameTienda = Frame(self.notebook, bg="#007b00")
        cartas = PhotoImage("Carta", file = "Src\img\Others\Cards.png")
        tokens = PhotoImage("Tokens", file = "Src\img\Others\Tokens.png")

        self.frameCartas = Frame(self.frameTienda, bg = "#007b00")        # Frame para poder cambiar estilo de cartas

        CartasLbl = Label(self.frameCartas, text = "Cartas", font = ("Fixedsys",18,"bold"), bg = "#007b00", fg = "#005200")
        CartasLbl.pack(fill=X)

        CartasImg = Label(self.frameCartas, image = cartas, bg = "#007b00")
        CartasImg.pack()
                                                              
        CartasDescriptionLbl = Label(self.frameCartas, text = "Aquí puedes cambiar el estilo\na tus cartas", font = ("Times", 9), bg = "#007b00", fg = "#b4ff9a")
        CartasDescriptionLbl.pack(fill = X, pady = (10,5))

        Cartas1Btn = Button(self.frameCartas, text = "Visualizar Estilos", font = ("Fixedsys"), relief = GROOVE, bg = "#005c00", cursor = "hand2", activebackground = "#006600", command = self.verEstilos)
        Cartas1Btn.pack(side = LEFT, pady= 10)
        Cartas1Btn.bind("<Enter>", lambda event: self.onhover(Cartas1Btn))
        Cartas1Btn.bind("<Leave>", lambda event: self.outhover(Cartas1Btn))

        Cartas2Btn = Button(self.frameCartas, text = "Cambiar", font = ("Fixedsys"), relief = GROOVE, bg = "#005c00", cursor = "hand2", activebackground = "#006600", command = self.cambiarEstilo)
        Cartas2Btn.pack(side = RIGHT, pady = 10)
        Cartas2Btn.bind("<Enter>", lambda event: self.onhover(Cartas2Btn))
        Cartas2Btn.bind("<Leave>", lambda event: self.outhover(Cartas2Btn))

        self.frameCartas.pack(side = LEFT, padx=(150,0))



        self.frameTokens = Frame(self.frameTienda, bg = "#007b00")     # Frame para poder comprar tokens

        TokensLbl = Label(self.frameTokens, text = "Tokens", font = ("Fixedsys",18,"bold"), bg = "#007b00", fg = "#005200")
        TokensLbl.pack(fill=X, pady = (0, 5))

        TokensImg = Label(self.frameTokens, image = tokens, bg = "#007b00")
        TokensImg.pack()

        TokensDescriptionLbl = Label(self.frameTokens, text = "Aquí puedes comprar tokens", font = ("Times", 9), bg = "#007b00", fg = "#b4ff9a")
        TokensDescriptionLbl.pack(fill = X, pady = (15, 10))

        TokensBtn = Button(self.frameTokens, text = "Comprar tokens", font = ("Fixedsys"), relief = GROOVE, bg = "#005c00", cursor = "hand2", activebackground = "#006600", command = self.comprarTokens)
        TokensBtn.pack(fill=X, pady= 10)
        TokensBtn.bind("<Enter>", lambda event: self.onhover(TokensBtn))
        TokensBtn.bind("<Leave>", lambda event: self.outhover(TokensBtn))

        self.frameTokens.pack(side = RIGHT, padx=(0,150))



        self.notebook.add(self.frameJuego, text="Juego")
        self.notebook.add(self.frameTienda, text="Tienda")
        self.notebook.pack(expand=True, fill=BOTH)
        self.root.mainloop()

    def jugarSolitario(self):
        pass
    
    def jugarMultijugador(self):
        Apuntado(self.estiloCartas)
        self.root.destroy()

    def verEstilos(self):
        pass

    def cambiarEstilo(self):
        pass

    def comprarTokens(self):
        def aceptar():
            self.usuario.sumTokens(int(spinbox.get()))
            root.destroy()
        root = Tk()
        root.title("Compra de tokens")

        cont1 = Frame(root)

        CTQ = Label(cont1, text = "Cuantos tokens quieres?")
        CTQ.pack(side = LEFT)
        
        spinbox = Spinbox(cont1, from_= 10, to=500, increment=10, width=5)
        spinbox.pack(side = RIGHT)

        cont1.pack(pady = (30,0))

        Aceptarbtn = Button(root, text = "Aceptar", command=aceptar)
        Aceptarbtn.pack(pady = 20)

        root.mainloop()


    def onhover(self, btn: Button):
        btn["bg"] = "#258d19"

    def outhover(self, btn: Button):
        btn["bg"] = "#005c00"


