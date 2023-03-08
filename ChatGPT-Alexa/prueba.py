from tkinter import *
raiz=Tk()
raiz.title("Ventana de prueba")
raiz.geometry("500x500")

miFrame=Frame()

miFrame.pack(fill='both',expand="True")
miFrame.config(bg="red",width="500",height="500")

raiz.config(bg="blue")

raiz.mainloop()