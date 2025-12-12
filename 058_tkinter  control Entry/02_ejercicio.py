"""
Confeccionar un programa que permita ingresar el nombre de usuario en un control Entry y cuando se presione un botón mostrar el valor ingresado en la barra de títulos de la ventana.
"""
import tkinter as tk 

class aplicacion1():

    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(self.ventana1,text="ingrese un nombre: ")
        self.label1.grid(column=0,row=0)
        self.dato=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1,width=10,textvariable=self.dato)
        self.entry1.grid(column=0,row=1)
        self.boton1=tk.Button(self.ventana1, text="aceptar", command=self.mostrar)
        self.boton1.grid(column=0,row=2)
        self.ventana1.mainloop()

    def mostrar(self):
        nombre=str(self.dato.get())
        self.ventana1.title(nombre)
    
aplicacion=aplicacion1()