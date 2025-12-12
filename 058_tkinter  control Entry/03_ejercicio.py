"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Confeccionar un programa que permita ingresar dos números en controles de tipo Entry, luego sumar los dos valores ingresados y mostrar la suma en una Label al presionar un botón.
"""
import tkinter as tk

class suma():
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(self.ventana1, text="ingrese el primer numero: ")
        self.label1.grid(column=0,row=0)
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1,width=20,textvariable=self.dato1)
        self.entry1.grid(column=1,row=0 )
        self.label2=tk.Label(self.ventana1,text="ingrese el segundo numero: ")
        self.label2.grid(column=0,row=1)
        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1, width=20, textvariable=self.dato2)
        self.entry2.grid(column=1,row=1)
        self.boton1=tk.Button(self.ventana1,text="sumar",command=self.sumarlosdos)
        self.boton1.grid(column=1,row=2)
        self.label3=tk.Label(self.ventana1,text="resultado")
        self.label3.grid(column=1,row=3)
        self.ventana1.mainloop()
    def sumarlosdos(self):
        suma=int(self.dato2.get())+int(self.dato1.get())
        self.label3.configure(text=suma)

suma=suma()