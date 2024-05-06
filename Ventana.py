from tkinter import *
from tkinter import messagebox, ttk
import tkinter as tk
import customtkinter
import customtkinter as ctk


class MainFrame(Frame):
    def __init__(self, master=None):
        super().__init__(master, width=1280, height=720)
        self.master = master
        self.place(x=0, y=0)
        self.config(bg="Yellow green")
        self.create_widgets()

        self.slot = ""
        self.listAux = []

    def Volver(self):
        self.label18.config(image=self.fondo)
        self.label18.place(x=0, y=0)
        self.config(bg="Yellow green")
        self.agregarVehiculo.place(relx=0.2, rely=0.5)
        self.administracion.place(relx=0.55, rely=0.5)
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
        self.label19.place_forget()
        self.label20.place_forget()
        self.volver.place_forget()

    def Administracion(self):

        self.val = 2

        self.agregarVehiculo.place_forget()
        self.administracion.place_forget()
        self.label18.config(image=self.fondoParqueadero)
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
        self.piso.bind("<<ComboboxSelected>>", self.selection_changed)
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
        from Main import Piso_1
        from Main import Piso_2
        from Main import Piso_3

        print(self.list.size())

        match (self.piso.get()):
            case "Piso 1":
                self.label17.config(text="Piso 1")
                self.label17.place(relx=0.66, rely=0.38)

                self.list.delete(1, tk.END)

                for i in Piso_1.vehicles:
                    self.list.insert(END, f"{i.getPlate()}      -       {i.getSlot()}       -       {i.getTime()}     -       {i.getVType()}")

            case "Piso 2":
                self.label17.config(text="Piso 2")
                self.label17.place(relx=0.66, rely=0.38)

                self.list.delete(1, tk.END)

                for i in Piso_2.vehicles:
                    self.list.insert(END, f"{i.getPlate()}      -       {i.getSlot()}       -       {i.getTime()}     -       {i.getVType()}")

            case "Piso 3":
                self.label17.config(text="Piso 3")
                self.label17.place(relx=0.66, rely=0.38)

                self.list.delete(1, tk.END)

                for i in Piso_3.vehicles:
                    self.list.insert(END, f"{i.getPlate()}      -       {i.getSlot()}       -       {i.getTime()}     -       {i.getVType()}")

    def Select(self):
        self.frame3.place(x=0, rely=0.5, relwidth=0.3, relheight=0.15)
        self.label7.place(relx=0.011, rely=0.505)
        self.label19.place(relx=0.2, rely=0.505)
        self.label20.place(relx=0.22, rely=0.585)
        self.label18.config(image=self.fondoParqueadero)
        self.label18.place(x=0, y=0)
        self.piso.config(width=10)
        self.piso.place(relx=0.03, rely=0.555)
        self.piso.bind("<<ComboboxSelected>>", self.selection_changed)
        self.label8.place(relx=0.01, rely=0.66)
        self.label9.place(relx=0.18, rely=0.66)
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

        self.val = 1

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
                    font=("Freeman", 14), bg="#7ED957", activebackground="#7ED957", foreground="navy").place(
            x=5, rely=0.3)
        Radiobutton(self.frame1, text="Carro", variable=self.opcion, value="carro", command=self.Select,
                    font=("Freeman", 14), bg="#7ED957", activebackground="#7ED957", foreground="navy").place(
            x=5, rely=0.3 + 0.05)
        Radiobutton(self.frame1, text="Movilidad Reducida", variable=self.opcion, value="discapacitado",
                    command=self.Select, font=("Freeman", 14), bg="#7ED957", activebackground="#7ED957",
                    foreground="navy").place(x=5, rely=0.3 + 0.1)

        # Labels
        self.label1.place(relx=0.34, y=50, height=50)
        self.label2.place(relx=0.34, y=110, height=50)
        self.label3.place(relx=0.34, y=170, height=50)
        self.label4.place(relx=0.34, y=230, height=50)
        self.label5.place(relx=0.06, y=30, height=50)
        self.label6.place(relx=0.12, rely=0.16)
        self.agregar.place(relx=0.4, rely=0.8, width=100, height=50)

    def Validacion(self, n):
        match self.val:
            case 1:
                if self.placa.get(1.0, "end-1c") == "" or self.hora.get(1.0, "end-1c") == "" or self.piso.get() == "":
                    messagebox.showerror(title="Advertencia", message="Completar todos los campos")
                else:
                    self.addVehicle(self.placa.get(1.0,"end-1c"), self.slot, self.hora.get(1.0,"end-1c"), self.opcion.get())
            case 2:

                match n:
                    case 1:
                        if self.placaBusqueda.get(1.0, "end-1c") == "":
                            messagebox.showerror(title="Advertencia", message="Completar todos los campos")
                        else:
                            self.Busqueda()
                    case 2:
                        if self.placa.get(1.0, "end-1c") == "" or self.hora.get(1.0, "end-1c") == "":
                            messagebox.showerror(title="Advertencia", message="Completar todos los campos")
                        else:
                            self.Liquidacion(self.placa.get(1.0,"end-1c"), self.hora.get(1.0,"end-1c"))

    def Busqueda(self):
        from Main import Piso_1
        from Main import Piso_2
        from Main import Piso_3

        self.encontrado = Piso_1.findVehicle(self.placaBusqueda.get(1.0,"end-1c"),1)
        if self.encontrado != False:
            return None
        self.encontrado = Piso_2.findVehicle(self.placaBusqueda.get(1.0, "end-1c"),1)
        if self.encontrado != False:
            return None
        self.encontrado = Piso_3.findVehicle(self.placaBusqueda.get(1.0, "end-1c"),1)
        if self.encontrado != False:
            return None

        if self.encontrado == False:
            messagebox.showerror(title="Búsqueda vehiculo", message="No se econtró el vehiculo")

    def create_widgets(self):
        font = ('Freeman', 38, "bold")

        self.val = 0

        self.fondo = tk.PhotoImage(file="fondoPrincipal.png")
        self.fondoParqueadero = tk.PhotoImage(file="parqueadero.png")
        self.label18 = Label(self.master, image=self.fondo)
        self.label18.place(x=0, y=0)
        self.agregarVehiculo = customtkinter.CTkButton(self.master, text="Agregar Vehículo",
                                                       font=('Freeman', 40, "bold"), height=100,
                                                       width=200, text_color="ghostwhite", fg_color="#13402A",
                                                       hover_color="forestgreen", corner_radius=30, border_width=10,
                                                       border_color="ghostwhite", command=self.AgregarVehiculo, bg_color="#7ED957")
        self.agregarVehiculo.place(relx=0.20, rely=0.5)

        self.administracion = customtkinter.CTkButton(self.master, text="Administración", font=('Freeman', 40, "bold"),
                                                      height=100,
                                                      width=200, text_color="ghostwhite", fg_color="#13402A",
                                                      hover_color="forestgreen", corner_radius=30, border_width=10,
                                                      border_color="ghostwhite", command=self.Administracion, bg_color="#7ED957")

        self.administracion.place(relx=0.55, rely=0.5)



        # Frames
        self.frame1 = Frame(self.master, bg="#7ED957")
        self.frame1_1 = Frame(self.master, bg="#7ED957")
        self.frame2 = Frame(self.frame1, bg="#13402A")
        self.frame2_2 = Frame(self.frame1_1, bg="#13402A")

        # Creacion de widgets al seleccionar un radiobutton
        self.frame3 = Frame(self.master, bg="#13402A")
        self.frame4 = Frame(self.master, bg="grey10")
        self.label7 = Label(self.master, text="Seleccione el piso", font=("Freeman", 17), bg="#13402A",
                            foreground="ghostwhite")
        self.piso = ttk.Combobox(self.master, state="readonly", values=["Piso 1", "Piso 2", "Piso 3"],
                                 font=("Freeman", 10))
        self.label8 = ctk.CTkLabel(self.master, text="Ingrese la placa\n del vehiculo", font=("Freeman", 20),
                                   text_color="ghostwhite", fg_color="#13402A", corner_radius=20, bg_color="#7ED957")
        self.label9 = ctk.CTkLabel(self.master, text="Ingrese la hora\n de entrada", font=("Freeman", 20),
                                   bg_color="#7ED957",
                                   text_color="ghostwhite", fg_color="#13402A", corner_radius=20)
        self.label19 = Label(self.master, text="Parqueadero\nEscogido", font=("Freeman", 14), bg="#13402A",
                             foreground="ghostwhite")
        self.label20 = Label(self.master, text=".", font=("Freeman", 14), bg="#13402A",
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
        self.label5 = Label(self.frame2, text="PARKEASE", font=font, bg="#13402A", foreground="ghostwhite")
        self.label5_5 = Label(self.frame2_2, text="PARKEASE", font=font, bg="#13402A", foreground="ghostwhite")
        self.label6 = ctk.CTkLabel(self.frame1, text="Ingrese el tipo de parqueadero\na escoger",
                                   font=("Freeman", 20), text_color="ghostwhite", width=90, height=70, corner_radius=20,
                                   fg_color="#13402A")
        self.label10 = Label(self.frame1_1, text="Escoga el piso deseado", font=("Freeman", 17), bg="#13402A",
                             foreground="ghostwhite")
        self.label11 = Label(self.frame1_1, text="Buscar por\n placa", font=("Freeman", 14), bg="#13402A",
                             foreground="ghostwhite")
        self.label13 = Label(self.frame1_1, text="Liquidación del vehiculo", font=("Freeman", 17), bg="#13402A",
                             foreground="ghostwhite")
        self.label14 = Label(self.frame1_1, text="Ingresar placa del vehiculo y hora de salida", bg="#13402A",
                             foreground="ghostwhite",
                             font=("Freeman", 12))
        self.label15 = Label(self.frame1_1, text="Placa", font=("Freeman", 16), bg="#7ED957", foreground="navy")
        self.label16 = Label(self.frame1_1, text="Hora", font=("Freeman", 16), bg="#7ED957", foreground="navy")
        self.label17 = Label(self.master, font=("Freeman", 30), bg="grey10", foreground="ghostwhite")


        # Botones
        self.agregar = Button(self.frame1, text="Agregar", bg="green", activebackground="red",
                              font=("Freeman", 16), command= lambda :self.Validacion(0))
        self.buscar = Button(self.frame1_1, text="Buscar", bg="green", activebackground="red",
                             font=("Freeman", 10), command=lambda:self.Validacion(1))
        self.liquidar = Button(self.frame1_1, text="Ok", bg="green", activebackground="red",
                               font=("Freeman", 10),
                               command= lambda:self.Validacion(2))
        self.volver = Button(self.master, text="Volver", bg="green", activebackground="red",
                             font=("Freeman", 10),
                             command=self.Volver)

        # Bloques de parqueo
        self.bloqueA = Button(self.master, text="A", bg="green", font=("Freeman", 30),
                              command=lambda: self.changeLabel("A", 0, 10))
        self.bloqueB = Button(self.master, text="B", bg="green", font=("Freeman", 30),
                              command=lambda: self.changeLabel("B", 1, 16))
        self.bloqueC = Button(self.master, text="C", bg="green", font=("Freeman", 30),
                              command=lambda: self.changeLabel("C", 2, 16))
        self.bloqueD = Button(self.master, text="D", bg="green", font=("Freeman", 30),
                              command=lambda: self.changeLabel("D", 3, 16))
        self.bloqueE = Button(self.master, text="E", bg="green", font=("Freeman", 30),
                              command=lambda: self.changeLabel("E", 4, 16))
        self.bloqueF = Button(self.master, text="F", bg="green", font=("Freeman", 30),
                              command=lambda: self.changeLabel("F", 5, 16))
        self.bloqueG = Button(self.master, text="G", bg="green", font=("Freeman", 30),
                              command=lambda: self.changeLabel("G", 6, 20))
        self.bloqueH = Button(self.master, text="H", bg="green", font=("Freeman", 30),
                              command=lambda: self.changeLabel("H", 7, 20))
        self.bloqueI = Button(self.master, text="I", bg="green", font=("Freeman", 30),
                              command=lambda: self.changeLabel("I", 8, 20))
        self.bloqueJ = Button(self.master, text="J", bg="green", font=("Freeman", 30),
                              command=lambda: self.changeLabel("J", 9, 20))
        self.bloqueK = Button(self.master, text="K", bg="green", font=("Freeman", 30),
                              command=lambda: self.changeLabel("K", 10, 20))
        self.bloqueL = Button(self.master, text="L", bg="green", font=("Freeman", 30),
                              command=lambda: self.changeLabel("L", 11, 20))

        # Lista vehiculos
        self.label12 = LabelFrame(self.master, text="Lista de vehiculos:", width=345, height=240, font=("Freeman", 10))
        self.titulos_lista = ("Placa    -   Lugar    -   Hora de entrada    -   Tipo vehiculo")
        self.listaVehiculos = []
        self.scrollbar = Scrollbar(self.frame1_1, orient=VERTICAL)
        self.list = Listbox(self.label12, width=47, height=9, yscrollcommand=self.scrollbar.set, font=("Freeman", 10))
        self.scrollbar.config(command=self.list.yview)
        self.list.insert(0, self.titulos_lista)
        self.list.insert(1, *self.listaVehiculos)

    def changeLabel(self, block, index, max):
        from Main import Piso_1
        from Main import Piso_2
        from Main import Piso_3

        match self.val:
            case 1:
                match (self.piso.get()):
                    case "Piso 1":
                        num = Piso_1.current[index]

                        if num + 1 > max - 1:
                            Piso_1.current[index] = 0
                        else:
                            Piso_1.current[index] += 1

                        self.slot = f"P1{block}{num + 1}"
                        self.label20.config(text=self.slot)

                    case "Piso 2":
                        num = Piso_2.current[index]

                        if num + 1 > max - 1:
                            Piso_2.current[index] = 0
                        else:
                            Piso_2.current[index] += 1

                        self.slot = f"P2{block}{num + 1}"
                        self.label20.config(text=self.slot)

                    case "Piso 3":
                        num = Piso_3.current[index]

                        if num + 1 > max - 1:
                            Piso_3.current[index] = 0
                        else:

                            Piso_3.current[index] += 1

                            Piso_3.current[index] += 1

                        self.slot = f"P3{block}{num + 1}"
                        self.label20.config(text=self.slot)


            case 2:

                match (self.piso.get()):
                    case "Piso 1":
                        self.label17.config(text="Piso 1")
                        self.label17.place(relx=0.66, rely=0.38)

                        self.list.delete(1, tk.END)

                        for i in Piso_1.vehicles:
                            if block in i.getSlot():
                                self.list.insert(END,f"{i.getPlate()}      -       {i.getSlot()}       -       {i.getTime()}     -       {i.getVType()}")

                    case "Piso 2":
                        self.label17.config(text="Piso 2")
                        self.label17.place(relx=0.66, rely=0.38)

                        self.list.delete(1, tk.END)

                        for i in Piso_2.vehicles:
                            if block in i.getSlot():
                                self.list.insert(END,
                                                 f"{i.getPlate()}      -       {i.getSlot()}       -       {i.getTime()}     -       {i.getVType()}")

                    case "Piso 3":
                        self.label17.config(text="Piso 3")
                        self.label17.place(relx=0.66, rely=0.38)

                        self.list.delete(1, tk.END)

                        for i in Piso_3.vehicles:
                            if block in i.getSlot():
                                self.list.insert(END,
                                                 f"{i.getPlate()}      -       {i.getSlot()}       -       {i.getTime()}     -       {i.getVType()}")

                pass

    def addVehicle(self, placa, slot, entryTime, VType):
        from Main import Vehicle
        from Main import Piso_1
        from Main import Piso_2
        from Main import Piso_3

        dp = False

        match VType:
            case "moto":
                VType = "M"
            case "carro":
                VType = "C"
            case "discapacitado":
                VType = "D"

        if ":" in entryTime:
            a = entryTime.split(":")
            if int(a[0]) >= 0 and int(a[0]) <= 23 and int(a[1]) >= 0 and int(a[1]) <= 59:
                dp = True

        if dp and len(placa) == 6:

            v = Vehicle(placa, slot, entryTime, VType)

            match (self.piso.get()):
                case "Piso 1":
                    if Piso_1.addVehicle(v):
                        messagebox.showinfo(title="Agregar Vehiculo", message="Vehiculo añadido exitosamente")

                        self.list.insert(END,f"{placa}        -       {slot}      -       {entryTime}         -       {VType}")

                        self.listaVehiculos.append(f"{placa}        -       {slot}      -       {entryTime}         -       {VType}")

                case "Piso 2":
                    if Piso_2.addVehicle(v):
                        messagebox.showinfo(title="Agregar Vehiculo", message="Vehiculo añadido exitosamente")
                        self.list.insert(END,f"{placa}        -       {slot}      -       {entryTime}         -       {VType}")

                        self.listaVehiculos.append(f"{placa}        -       {slot}      -       {entryTime}         -       {VType}")
                case "Piso 3":
                    if Piso_3.addVehicle(v):
                        messagebox.showinfo(title="Agregar Vehiculo", message="Vehiculo añadido exitosamente")

                        self.list.insert(END,f"{placa}        -       {slot}      -       {entryTime}         -       {VType}")

                        self.listaVehiculos.append(f"{placa}        -       {slot}      -       {entryTime}         -       {VType}")

            print(self.listaVehiculos)
        else:
            messagebox.showinfo(title="Datos Invalidos",
                                message="El vehiculo no se pudo añadir\nRevise sus datos")

    def Liquidacion(self, plate, time):

        dv = False

        from Main import plates

        from Main import Piso_1
        from Main import Piso_2
        from Main import Piso_3

        # Determinar si la placa existe

        for p in plates:
            if plate == p:
                dv = True

        if ":" in time:
            a = time.split(":")
            if int(a[0]) >= 0 and int(a[0]) <= 23 and int(a[1]) >= 0 and int(a[1]) <= 59:
                dp = True
            else:
                messagebox.showinfo(title="Liquidacion",message="Tiempo invalido")
                return

        if dv and dp:
            n = Piso_1.findVehicle(plate,0)
            if n == False:
                n = Piso_2.findVehicle(plate,0)
                if n == False:
                    Piso_3.clearVehicle(plate,time)
                else:
                    Piso_2.clearVehicle(plate,time)
            else:
                Piso_1.clearVehicle(plate,time)
        else:
            messagebox.showinfo(title="Liquidacion",message="Placa no encontrada")



