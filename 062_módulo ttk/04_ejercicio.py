"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Mostrar una ventana y en su interior tres controles de tipo Checkbutton cuyas etiquetas correspondan a distintos lenguajes de programación. Cuando se presione un botón mostrar en una Label la cantidad de Checkbutton que se encuentran chequeados. Utilizar Widget del módulo ttk.
"""
import tkinter as tk 
from tkinter import ttk 

class aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()

        self.variable1=tk.IntVar()
        self.check1=ttk.Checkbutton(self.ventana1,text="python",variable=self.variable1)
        self.check1.grid(column=0,row=0)

        self.variable2=tk.IntVar()
        self.check2=ttk.Checkbutton(self.ventana1,text="java",variable=self.variable2)
        self.check2.grid(column=0,row=1)

        self.variable3=tk.IntVar()
        self.check3=ttk.Checkbutton(self.ventana1,text="C",variable=self.variable3)
        self.check3.grid(column=0,row=2)

        self.boton1=ttk.Button(self.ventana1,text="aceptar",command=self.cuantos)
        self.boton1.grid(column=0,row=3)
        self.label1=ttk.Label(self.ventana1,text="seleccion")
        self.label1.grid(column=0,row=4)

        self.ventana1.mainloop()
    def cuantos(self):
        cant=0
        if self.variable1.get()==1:
            cant+=1
        if self.variable2.get()==1:
            cant+=1
        if self.variable3.get()==1:
            cant+=1
        self.label1.configure(text="cantidad:"+str(cant))
aplicacion=aplicacion()