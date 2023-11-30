from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Prev import Previous
from Src.Packages.Usuario import Usuario
from datetime import date
from Prev import Previous
import sys

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
            self.__registro.append(Usuario(nickname, nombre, fecha, contraseña, tokens))

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
        self.Registrarbtn.bind("<Enter>", lambda event: self.buttonhover(self.Registrarbtn))
        self.Registrarbtn.bind("<Leave>", lambda event: self.buttonhover_leave(self.Registrarbtn))

        self.root.mainloop()
    
    def iniciarSesion(self):
        Nick = self.Nicktxt.get()
        Pwd = self.Pwdtxt.get()
        exist = False
        for usuario in self.__registro:
            if usuario.getNick() == Nick:
                exist = True
                break
        if exist:
            if usuario.getContraseña() != Pwd:
                messagebox.showerror(message="Contraseña incorrecta", title="Error")
                self.Pwd.set("")
            else:
                self.root.destroy()
                Previous(usuario)
        else:
            messagebox.showerror(message="Usuario no registrado", title="Error")

    def registrar(self):
        def registro():
            nick = nickTxt.get()
            name = nombreTxt.get()
            fechaNac = fechaNacTxt.get()
            pwd = contraseñaTxt.get()
            try:
                if nick == "" or name == "" or fechaNac == "" or pwd == "":
                    messagebox.showerror("Error", "Complete todos los campos")
                    raise Exception("e")
                else:
                    for usuario in self.__registro:
                        if usuario.getNick() == nick:
                            messagebox.showerror("Error", "Usuario ya registrado")
                            raise Exception("e")
                    try:
                        fsplit = fechaNac.split("/")
                    except:
                        messagebox.showerror("Error", "Ingrese una fecha válida")
                        raise Exception("e")
                    try:
                        dd = int(fsplit[0])
                    except:
                        messagebox.showerror("Error", "Ingrese una fecha válida")
                        raise Exception("e")
                    try:
                        mm = int(fsplit[1])
                    except:
                        messagebox.showerror("Error", "Ingrese una fecha válida")
                        raise Exception("e")
                    try:
                        aa = int(fsplit[2])
                    except:
                        messagebox.showerror("Error", "Ingrese una fecha válida")
                        raise Exception("e")

                    fecha_nacimiento = date(aa,mm,dd)
                    fecha_actual = date.today()

                    if fecha_actual.month < fecha_nacimiento.month:
                        tt = 1
                    elif fecha_actual.month == fecha_nacimiento.month:
                        if fecha_actual.day < fecha_nacimiento.day:
                            tt = 1
                        else:
                            tt = 0
                    else:
                        tt = 0

                    edad = fecha_actual.year - fecha_nacimiento.year - tt
                    if edad < 18:
                        messagebox.showerror("Error", "No puedes registrarte, eres menor de edad")
                    else:
                        self.__registro.append(Usuario(nick,name,fecha_nacimiento,pwd))
                        nueva = []
                        for usuario in self.__registro:
                            nombre = usuario.getNombre()
                            nickname = usuario.getNick()
                            fecha = usuario.getFechaNac()
                            pw = usuario.getContraseña()
                            tokens = usuario.getTokens()
                            nueva.append(f"{nickname},{nombre},{fecha},{pw},{tokens}")
                        towrite = "\n".join(nueva)
                        with open("Src/Packages/Registros.txt", "w") as R:
                            R.write(towrite)
                        root.destroy()
            except:
                pass
        root = Tk()
        root.title("Registro")
        
        F1 = Frame(root)
        nickLbl = Label(F1, text = "Nickname", font=("Times",12))
        nickLbl.pack(side = LEFT, pady = (15,0), padx = (20,0))

        nombreLbl = Label(F1, text = "Nombre", font=("Times",12))
        nombreLbl.pack(side = RIGHT, pady = (15,0), padx = (0, 130))
        F1.pack(fill = X)

        F2 = Frame(root)
        nickTxt = Entry(F2, font=("Times", 12))
        nickTxt.pack(side=LEFT, pady = 10, padx = (20,10))

        nombreTxt = Entry(F2, font=("Times", 12))
        nombreTxt.pack(side = RIGHT, pady = 10, padx = (10,20))

        F2.pack(fill = X)

        F3 = Frame(root)
        fechaNacLbl = Label(F3, text = "Fecha de nacimiento\n(dd/mm/aa)", font=("Times",12), justify = LEFT)
        fechaNacLbl.pack(side = LEFT, padx = (0,55))

        contraseñaLbl = Label(F3, text = "Contraseña", font=("Times",12))
        contraseñaLbl.pack(side = RIGHT, pady = (30,0), padx = (0, 95))
        F3.pack()

        F4 = Frame(root)
        fechaNacTxt = Entry(F4, font=("Times", 12))
        fechaNacTxt.pack(side = LEFT, pady = 5, padx = (20,10))

        contraseñaTxt = Entry(F4, font=("Times", 12))
        contraseñaTxt.pack(side = RIGHT, pady = 5, padx = (10,20))
        F4.pack()
        
        registrarseBtn = Button(root, text = "Registrarse", command= lambda: registro())
        registrarseBtn.pack(padx=(280,0), pady= (10,20))

        root.mainloop()
        
    def buttonhover(self, btn: Button):
        btn["bg"] = "#0F5A90"

    def buttonhover_leave(self, btn: Button):
        btn["bg"] = "#52a5e0"


Login()