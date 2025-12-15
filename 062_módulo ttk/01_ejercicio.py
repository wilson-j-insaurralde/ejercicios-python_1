"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Mostrar una ventana y en su interior dos botones y una label utilizando el módulo ttk. La label muestra inicialmente el valor 1. Cada uno de los botones permiten incrementar o decrementar en uno el contenido de la label
"""

import tkinter as tk 
from tkinter import ttk

class aplicacion:   
    def __init__(self):
        self.ventana1=tk.Tk()
        self.dato=1
        self.ventana1.title("botonoes button y label")
        self.label1=ttk.Label(self.ventana1,text=self.dato)
        self.label1.grid(column=0,row=0)
        self.label1.configure(foreground="red")

        self.boton1=ttk.Button(self.ventana1,text="incrementar",command=self.incrementar)
        self.boton1.grid(column=0,row=1)
        self.boton2=ttk.Button(self.ventana1,text="decrementar",command=self.decrementar)
        self.boton2.grid(column=0,row=2)

        self.ventana1.mainloop()
    def incrementar(self):
        self.dato=self.dato+1
        self.label1.configure(text=self.dato)
        

    def decrementar(self):
        self.dato=self.dato-1
        self.label1.configure(text=self.dato)

aplicacion=aplicacion()