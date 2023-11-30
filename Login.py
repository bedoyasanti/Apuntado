from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Prev import Previous
from Src.Packages.Usuario import Usuario
from datetime import date

class Login:
    def __init__(self):
        self.__registro = []
        with open("Src\Packages\Registros.txt") as R:
            reader = R.readlines()
        r = [line.replace("\n", "") for line in reader]
        for line in r:
            u = line.split(",")
            nickname = u[0]
            nombre = u[1]
            f = u[2].split("/")
            fecha = date(int(f[2]), int(f[1]), int(f[0]))
            contraseña = u[3]
            tokens = int(u[4])
            self.__registro.append([Usuario(nickname, nombre, fecha, contraseña, tokens)])

        self.root = Tk()
        self.root.title("Login")
        self.root.geometry("400x500")
        self.root.resizable(width=0, height=0)

        # Frame para mostrar "Inicio de sesión"
        self.mainFrame_top = Frame(self.root, height=50, bd=0, relief=SOLID)
        self.mainFrame_top.pack(side="top",fill=X)

        # Frame para usuario y contraseña
        self.mainFrame = Frame(self.root, bd=0, relief=SOLID, bg ="#f1f1f1")
        self.mainFrame.pack(expand=YES, fill=BOTH)
        
        # Titulo del programa
        self.titulo = Label(self.mainFrame_top, text="Inicio de sesión", font=("Times",30), fg="#616583", bg="#f1f1f1", pady=50)
        self.titulo.pack(expand=YES,fill=BOTH)

        # Label y textbox para ingresar el Id
        Nicklbl = Label(self.mainFrame, text = "Nickname", font=("Times",14), fg="#616583", bg="#f1f1f1", anchor="w")
        Nicklbl.pack(fill=X, padx=20, pady=5)

        self.Nick = StringVar()
        self.Nicktxt = ttk.Entry(self.mainFrame,font=("Times", 14), textvariable=self.Nick)
        self.Nicktxt.pack(fill=X, padx=20, pady=10)

        # Label y textbox para ingresar la contraseña
        Pwdlbl = Label(self.mainFrame, text = "Contraseña", font=("Times",14), fg="#616583", bg="#f1f1f1", anchor="w")
        Pwdlbl.pack(fill=X, padx=20,pady=5)

        self.Pwd = StringVar()
        self.Pwdtxt = ttk.Entry(self.mainFrame,font=("Times", 14), textvariable=self.Pwd)
        self.Pwdtxt.pack(fill=X, padx=20, pady=10)
        self.Pwdtxt.config(show="·")

        # Boton para iniciar sesion
        self.Iniciarbtn = Button(self.mainFrame, text="Iniciar sesión", font=("Times", 15, "bold"), bg="#52a5e0", bd=0, fg="#fff", command=self.iniciarSesion)
        self.Iniciarbtn.pack(fill=X, padx=20, pady=20)
        self.Iniciarbtn.bind("<Enter>", lambda event: self.buttonhover(self.Iniciarbtn))
        self.Iniciarbtn.bind("<Leave>", lambda event: self.buttonhover_leave(self.Iniciarbtn))

        self.Registrarbtn = Button(self.mainFrame, text="Registrar", font=("Times", 15, "bold"), bg="#52a5e0", bd=0, fg="#fff", command=self.registrar)
        self.Registrarbtn.pack(fill=X, padx=20, pady=20)
        self.Registrarbtn.bind("<Enter>", lambda event: self.buttonhover(self.Iniciarbtn))
        self.Registrarbtn.bind("<Leave>", lambda event: self.buttonhover_leave(self.Iniciarbtn))

        self.root.mainloop()
    
    def iniciarSesion(self):
        # Verificación de credenciales de usuario
        Nick = self.Nicktxt.get()
        Pwd = self.Pwdtxt.get()
        try:
            for usuario in self.__registro:
                pass
        except:
            self.Id.set("")
            self.Pwd.set("")
            messagebox.showerror(message="Porfavor introduzca usuario y contraseña válidos", title="Error")

    def registrar(self):
        pass
        
    def buttonhover(self, btn: Button):
        btn["bg"] = "#0F5A90"

    def buttonhover_leave(self, btn: Button):
        btn["bg"] = "#52a5e0"


Login()