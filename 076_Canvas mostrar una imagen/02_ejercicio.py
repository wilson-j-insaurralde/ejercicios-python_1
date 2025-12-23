"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Disponer un botón y mostrar al azar una de las tres cartas del problema anterior. Cada vez que se presione el botón generar un valor aleatorio y a partir de dicho valor mostrar una carta.
"""
import tkinter as tk 
from tkinter import ttk
import random

class aplicacion():
    def __init__(self):
        self.ventana1=tk.Tk()
        self.boton=ttk.Button(self.ventana1,text="sortear",command=self.sortear)
        self.boton.grid(column=0,row=0)
        self.canvas1=tk.Canvas(self.ventana1,height=600,width=900,background="black")
        self.canvas1.grid(column=0,row=1)
        self.archi1=tk.PhotoImage(file="076_Canvas mostrar una imagen/imagenes/carta1.png")
        self.archi2=tk.PhotoImage(file="076_Canvas mostrar una imagen/imagenes/carta2.png")
        self.archi3=tk.PhotoImage(file="076_Canvas mostrar una imagen/imagenes/carta3.png")
        self.canvas1.create_image(50, 100, image=self.archi1, anchor="nw")


        self.ventana1.mainloop()
    
    def sortear(self): 
        valor=random.randint(1,3)
        if valor==1:
           self.canvas1.create_image(50, 100, image=self.archi1, anchor="nw")
        if valor==2:
           self.canvas1.create_image(50, 100, image=self.archi2, anchor="nw")
        if valor==3:
            self.canvas1.create_image(50, 100, image=self.archi3, anchor="nw")


aplicacion1=aplicacion()