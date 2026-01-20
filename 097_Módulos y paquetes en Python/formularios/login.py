"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Desarrollar una aplicación visual que muestre dos botones. Al presionar el primero mostrar otra ventana para el login, y al presionar el segundo mostrar una ventana de mensajes.

Crear un paquete llamado 'formularios' que contenga en su interior dos módulos llamados 'login.py' y 'mensaje.py'.

La aplicación principal llamarla 'principal.py'

Debemos crear una carpeta llamada 'formularios' y en su interior tres archivos: 'login.py', 'mensaje.py' y '__init__.py'.

El archivo '__init__.py' generalmente se encuentra vacío y tiene por objetivo indicar al intérprete de Python que dicha carpeta es un paquete.
"""

import tkinter as tk 

from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.labelframe=ttk.LabelFrame(self.ventana1,text="login")
        self.labelframe.grid(column=0,row=0,padx=5,pady=10)
        self.login()
    def login(self):
        self.label1=ttk.Label(self.labelframe,text="Nombre de usuario:")
        self.label1.grid(column=0,row=0,padx=4,pady=4)
        self.entry1=ttk.Entry(self.labelframe)
        self.entry1.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe, text="Ingrese clave:")    
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.entry2=ttk.Entry(self.labelframe, show="*")
        self.entry2.grid(column=1, row=1, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe, text="Ingresar",command=self.ingresar)
        self.boton1.grid(column=1, row=2, padx=4, pady=4)
    def ingresar(self):
        self.ventana1.destroy()


def mostrar():
    aplicacion1=Aplicacion()