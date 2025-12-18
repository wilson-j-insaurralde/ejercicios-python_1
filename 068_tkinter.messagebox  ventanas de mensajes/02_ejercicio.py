"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Diálogos para confirmar o rechazar.
El paquete 'messagebox' cuenta con otra función que nos muestra un diálogo con dos botones con los mensajes "Si" o "No", luego desde nuestro programa podemos identificar cual de los dos botones se ha presionado.

Problema:
Confeccionar un programa que tenga solo un menú de opciones que al ser presionado nos muestre un cuadro de mensaje que informe si queremos finalizar la ejecución del programa. Si se presiona "si" se finaliza el programa en caso contrario no se hace nada.
"""

import tkinter as tk 

from tkinter import messagebox as mb
import sys

class aplicacion: 
    def __init__(self):
        self.ventana1=tk.Tk()
        self.agregar_menu()
        self.ventana1.mainloop()
    def agregar_menu(self):
        self.menubar1=tk.Menu(self.ventana1)
        self.ventana1.config(menu=self.menubar1)
        self.opciones1=tk.Menu(self.menubar1,tearoff=0)
        self.opciones1.add_command(label="salir",command=self.salir)
        self.menubar1.add_cascade(label="opciones",menu=self.opciones1)
    def salir(self):
        repuestas=mb.askyesno("Cuidado", "¿Quiere salir del programa?")
        if repuestas==True:
            sys.exit()


aplicacion=aplicacion()