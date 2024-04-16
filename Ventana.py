from tkinter import *
from tkinter import ttk


class MainFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=1280, height=720)
        self.master = master
        self.place(x=0, y=0)
        self.config(bg="Yellow green")
        self.create_widgets()

    def Select(self):
        self.frame3.place(x=0, rely=0.5, relwidth=0.3, relheight=0.15)
        self.label7.place(relx=0.068, rely=0.53)
        self.piso.place(relx=0.095, rely=0.6)
        self.label8.place(relx=0.017, rely=0.66)
        self.label9.place(relx= 0.17, rely=0.66)
        self.placa.place(relx=0.026, rely=0.75)
        self.hora.place(relx=0.19, rely=0.75)
        self.label1.destroy()
        self.label2.destroy()
        self.label3.destroy()
        self.label4.destroy()

    def Inicio(self):
        self.inicio.destroy()
        self.frame1.place(x=0, y=0, relwidth=0.3, height=self.master.winfo_height())
        self.frame2.place(x=0, y=0, width=self.master.winfo_width(), relheight=0.15)
        self.frame4.place(relx=0.3, y=0 , width=self.master.winfo_width(), height= self.master.winfo_height())

        # RadioButtons
        self.opcion = StringVar()
        self.opcion.set(None)
        Radiobutton(self.frame1, text="Moto", variable=self.opcion, value="moto", command=self.Select).place(x=5, rely=0.3)
        Radiobutton(self.frame1, text="Carro", variable=self.opcion, value="carro", command=self.Select).place(x=5,rely=0.3 + 0.05)
        Radiobutton(self.frame1, text="Movilidad Reducida", variable=self.opcion, value="discapacitado", command=self.Select).place(x=5, rely=0.3 + 0.1)

        self.label1.place(relx=0.5, y=50, height=50)
        self.label2.place(relx=0.5, y=110, height=50)
        self.label3.place(relx=0.5, y=170, height=50)
        self.label4.place(relx=0.5, y=230, height=50)
        self.label5.place(relx=0.035, y=30, height=50)
        self.label6.place(x=5, rely=0.2, relwidth=self.frame1.winfo_width() - 0.03)
        self.btn.place(relx=0.4, rely=0.8, width=100, height=50)

    def create_widgets(self):
        self.inicio = Button(self.master, text="Inicio", command=self.Inicio)
        self.inicio.place(relx=0.5, rely=0.5)

        font = ("Comic Sans MS", 20, "bold")
        # Frames
        self.frame1 = Frame(self.master, bg="Yellow green")
        self.frame2 = Frame(self.frame1, bg="teal")

        # Creacion de widgets al seleccionar un radiobutton
        self.frame3 = Frame(self.master, bg="teal")
        self.frame4 = Frame(self.master, bg="grey10")
        self.label7 = Label(self.master, text="Escoga el piso deseado", font=("Comic Sans MS", 14))
        self.piso = ttk.Combobox(self.master, state="readonly", values=["Piso 1", "Piso 2", "Piso 3"])
        self.label8 = Label(self.master, text="Ingrese la placa\n del vehiculo", font=("Comic Sans MS", 14))
        self.label9= Label(self.master,text="Ingrese la hora\n de entrada", font = ("Commic Sans MS", 14))
        self.placa = Text(self.master, width=15, height=1)
        self.hora= Text(self.master,width=10, height=1)

        # Labels
        self.label1 = Label(self.frame4, text="Bienvenidos a Parqueadero Popo", font=font)
        self.label2 = Label(self.frame4, text="1. Ingrese sus datos.", font=font)
        self.label3 = Label(self.frame4, text="2. Se mostrarán los lugares en pantalla.", font=font)
        self.label4 = Label(self.frame4, text="3. Escoja su lugar deseado.", font=font)
        self.label5 = Label(self.frame2, text="PARQUEADERO POPO", font=font)
        self.label6 = Label(self.frame1, text="Ingrese el tipo de parqueadero\na escoger", font=("Comic Sans MS", 14))

        self.btn = Button(self.frame1, text="Arturo Felipe", bg="green", activebackground="red")


