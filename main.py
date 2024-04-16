from Ventana import MainFrame
from tkinter import Tk

def main():
    root = Tk()
    root.wm_title("Parqueadero Popo")
    root.geometry("1280x720")
    root.resizable(False, False)
    root.iconbitmap("icono.ico")
    app = MainFrame(root)
    app.mainloop()

if __name__=="__main__":
    main()