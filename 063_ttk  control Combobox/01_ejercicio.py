"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""
"""
Mostrar en una ventana un control de tipo Combobox con los días de la semana. Cuando se presione un botón actualizar una Label con el día seleccionado.
"""

import tkinter as tk 
from tkinter import ttk 

class aplicacion: 
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=ttk.Label(self.ventana1, text="seleccione un dia de la semana: ")
        self.label1.grid(column=0,row=0)
        self.opcion=tk.StringVar()
        diassemana=("Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo")
        self.combox1=ttk.Combobox(self.ventana1,width=10,textvariable=self.opcion,values=diassemana,state='readonly')
        self.combox1.current(0)
        self.combox1.grid(column=0,row=1)
        self.boton1=ttk.Button(self.ventana1,text="recuperar",command=self.recuperar)
        self.boton1.grid(column=0,row=2)
        self.label2=ttk.Label(self.ventana1,text="dia seleccionado")
        self.label2.grid(column=0,row=3)
        self.ventana1.mainloop()

    def recuperar(self):
        self.label2.config(text=self.opcion.get())
        
aplicacion=aplicacion()        