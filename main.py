from tkinter import *
from tkinter import ttk


def arturoFelipe():
    root2 = Tk()

    root2.title('Arturo Felipe2')
    root2.resizable(False, False)
    root2.geometry("1280x720")
    root2.config(background="green")
    btn.config(background="red")
    root2.mainloop()


def Selec():
    frame3 = Frame(frame1, bg="darkorchid")
    frame3.place(x=0, rely=0.5, width=root.winfo_width(), relheight=0.15)
    label7= Label(frame3, text="Escoga el piso deseado", font=("Comic Sans MS", 14))
    label7.place(relx=0.068,rely=0.1)
    piso = ttk.Combobox(frame3, state="readonly",values=["Piso 1", "Piso 2", "Piso 3"])
    piso.place(relx=0.095, rely=0.5)
    label1.destroy()
    label2.destroy()
    label3.destroy()
    label4.destroy()


root = Tk()

root.title('Arturo Felipe')
root.resizable(False, False)
root.geometry("1280x720")
root.config(background="purple")
root.iconbitmap("icono.ico")

font = ("Comic Sans MS", 20, "bold")
#Frames
frame1 = Frame(root, bg="darkorchid1")
frame1.place(x=0, y=0, relwidth=0.3, height=root.winfo_height())
frame2 = Frame(frame1, bg="darkorchid")
frame2.place(x=0, y=0, width=root.winfo_width(), relheight=0.15)

#RadioButtons
opcion = StringVar()
opcion.set(None)
Radiobutton(frame1, text="Moto", variable=opcion, value="moto", command=Selec).place(x=5, rely=0.3)
Radiobutton(frame1, text="Carro", variable=opcion, value="carro", command=Selec).place(x=5, rely=0.3+0.05)
Radiobutton(frame1, text="Movilidad Reducida", variable=opcion, value="discapacitado", command=Selec).place(x=5, rely=0.3+0.1)

#Labels
label1 = Label(root, text="Bienvenidos a Parqueadero Popo", font=font)
label1.place(relx=0.5, y=50, height=50)
label2 = Label(root, text="1. Ingrese sus datos.", font=font)
label2.place(relx=0.5, y=110, height=50)
label3 = Label(root, text="2. Se mostrarán los lugares en pantalla.", font=font)
label3.place(relx=0.5, y=170, height=50)
label4 = Label(root, text="3. Escoja su lugar deseado.", font=font)
label4.place(relx=0.5, y=230, height=50)
label5 = Label(frame2, text="PARQUEADERO POPO", font=font)
label5.place(relx=0.035, y=30, height=50)
label6 = Label(frame1, text="Ingrese el tipo de parqueadero\na escoger", font=("Comic Sans MS", 14))
label6.place(x=5, rely=0.2, relwidth=frame1.winfo_width() - 0.03)

btn = Button(frame1, text="Arturo Felipe", bg="green", command=arturoFelipe, activebackground="red")
btn.place(relx=0.4, rely=0.8, width=100, height=50)
root.mainloop()
