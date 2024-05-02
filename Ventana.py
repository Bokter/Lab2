from tkinter import *
from tkinter import messagebox, ttk


class MainFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=1280, height=720)
        self.master = master
        self.place(x=0, y=0)
        self.config(bg="Yellow green")
        self.create_widgets()

    def Volver(self):
        self.config(bg="Yellow green")
        self.inicio.place(relx=0.5, rely=0.5)
        self.inicio2.place(relx=0.5, rely=0.55)
        self.OcultarMotos()
        self.OcultarCarros()
        self.bloqueA.place_forget()
        self.frame1.place_forget()
        self.frame1_1.place_forget()
        self.frame2_2.place_forget()
        self.frame2.place_forget()
        self.frame3.place_forget()
        self.frame4.place_forget()
        self.piso.place_forget()
        self.placa.place_forget()
        self.placaBusqueda.place_forget()
        self.hora.place_forget()
        self.label12.place_forget()
        self.label7.place_forget()
        self.label8.place_forget()
        self.label9.place_forget()
        self.label1.place_forget()
        self.label2.place_forget()
        self.label3.place_forget()
        self.label4.place_forget()
        self.list.place_forget()
        self.scrollbar.place_forget()
        self.volver.place_forget()

    def Liquidacion(self):
        messagebox.showinfo(title="Liquidación", message="Monto a pagar\n si",)

    def Incio2(self):
        self.inicio.place_forget()
        self.inicio2.place_forget()
        self.config(bg="grey10")

        # Frames
        self.frame1_1.place(x=0, y=0, relwidth=0.3, height=self.master.winfo_height())
        self.frame2_2.place(x=0, y=0, width=self.master.winfo_width(), relheight=0.15)

        # Labels
        self.label5_5.place(relx=0.035, y=30, height=50)
        self.label10.place(relx=0.25, rely=0.17)
        self.label11.place(relx=0.035, rely=0.27)
        self.label13.place(relx=0.1, rely=0.73)
        self.label14.place(relx=0.08, rely=0.8)
        self.label15.place(relx=0.22, rely=0.85)
        self.label16.place(relx=0.7, rely=0.85)

        self.placaBusqueda.place(relx=0.1, rely=0.3)
        self.placa.place(relx=0.035, rely=0.9)
        self.hora.place(relx=0.2, rely=0.9)
        self.piso.place(relx=0.1, rely=0.22)

        # Botones
        self.buscar.place(relx=0.7, rely=0.29)
        self.liquidar.place(relx=0.5, rely=0.9)
        self.volver.place(relx=0.9, rely=0.91)
        self.MostrarCarros()
        self.MostrarMotos()
        self.bloqueA.place(relx=0.35, y=5, width=140, height=220)

        # Lista de vehiculos
        self.label12.place(relx=0.015, rely=0.38)
        self.list.place(x=2, y=2)
        self.scrollbar.pack(side=RIGHT)
        self.list.insert(0, self.titulos_lista)
        self.list.insert(1, *self.listaVehiculos)

    def OcultarMotos(self):
        self.bloqueG.place_forget()
        self.bloqueH.place_forget()
        self.bloqueI.place_forget()
        self.bloqueJ.place_forget()
        self.bloqueK.place_forget()
        self.bloqueL.place_forget()

    def OcultarCarros(self):
        self.bloqueB.place_forget()
        self.bloqueC.place_forget()
        self.bloqueD.place_forget()
        self.bloqueE.place_forget()
        self.bloqueF.place_forget()

    def MostrarCarros(self):
        self.bloqueB.place(relx=0.46, y=5, width=140, height=220)
        self.bloqueC.place(relx=0.57, y=5, width=140, height=220)
        self.bloqueD.place(relx=0.68, y=5, width=140, height=220)
        self.bloqueE.place(relx=0.79, y=5, width=140, height=220)
        self.bloqueF.place(relx=0.9, y=5, width=140, height=220)

    def MostrarMotos(self):
        self.bloqueG.place(relx=0.35, rely=0.6, width=140, height=220)
        self.bloqueH.place(relx=0.46, rely=0.6, width=140, height=220)
        self.bloqueI.place(relx=0.57, rely=0.6, width=140, height=220)
        self.bloqueJ.place(relx=0.68, rely=0.6, width=140, height=220)
        self.bloqueK.place(relx=0.79, rely=0.6, width=140, height=220)
        self.bloqueL.place(relx=0.9, rely=0.6, width=140, height=220)

    def Select(self):
        self.frame3.place(x=0, rely=0.5, relwidth=0.3, relheight=0.15)
        self.label7.place(relx=0.068, rely=0.53)
        self.piso.place(relx=0.095, rely=0.6)
        self.label8.place(relx=0.017, rely=0.66)
        self.label9.place(relx=0.17, rely=0.66)
        self.placa.place(relx=0.026, rely=0.75)
        self.hora.place(relx=0.19, rely=0.75)
        self.label1.place_forget()
        self.label2.place_forget()
        self.label3.place_forget()
        self.label4.place_forget()

        match self.opcion.get():
            case "moto":
                self.MostrarMotos()
                self.bloqueA.place_forget()
                self.OcultarCarros()

            case "carro":
                self.MostrarCarros()
                self.bloqueA.place_forget()
                self.OcultarMotos()

            case "discapacitado":
                self.bloqueA.place(relx=0.35, y=5, width=140, height=220)
                self.OcultarCarros()
                self.OcultarMotos()

    def Inicio(self):
        self.inicio.place_forget()
        self.inicio2.place_forget()
        self.config(bg="grey10")
        self.frame1.place(x=0, y=0, relwidth=0.3, height=self.master.winfo_height())
        self.frame2.place(x=0, y=0, width=self.master.winfo_width(), relheight=0.15)
        self.volver.place(relx=0.9, rely=0.91)

        # RadioButtons
        self.opcion = StringVar()
        self.opcion.set(None)
        Radiobutton(self.frame1, text="Moto", variable=self.opcion, value="moto", command=self.Select).place(x=5,
                                                                                                             rely=0.3)
        Radiobutton(self.frame1, text="Carro", variable=self.opcion, value="carro", command=self.Select).place(x=5,
                                                                                                               rely=0.3 + 0.05)
        Radiobutton(self.frame1, text="Movilidad Reducida", variable=self.opcion, value="discapacitado",
                    command=self.Select).place(x=5, rely=0.3 + 0.1)

        # Labels
        self.label1.place(relx=0.5, y=50, height=50)
        self.label2.place(relx=0.5, y=110, height=50)
        self.label3.place(relx=0.5, y=170, height=50)
        self.label4.place(relx=0.5, y=230, height=50)
        self.label5.place(relx=0.035, y=30, height=50)
        self.label6.place(relx=0.14, rely=0.18)
        self.agregar.place(relx=0.4, rely=0.8, width=100, height=50)

    def create_widgets(self):
        self.inicio = Button(self.master, text="Inicio", command=self.Inicio)
        self.inicio.place(relx=0.5, rely=0.5)
        self.inicio2 = Button(self.master, text="Inicio2", command=self.Incio2)
        self.inicio2.place(relx=0.5, rely=0.55)

        font = ("Comic Sans MS", 20, "bold")
        # Frames
        self.frame1 = Frame(self.master, bg="Yellow green")
        self.frame1_1 = Frame(self.master, bg="Yellow green")
        self.frame2 = Frame(self.frame1, bg="teal")
        self.frame2_2 = Frame(self.frame1_1, bg="teal")

        # Creacion de widgets al seleccionar un radiobutton
        self.frame3 = Frame(self.master, bg="teal")
        self.frame4 = Frame(self.master, bg="grey10")
        self.label7 = Label(self.master, text="Escoga el piso deseado", font=("Comic Sans MS", 14))
        self.piso = ttk.Combobox(self.master, state="readonly", values=["Piso 1", "Piso 2", "Piso 3"])
        self.label8 = Label(self.master, text="Ingrese la placa\n del vehiculo", font=("Comic Sans MS", 14))
        self.label9 = Label(self.master, text="Ingrese la hora\n de entrada", font=("Commic Sans MS", 14))
        self.placa = Text(self.master, width=15, height=1)
        self.placaBusqueda = Text(self.master, width=15, height=1)
        self.hora = Text(self.master, width=10, height=1)

        # Labels
        self.label1 = Label(self.master, text="Bienvenidos a Parqueadero Popo", font=font)
        self.label2 = Label(self.master, text="1. Ingrese sus datos.", font=font)
        self.label3 = Label(self.master, text="2. Se mostrarán los lugares en pantalla.", font=font)
        self.label4 = Label(self.master, text="3. Escoja su lugar deseado.", font=font)
        self.label5 = Label(self.frame2, text="PARQUEADERO POPO", font=font)
        self.label5_5 = Label(self.frame2_2, text="PARQUEADERO POPO", font=font)
        self.label6 = Label(self.frame1, text="Ingrese el tipo de parqueadero\na escoger", font=("Comic Sans MS", 14))
        self.label10 = Label(self.frame1_1, text="Escoga el piso deseado", font=("Comic Sans MS", 14))
        self.label11 = Label(self.frame1_1, text="Buscar por\n placa", font=("Comic Sans MS", 14))
        self.label13 = Label(self.frame1_1, text="Liquidación del vehiculo", font=font)
        self.label14 = Label(self.frame1_1, text="Ingresar placa del vehiculo y hora de salida", font=("Comic Sans MS", 12))
        self.label15 = Label(self.frame1_1, text="Placa", font=("Comic Sans MS", 16))
        self.label16 = Label(self.frame1_1, text="Hora", font=("Comic Sans MS", 16))

        # Botones
        self.agregar = Button(self.frame1, text="Arturo Felipe", bg="green", activebackground="red",
                              font=("Comic Sans MS", 10))
        self.buscar = Button(self.frame1_1, text="Buscar", bg="green", activebackground="red",
                             font=("Comic Sans MS", 10))
        self.liquidar = Button(self.frame1_1, text="Ok", bg="green", activebackground="red", font=("Comic Sans MS", 10),
                               command=self.Liquidacion)
        self.volver = Button(self.master, text="Volver", bg="green", activebackground="red", font=("Comic Sans Ms", 10),
                             command=self.Volver)

        # Bloques de parqueo
        self.bloqueA = Button(self.master, text="A", bg="green")
        self.bloqueB = Button(self.master, text="B", bg="green")
        self.bloqueC = Button(self.master, text="C", bg="green")
        self.bloqueD = Button(self.master, text="D", bg="green")
        self.bloqueE = Button(self.master, text="E", bg="green")
        self.bloqueF = Button(self.master, text="F", bg="green")
        self.bloqueG = Button(self.master, text="G", bg="green")
        self.bloqueH = Button(self.master, text="H", bg="green")
        self.bloqueI = Button(self.master, text="I", bg="green")
        self.bloqueJ = Button(self.master, text="J", bg="green")
        self.bloqueK = Button(self.master, text="K", bg="green")
        self.bloqueL = Button(self.master, text="L", bg="green")

        # Lista vehiculos
        self.label12 = LabelFrame(self.master, text="Lista de vehiculos:", width=345, height=240)
        self.titulos_lista =("Placa    -   Lugar    -   Hora de entrada    -   Tipo vehiculo")
        self.listaVehiculos = (
            "CFC-223", "WGC-678", "XCV-123", "YTR-456", "VBN-789", "CBA-012", "CAB-345", "DEF-678", "GHI-901",
            "JKL-123")
        self.scrollbar = Scrollbar(self.frame1_1, orient=VERTICAL)
        self.list = Listbox(self.label12, width=55, height=12, yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.list.yview)
