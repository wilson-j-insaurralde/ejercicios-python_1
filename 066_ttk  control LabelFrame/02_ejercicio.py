"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Mediante dos controles de tipo LabelFrame implementar la siguiente interfaz visual:
articulo:
    codigo de articulo : 
    descripcion:
    precio:
operaciones:
    ALTA     BAJA    MODIFICACION
"""

import tkinter as tk 
from tkinter import ttk 

class aplicacion :
    def __init__(self):
        self.ventana1=tk.Tk()
        self.estilo = ttk.Style()
        self.estilo.configure("TLabelframe.Label", foreground="blue", font=("Arial", 10, "bold"))
        self.labelframe1=ttk.Labelframe(self.ventana1,text="Articulo:")
        self.labelframe1.grid(column=0,row=0,padx=5,pady=10)
        self.articulo()
        self.labelframe2=ttk.Labelframe(self.ventana1,text="Operaciones:")
        self.labelframe2.grid(column=0,row=1,padx=5,pady=10)
        self.operaciones()
        self.ventana1.mainloop()

    def articulo(self):
        self.label1=ttk.Label(self.labelframe1,text="codigo de articulo:")
        self.label1.grid(column=0,row=0,padx=4,pady=4)
        self.entry1=ttk.Entry(self.labelframe1)
        self.entry1.grid(column=1,row=0,padx=4,pady=4)
        self.label2=ttk.Label(self.labelframe1,text="descripcion:")
        self.label2.grid(column=0,row=1,padx=4,pady=4)
        self.entry2=ttk.Entry(self.labelframe1)
        self.entry2.grid(column=1,row=1,padx=4,pady=4)
        self.label3=ttk.Label(self.labelframe1,text="precio:")
        self.label3.grid(column=0,row=2,padx=4,pady=4)
        self.entry3=ttk.Entry(self.labelframe1)
        self.entry3.grid(column=1,row=2,padx=4,pady=4)
    def operaciones(self):
        self.boton1=ttk.Button(self.labelframe2,text="alta")
        self.boton1.grid(column=0,row=0,padx=4,pady=4)
        self.boton12=ttk.Button(self.labelframe2,text="baja")
        self.boton12.grid(column=1,row=0,padx=4,pady=4)
        self.boton3=ttk.Button(self.labelframe2,text="modificacion")
        self.boton3.grid(column=2,row=0,padx=4,pady=4)

aplicacion=aplicacion()