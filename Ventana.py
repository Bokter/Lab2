from tkinter import *
from tkinter import ttk




class MainFrame(Frame):
    def __init__(self,master = None):
        super().__init__(master, width=1280, height= 720)
        self.master=master
        self.place(x=0,y=0)


    def create_widgets(self):
        self.inicio = Button(self.master, text="Inicio", command=Inicio)
        self.inicio.place(relx=0.5, rely=0.5)

        font = ("Comic Sans MS", 20, "bold")
        # Frames
        frame1 = Frame(self.master, bg="darkorchid1")
        frame1.place(x=0, y=0, relwidth=0.3, height=self.master.winfo_height())
        frame2 = Frame(frame1, bg="darkorchid")
        frame2.place(x=0, y=0, width=self.master.winfo_width(), relheight=0.15)

        # RadioButtons
        self.opcion = StringVar()
        self.opcion.set("")
        Radiobutton(frame1, text="Moto", variable=self.opcion, value="moto", command=Selec).place(x=5, rely=0.3)
        Radiobutton(frame1, text="Carro", variable=self.opcion, value="carro", command=Selec).place(x=5, rely=0.3 + 0.05)
        Radiobutton(frame1, text="Movilidad Reducida", variable=self.opcion, value="discapacitado", command=Selec).place(x=5, rely=0.3 + 0.1)

        # Labels
        self.label1 = Label(self.master, text="Bienvenidos a Parqueadero Popo", font=font)
        self.label1.place(relx=0.5, y=50, height=50)
        self.label2 = Label(self.master, text="1. Ingrese sus datos.", font=font)
        self.label2.place(relx=0.5, y=110, height=50)
        self.label3 = Label(self.master, text="2. Se mostrarán los lugares en pantalla.", font=font)
        self.label3.place(relx=0.5, y=170, height=50)
        self.label4 = Label(self.master, text="3. Escoja su lugar deseado.", font=font)
        self.label4.place(relx=0.5, y=230, height=50)
        self.label5 = Label(frame2, text="PARQUEADERO POPO", font=font)
        self.label5.place(relx=0.035, y=30, height=50)
        self.label6 = Label(frame1, text="Ingrese el tipo de parqueadero\na escoger", font=("Comic Sans MS", 14))
        self.label6.place(x=5, rely=0.2, relwidth=frame1.winfo_width() - 0.03)

        self.btn = Button(frame1, text="Arturo Felipe", bg="green", activebackground="red")
        self.btn.place(relx=0.4, rely=0.8, width=100, height=50)