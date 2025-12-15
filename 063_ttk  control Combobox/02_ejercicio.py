"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Solicitar el ingreso del nombre de una persona y seleccionar de un control Combobox un país. Al presionar un botón mostrar en la barra de la ventana el nombre ingresado y el país seleccionado.
"""
import tkinter as tk
from tkinter import ttk
 
class aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.nombre=tk.StringVar()
        self.label1=ttk.Label(self.ventana1,text="ingrese su nombre")
        self.label1.grid(column=0,row=0)
        self.entry1=ttk.Entry(self.ventana1,width=20,textvariable=self.nombre)
        self.entry1.grid(column=1,row=0)
        self.label2=ttk.Label(self.ventana1,text="seleccione su pais: ")
        self.label2.grid(column=0,row=1)
        self.seleccion=tk.StringVar()
        paises=("argentina","peru","brazil","chile","paraguay","uruguay","bolivia")
        self.controlbox1=ttk.Combobox(self.ventana1,width=20,textvariable=self.seleccion,values=paises, state='readonly')
        self.controlbox1.current(0)
        self.controlbox1.grid(column=1,row=1)
        self.boton1=ttk.Button(self.ventana1,text="aceptar",command=self.colocar)
        self.boton1.grid(column=1,row=2)


        self.ventana1.mainloop()
    def colocar(self):
        pais=str(self.seleccion.get())
        nombre=str(self.nombre.get())
        self.ventana1.title(f"nombre:{nombre}---pais:{pais}")

aplicacion=aplicacion()