"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Ingresar el nombre de usuario y clave en controles de tipo Entry. Si se ingresa las cadena (usuario: juan, clave="abc123") luego mostrar en el título de la ventana el mensaje "Correcto" en caso contrario mostrar el mensaje "Incorrecto". Utilizar Widget del módulo ttk.
"""
import tkinter as tk 
from tkinter import ttk

class aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.nombre=tk.StringVar()
        self.clave=tk.StringVar()
        self.label1=ttk.Label(self.ventana1,text="nombre:")
        self.label1.grid(column=0,row=0)
        self.entry1=ttk.Entry(self.ventana1,width=20,textvariable=self.nombre)
        self.entry1.grid(column=1,row=0)
        self.label2=ttk.Label(self.ventana1,text="contraseña")
        self.label2.grid(column=0,row=1)

        self.entry2=ttk.Entry(self.ventana1,width=20,textvariable=self.clave,show="*")
        self.entry2.grid(column=1,row=1)
        self.boton1=ttk.Button(self.ventana1,text="aceptar",command=self.verificar_usuario)
        self.boton1.grid(column=1,row=2)

        self.ventana1.mainloop()
    def verificar_usuario(self):
        nombre=self.nombre.get()
        clave=self.clave.get()
        if nombre == "juan" and clave=="abc123":
            self.ventana1.title("correcto")
        else:
            self.ventana1.title("incorrecto")
aplicacion=aplicacion()