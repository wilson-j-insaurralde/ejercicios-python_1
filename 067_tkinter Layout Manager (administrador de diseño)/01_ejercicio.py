"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""
"""
Layout Manager: Pack
Veamos con un ejemplo como se ubican los Widget utilizando Pack.

Problema:
Disponer una serie de botones utilizando el Layout Manager de tipo Pack.
"""
import tkinter as tk 
from tkinter import ttk 

class aplicacion: 
    def __init__(self):
        self.ventana1=tk.Tk()
        self.boton1=ttk.Button(self.ventana1,text="boton 1")
        self.boton1.pack(side=tk.TOP,fill=tk.BOTH)
        self.boton2=ttk.Button(self.ventana1,text="boton 2")
        self.boton2.pack(side=tk.TOP,fill=tk.BOTH)
        self.boton3=ttk.Button(self.ventana1,text="boton 3")
        self.boton3.pack(side=tk.TOP,fill=tk.BOTH)
        self.boton4=ttk.Button(self.ventana1,text="boton 4")
        self.boton4.pack(side=tk.LEFT)
        self.boton5=ttk.Button(self.ventana1,text="boton 5")
        self.boton5.pack(side=tk.RIGHT)
        self.boton6=ttk.Button(self.ventana1,text="boton 6")
        self.boton6.pack(side=tk.RIGHT)
        self.boton7=ttk.Button(self.ventana1, text="boton 7")
        self.boton7.pack(side=tk.RIGHT)

        self.ventana1.mainloop()

aplicacion=aplicacion()