"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

import tkinter as tk 

class aplicacion: 
    def __init__(self):
        self.ventana1=tk.Tk()
        menubar1=tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1=tk.Menu(menubar1,tearoff=0)
        opciones1.add_command(label="rojo",command=self.fijarrojo,accelerator="CtrlL+R")
        opciones1.add_command(label="verde",command=self.fijarverde,accelerator="Ctrl+V")
       
        opciones1.add_separator()
        opciones1.add_command(label="azul",command=self.fijarazul,accelerator="Ctrl+A")
        self.ventana1.bind_all("<Control-r>",self.cambiar)
        self.ventana1.bind_all("<Control-v>",self.cambiar)
        self.ventana1.bind_all("<Control-a>",self.cambiar)
        menubar1.add_cascade(label="colores",menu=opciones1)
        opciones2=tk.Menu(menubar1)
        opciones2.add_command(label="640x480", command=self.ventanachica)
        opciones2.add_command(label="1080x800",command=self.ventanagrande)
        menubar1.add_cascade(label="tamaños", menu=opciones2)
        self.ventana1.mainloop()

    def cambiar(self,event):
        if event.keysym=="r":
            self.fijarrojo()
        if event.keysym=="v":
            self.fijarverde()
        if event.keysym=="a":
            self.fijarazul()
    def fijarrojo(self):
        self.ventana1.configure(background="red")
    def fijarverde(self):
        self.ventana1.configure(background="green")
    def fijarazul(self):
        self.ventana1.configure(background="blue")
    def ventanachica(self):
        self.ventana1.geometry("640x480")
    def ventanagrande(self):
        self.ventana1.geometry("1080x800")

aplicacion=aplicacion()