"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Mediante dos controles de tipo Entry permitir el ingreso de dos números. Crear un menú que contenga una opción que cambie el tamaño de la ventana con los valores ingresados por teclado. Finalmente disponer otra opción que finalice el programa
"""


import tkinter as tk 
import sys

class aplicacion: 
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(self.ventana1, text="ingrese el largo: ")
        self.label1.grid(column=0,row=0)
        self.label2=tk.Label(self.ventana1,text="ingrese el ancho")
        self.label2.grid(column=0,row=1)
        self.largo=tk.IntVar()
        self.entry1=tk.Entry(self.ventana1,width=20,textvariable=self.largo)
        self.entry1.grid(column=1,row=0)
        self.ancho=tk.IntVar()
        self.entry2=tk.Entry(self.ventana1,width=20,textvariable=self.ancho)
        self.entry2.grid(column=1,row=1)
        menubar1=tk.Menu(self.ventana1)
        self.ventana1.configure(menu=menubar1)
        opciones=tk.Menu(menubar1)
        opciones.add_command(label="cambiar tamaño",command=self.cambiartamaño)
        opciones.add_command(label="finalizar",command=self.finalizar)
        menubar1.add_cascade(label="opciones",menu=opciones)

        self.ventana1.mainloop()
    def cambiartamaño(self):
        largo=self.largo.get()
        ancho=self.ancho.get()
        self.ventana1.geometry(f"{largo}x{ancho}")
    def finalizar(self):
        sys.exit()


aplicacion=aplicacion()