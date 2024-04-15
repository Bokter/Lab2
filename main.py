from tkinter import *
from tkinter import ttk


def Selec():
    frame3 = Frame(ventanaPrincipal, bg="darkorchid")
    frame3.place(x=0, rely=0.5, relwidth=0.3, relheight=0.15)
    label7 = Label(ventanaPrincipal, text="Escoga el piso deseado", font=("Comic Sans MS", 14))
    label7.place(relx=0.068, rely=0.53)
    piso = ttk.Combobox(ventanaPrincipal, state="readonly", values=["Piso 1", "Piso 2", "Piso 3"])
    piso.place(relx=0.095, rely=0.6)
    label8 = Label(ventanaPrincipal, text="Ingrese la placa del vehiculo", font=("Comic Sans MS", 14))
    label8.place(relx=0.095, rely=0.66)
    placa = Text(ventanaPrincipal, width=29, height=1)
    placa.place(relx=0.095, rely=0.73)



def Inicio():
    inicio.destroy()
    font = ("Comic Sans MS", 20, "bold")
    # Frames
    frame1 = Frame(ventanaPrincipal, bg="darkorchid1")
    frame1.place(x=0, y=0, relwidth=0.3, height=ventanaPrincipal.winfo_height())
    frame2 = Frame(frame1, bg="darkorchid")
    frame2.place(x=0, y=0, width=ventanaPrincipal.winfo_width(), relheight=0.15)

    # RadioButtons
    opcion = StringVar()
    opcion.set("")
    Radiobutton(frame1, text="Moto", variable=opcion, value="moto", command=Selec).place(x=5, rely=0.3)
    Radiobutton(frame1, text="Carro", variable=opcion, value="carro", command=Selec).place(x=5, rely=0.3 + 0.05)
    Radiobutton(frame1, text="Movilidad Reducida", variable=opcion, value="discapacitado", command=Selec).place(x=5,
                                                                                                                rely=0.3 + 0.1)

    # Labels
    label1 = Label(ventanaPrincipal, text="Bienvenidos a Parqueadero Popo", font=font)
    label1.place(relx=0.5, y=50, height=50)
    label2 = Label(ventanaPrincipal, text="1. Ingrese sus datos.", font=font)
    label2.place(relx=0.5, y=110, height=50)
    label3 = Label(ventanaPrincipal, text="2. Se mostrarán los lugares en pantalla.", font=font)
    label3.place(relx=0.5, y=170, height=50)
    label4 = Label(ventanaPrincipal, text="3. Escoja su lugar deseado.", font=font)
    label4.place(relx=0.5, y=230, height=50)
    label5 = Label(frame2, text="PARQUEADERO POPO", font=font)
    label5.place(relx=0.035, y=30, height=50)
    label6 = Label(frame1, text="Ingrese el tipo de parqueadero\na escoger", font=("Comic Sans MS", 14))
    label6.place(x=5, rely=0.2, relwidth=frame1.winfo_width() - 0.03)

    btn = Button(frame1, text="Arturo Felipe", bg="green", activebackground="red")
    btn.place(relx=0.4, rely=0.8, width=100, height=50)


ventanaPrincipal = Tk()
ventanaPrincipal.title("Inicio")
ventanaPrincipal.resizable(False, False)
ventanaPrincipal.geometry("1280x720")
ventanaPrincipal.config(bg="Yellow green")
ventanaPrincipal.iconbitmap("icono.ico")


ventanaPrincipal.mainloop()
