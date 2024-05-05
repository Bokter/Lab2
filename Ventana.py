from tkinter import *
from tkinter import messagebox, ttk
import customtkinter
import customtkinter as ctk

class MainFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=1280, height=720)
        self.master = master
        self.place(x=0, y=0)
        self.config(bg="Yellow green")
        self.create_widgets()

    def Volver(self):
        self.config(bg="Yellow green")
        self.agregarVehiculo.place(relx=0.4, rely=0.5)
        self.administracion.place(relx=0.41, rely=0.75)
        self.label18.place(relx=0.44, rely=0.1)
        self.OcultarBloques()
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
        self.label17.place_forget()
        self.volver.place_forget()

    def Liquidacion(self):
        messagebox.showinfo(title="Liquidación", message="Monto a pagar\n si", )

    def Administracion(self):
        self.agregarVehiculo.place_forget()
        self.administracion.place_forget()
        self.label18.place_forget()
        self.config(bg="grey10")

        # Frames
        self.frame1_1.place(x=0, y=0, relwidth=0.3, height=self.master.winfo_height())
        self.frame2_2.place(x=0, y=0, width=self.master.winfo_width(), relheight=0.15)

        # Labels
        self.label5_5.place(relx=0.06, y=30, height=50)
        self.label10.place(relx=0.016, rely=0.17)
        self.label11.place(relx=0.035, rely=0.27)
        self.label13.place(relx=0.2, rely=0.73)
        self.label14.place(relx=0.13, rely=0.8)
        self.label15.place(relx=0.22, rely=0.85)
        self.label16.place(relx=0.7, rely=0.85)

        self.placaBusqueda.place(relx=0.1, rely=0.3)
        self.placa.place(relx=0.035, rely=0.9)
        self.hora.place(relx=0.2, rely=0.9)
        self.piso.config(width=10)
        self.piso.place(relx=0.2, rely=0.176)

        # Botones
        self.buscar.place(relx=0.7, rely=0.29)
        self.liquidar.place(relx=0.5, rely=0.9)
        self.volver.place(relx=0.9, rely=0.91)
        self.MostrarBloques()

        # Lista de vehiculos
        self.label12.place(relx=0.015, rely=0.38)
        self.list.place(x=2, y=2)
        self.scrollbar.pack(side=RIGHT)
        self.list.insert(0, self.titulos_lista)
        self.list.insert(1, *self.listaVehiculos)

    def OcultarBloques(self):
        # Motos
        self.bloqueG.place_forget()
        self.bloqueH.place_forget()
        self.bloqueI.place_forget()
        self.bloqueJ.place_forget()
        self.bloqueK.place_forget()
        self.bloqueL.place_forget()

        # Carros
        self.bloqueB.place_forget()
        self.bloqueC.place_forget()
        self.bloqueD.place_forget()
        self.bloqueE.place_forget()
        self.bloqueF.place_forget()

        # Discapacitado
        self.bloqueA.place_forget()

    def DisabledCarros(self):
        self.bloqueB.config(bg="grey", state="disabled")
        self.bloqueC.config(bg="grey", state="disabled")
        self.bloqueD.config(bg="grey", state="disabled")
        self.bloqueE.config(bg="grey", state="disabled")
        self.bloqueF.config(bg="grey", state="disabled")

    def DisabledMotos(self):
        self.bloqueG.config(bg="grey", state="disabled")
        self.bloqueH.config(bg="grey", state="disabled")
        self.bloqueI.config(bg="grey", state="disabled")
        self.bloqueJ.config(bg="grey", state="disabled")
        self.bloqueK.config(bg="grey", state="disabled")
        self.bloqueL.config(bg="grey", state="disabled")

    def MostrarCarros(self):
        self.bloqueB.config(bg="green", state="normal")
        self.bloqueC.config(bg="green", state="normal")
        self.bloqueD.config(bg="green", state="normal")
        self.bloqueE.config(bg="green", state="normal")
        self.bloqueF.config(bg="green", state="normal")

    def MostrarMotos(self):
        self.bloqueG.config(bg="green", state="normal")
        self.bloqueH.config(bg="green", state="normal")
        self.bloqueI.config(bg="green", state="normal")
        self.bloqueJ.config(bg="green", state="normal")
        self.bloqueK.config(bg="green", state="normal")
        self.bloqueL.config(bg="green", state="normal")

    def MostrarBloques(self):
        self.MostrarMotos()
        self.MostrarCarros()
        self.bloqueA.config(bg="green", state="normal")
        # Carros
        self.bloqueB.place(relx=0.46, y=5, width=140, height=220)
        self.bloqueC.place(relx=0.57, y=5, width=140, height=220)
        self.bloqueD.place(relx=0.68, y=5, width=140, height=220)
        self.bloqueE.place(relx=0.79, y=5, width=140, height=220)
        self.bloqueF.place(relx=0.9, y=5, width=140, height=220)

        # Motos
        self.bloqueG.place(relx=0.35, rely=0.6, width=140, height=220)
        self.bloqueH.place(relx=0.46, rely=0.6, width=140, height=220)
        self.bloqueI.place(relx=0.57, rely=0.6, width=140, height=220)
        self.bloqueJ.place(relx=0.68, rely=0.6, width=140, height=220)
        self.bloqueK.place(relx=0.79, rely=0.6, width=140, height=220)
        self.bloqueL.place(relx=0.9, rely=0.6, width=140, height=220)

        # Discapacitado
        self.bloqueA.place(relx=0.35, y=5, width=140, height=220)

    def selection_changed(self, event):
        match (self.piso.get()):
            case "Piso 1":
                self.label17.config(text="Piso 1")
                self.label17.place(relx=0.66, rely=0.4)
            case "Piso 2":
                self.label17.config(text="Piso 2")
                self.label17.place(relx=0.66, rely=0.4)
            case "Piso 3":
                self.label17.config(text="Piso 3")
                self.label17.place(relx=0.66, rely=0.4)

    def Select(self):
        self.frame3.place(x=0, rely=0.5, relwidth=0.3, relheight=0.15)
        self.label7.place(relx=0.066, rely=0.5)
        self.piso.config(width=20)
        self.piso.place(relx=0.09, rely=0.57)
        self.piso.bind("<<ComboboxSelected>>", self.selection_changed)
        self.label8.place(relx=0.02, rely=0.66)
        self.label9.place(relx=0.19, rely=0.66)
        self.placa.place(relx=0.022, rely=0.76)
        self.hora.place(relx=0.205, rely=0.76)
        self.label1.place_forget()
        self.label2.place_forget()
        self.label3.place_forget()
        self.label4.place_forget()
        self.MostrarBloques()

        match self.opcion.get():
            case "moto":
                self.MostrarMotos()
                self.bloqueA.config(bg="grey", state="disabled")
                self.DisabledCarros()

            case "carro":
                self.MostrarCarros()
                self.bloqueA.config(bg="grey", state="disabled")
                self.DisabledMotos()

            case "discapacitado":
                self.bloqueA.config(bg="green", state="normal")
                self.DisabledCarros()
                self.DisabledMotos()

    def AgregarVehiculo(self):
        self.agregarVehiculo.place_forget()
        self.administracion.place_forget()
        self.label18.place_forget()
        self.config(bg="grey10")
        self.frame1.place(x=0, y=0, relwidth=0.3, height=self.master.winfo_height())
        self.frame2.place(x=0, y=0, width=self.master.winfo_width(), relheight=0.15)
        self.volver.place(relx=0.9, rely=0.91)

        # RadioButtons
        self.opcion = StringVar()
        self.opcion.set(None)
        Radiobutton(self.frame1, text="Moto", variable=self.opcion, value="moto", command=self.Select,
                    font=("Freeman", 14), bg="Yellow green", activebackground="Yellow green", foreground="navy").place(
            x=5, rely=0.3)
        Radiobutton(self.frame1, text="Carro", variable=self.opcion, value="carro", command=self.Select,
                    font=("Freeman", 14), bg="Yellow green", activebackground="Yellow green", foreground="navy").place(
            x=5, rely=0.3 + 0.05)
        Radiobutton(self.frame1, text="Movilidad Reducida", variable=self.opcion, value="discapacitado",
                    command=self.Select, font=("Freeman", 14), bg="Yellow green", activebackground="Yellow green",
                    foreground="navy").place(x=5, rely=0.3 + 0.1)

        # Labels
        self.label1.place(relx=0.34, y=50, height=50)
        self.label2.place(relx=0.34, y=110, height=50)
        self.label3.place(relx=0.34, y=170, height=50)
        self.label4.place(relx=0.34, y=230, height=50)
        self.label5.place(relx=0.06, y=30, height=50)
        self.label6.place(relx=0.12, rely=0.16)
        self.agregar.place(relx=0.4, rely=0.8, width=100, height=50)

    def create_widgets(self):
        font = ('Freeman', 38, "bold")

        self.agregarVehiculo = customtkinter.CTkButton(self.master, text="Agregar Vehículo",
                                                       font=('Freeman', 40, "bold"), height=100,
                                                       width=200, text_color="ghostwhite", fg_color="deepskyblue3",
                                                       hover_color="forestgreen", corner_radius=30, border_width=10,
                                                       border_color="Coral", command=self.AgregarVehiculo,
                                                       bg_color="Yellow green")
        self.agregarVehiculo.place(relx=0.4, rely=0.5)
        self.administracion = customtkinter.CTkButton(self.master, text="Administración", font=('Freeman', 40, "bold"),
                                                      height=100,
                                                      width=200, text_color="ghostwhite", fg_color="deepskyblue3",
                                                      hover_color="forestgreen", corner_radius=30, border_width=10,
                                                      border_color="Coral", command=self.Administracion,
                                                      bg_color="Yellow green")
        self.administracion.place(relx=0.41, rely=0.75)

        # Frames
        self.frame1 = Frame(self.master, bg="Yellow green")
        self.frame1_1 = Frame(self.master, bg="Yellow green")
        self.frame2 = Frame(self.frame1, bg="teal")
        self.frame2_2 = Frame(self.frame1_1, bg="teal")

        # Creacion de widgets al seleccionar un radiobutton
        self.frame3 = Frame(self.master, bg="teal")
        self.frame4 = Frame(self.master, bg="grey10")
        self.label7 = Label(self.master, text="Escoga el piso deseado", font=("Freeman", 17), bg="teal",
                            foreground="ghostwhite")
        self.piso = ttk.Combobox(self.master, state="readonly", values=["Piso 1", "Piso 2", "Piso 3"],
                                 font=("Freeman", 10))
        self.label8 = Label(self.master, text="Ingrese la placa\n del vehiculo", font=("Freeman", 14), bg="teal",
                            foreground="ghostwhite")
        self.label9 = Label(self.master, text="Ingrese la hora\n de entrada", font=("Freeman", 14), bg="teal",
                            foreground="ghostwhite")
        self.placa = Text(self.master, width=15, height=1)
        self.placaBusqueda = Text(self.master, width=15, height=1)
        self.hora = Text(self.master, width=10, height=1)

        # Labels
        self.label1 = Label(self.master, text="Bienvenidos a ParkEase", font=font, bg="grey10", foreground="ghostwhite")
        self.label2 = Label(self.master, text="1. Ingrese sus datos.", font=font, bg="grey10", foreground="ghostwhite")
        self.label3 = Label(self.master, text="2. Se mostrarán los lugares en pantalla.", font=font, bg="grey10",
                            foreground="ghostwhite")
        self.label4 = Label(self.master, text="3. Escoja su lugar deseado.", font=font, bg="grey10",
                            foreground="ghostwhite")
        self.label5 = Label(self.frame2, text="PARKEASE", font=font, bg="teal", foreground="ghostwhite")
        self.label5_5 = Label(self.frame2_2, text="PARKEASE", font=font, bg="teal", foreground="ghostwhite")
        self.label6 = Label(self.frame1, text="Ingrese el tipo de parqueadero\na escoger",
                            font=("Freeman", 17), bg="teal", foreground="ghostwhite")
        self.label10 = Label(self.frame1_1, text="Escoga el piso deseado", font=("Freeman", 17), bg="teal",
                             foreground="ghostwhite")
        self.label11 = Label(self.frame1_1, text="Buscar por\n placa", font=("Freeman", 14), bg="teal",
                             foreground="ghostwhite")
        self.label13 = Label(self.frame1_1, text="Liquidación del vehiculo", font=("Freeman", 17), bg="teal",
                             foreground="ghostwhite")
        self.label14 = Label(self.frame1_1, text="Ingresar placa del vehiculo y hora de salida", bg="teal",
                             foreground="ghostwhite",
                             font=("Freeman", 12))
        self.label15 = Label(self.frame1_1, text="Placa", font=("Freeman", 16), bg="Yellow green", foreground="navy")
        self.label16 = Label(self.frame1_1, text="Hora", font=("Freeman", 16), bg="Yellow green", foreground="navy")
        self.label17 = Label(self.master, font=("Freeman", 30), bg="grey10", foreground="ghostwhite")
        self.label18 = Label(self.master, text="PARKEASE", font=("Freeman", 40), bg="teal", foreground="ghostwhite", borderwidth=10, relief="ridge")
        self.label18.place(relx= 0.44, rely=0.1)

        # Botones
        self.agregar = Button(self.frame1, text="Agregar", bg="green", activebackground="red",
                              font=("Freeman", 16))
        self.buscar = Button(self.frame1_1, text="Buscar", bg="green", activebackground="red",
                             font=("Freeman", 10))
        self.liquidar = Button(self.frame1_1, text="Ok", bg="green", activebackground="red",
                               font=("Freeman", 10),
                               command=self.Liquidacion)
        self.volver = Button(self.master, text="Volver", bg="green", activebackground="red",
                             font=("Freeman", 10),
                             command=self.Volver)

        # Bloques de parqueo
        self.bloqueA = Button(self.master, text="A", bg="green", font=("Freeman", 30))
        self.bloqueB = Button(self.master, text="B", bg="green", font=("Freeman", 30))
        self.bloqueC = Button(self.master, text="C", bg="green", font=("Freeman", 30))
        self.bloqueD = Button(self.master, text="D", bg="green", font=("Freeman", 30))
        self.bloqueE = Button(self.master, text="E", bg="green", font=("Freeman", 30))
        self.bloqueF = Button(self.master, text="F", bg="green", font=("Freeman", 30))
        self.bloqueG = Button(self.master, text="G", bg="green", font=("Freeman", 30))
        self.bloqueH = Button(self.master, text="H", bg="green", font=("Freeman", 30))
        self.bloqueI = Button(self.master, text="I", bg="green", font=("Freeman", 30))
        self.bloqueJ = Button(self.master, text="J", bg="green", font=("Freeman", 30))
        self.bloqueK = Button(self.master, text="K", bg="green", font=("Freeman", 30))
        self.bloqueL = Button(self.master, text="L", bg="green", font=("Freeman", 30))

        # Lista vehiculos
        self.label12 = LabelFrame(self.master, text="Lista de vehiculos:", width=345, height=240, font=("Freeman", 10))
        self.titulos_lista = ("Placa    -   Lugar    -   Hora de entrada    -   Tipo vehiculo")
        self.listaVehiculos = (
            "CFC-223", "WGC-678", "XCV-123", "YTR-456", "VBN-789", "CBA-012", "CAB-345", "DEF-678", "GHI-901",
            "JKL-123")
        self.scrollbar = Scrollbar(self.frame1_1, orient=VERTICAL)
        self.list = Listbox(self.label12, width=47, height=9, yscrollcommand=self.scrollbar.set, font=("Freeman", 10))
        self.scrollbar.config(command=self.list.yview)
