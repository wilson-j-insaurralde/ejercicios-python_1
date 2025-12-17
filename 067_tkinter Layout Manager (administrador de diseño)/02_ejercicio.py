"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""
"""
Disponer una serie de botones utilizando el Layout Manager de tipo Grid.
"""

import tkinter as tk 
from tkinter import ttk 

class aplicacion: 
    def __init__(self):
        self.ventana1=tk.Tk()
        self.boton1=ttk.Button(self.ventana1,text="boton 1")
        self.boton1.grid(column=0,row=0)
        self.boton2=ttk.Button(self.ventana1,text="boton 2")
        self.boton2.grid(column=1,row=0)
        self.boton3=ttk.Button(self.ventana1,text="boton 3")
        self.boton3.grid(column=2,row=0,rowspan=2,sticky="ns")
        self.boton4=ttk.Button(self.ventana1,text="boton 4")
        self.boton4.grid(column=0,row=1)
        self.boton5=ttk.Button(self.ventana1,text="boton 5")
        self.boton5.grid(column=1,row=1)
        self.boton6=ttk.Button(self.ventana1,text="boton 6")
        self.boton6.grid(column=0,row=2,columnspan=3, sticky="we")
        self.ventana1.mainloop()

aplicacion=aplicacion()