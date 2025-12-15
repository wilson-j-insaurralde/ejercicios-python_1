"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Mostrar dos controles de tipo Radiobutton con las etiquetas "Varón" y "Mujer", cuando se presione un botón actualizar una Label con el Radiobutton seleccionado.
"""

import tkinter as tk 
from tkinter import ttk

class aplicacion: 
    def __init__(self):
        self.ventana1=tk.Tk()
        self.seleccion=tk.IntVar()
        self.raid1=ttk.Radiobutton(self.ventana1,text="Varon",variable=self.seleccion,value=1)
        self.raid1.grid(column=0,row=0)
        self.raid2=ttk.Radiobutton(self.ventana1,text="mujer",variable=self.seleccion,value=2)
        self.raid2.grid(column=0,row=1)
        self.boton1=ttk.Button(self.ventana1,text="aceptar",command=self.seleccionr)
        self.boton1.grid(column=0,row=2)
        self.label1=ttk.Label(text="opcion seleccionada: ")
        self.label1.grid(column=0, row=3)
        self.ventana1.mainloop()
    def seleccionr(self):
        if self.seleccion.get()==1:
            self.ventana1.title("varon")
            self.label1.configure(text="opcion seleccionada: varon ")
        if self.seleccion.get()==2:
            self.ventana1.title("mujer")
            self.label1.configure(text="opcion seleccionada: mujer ")
    
aplicacion=aplicacion()