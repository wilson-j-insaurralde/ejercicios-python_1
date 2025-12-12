"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Mostrar una ventana y que en su título aparezca el mensaje 'Hola Mundo'.

El programa en Python haciendo uso del módulo 'tkinter' requiere el siguiente algoritmo:

"""

import tkinter as tk 
ventana1=tk.Tk()
ventana1.title("hola mundo")
ventana1.mainloop()
"""
El programa anterior modificado con POO queda:
"""
class aplicacion:
    def __init__(self):
        self.ventana=tk.Tk()
        self.ventana.title("hola mundo")
        self.ventana.mainloop()

aplicacion1=aplicacion()
aplicacion2=aplicacion()