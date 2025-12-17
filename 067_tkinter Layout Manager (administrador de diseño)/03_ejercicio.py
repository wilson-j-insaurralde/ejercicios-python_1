"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""
"""
Layout Manager: Place
Este tipo de Layout Manager nos permite disponer un Widget en una posición y con un tamaño con valor absoluto a nivel de píxeles. Hay que tener cuidado en que casos utilizar este tipo de administrador de diseños ya que si agrandamos o reducimos el tamaño de la ventana puede ser que los controles queden fuera de la ventana y el operador no pueda visualizarlos.

Problema:
Disponer dos botones en la parte inferior derecha de la ventana utilizando el Layout Manager de tipo Place. El ancho y alto de la ventana debe ser de 800 por 600 píxeles.
"""
import tkinter as tk 
from tkinter import ttk

class aplicacion: 
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.geometry("800x600")
        self.ventana1.resizable(0,0)
        self.boton1=ttk.Button(self.ventana1,text="Confirmar")
        self.boton1.place(x=680, y=550, width=90, height=30)
        self.boton2=ttk.Button(self.ventana1, text="Cancelar")
        self.boton2.place(x=580, y=550, width=90, height=30)
        self.ventana1.mainloop()

aplicacion=aplicacion()