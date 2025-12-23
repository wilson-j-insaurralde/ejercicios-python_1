"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""Crear 100 cuadrados de color rojo y disponerlos en el control Canvas en posiciones aleatorias. Permitir desplazar con el mouse cualquiera de los cuadrados."""

import tkinter as tk
from tkinter import ttk
import random
class aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.canvas1=tk.Canvas(self.ventana1,width=900,height=600,background="black")
        self.canvas1.grid(column=0,row=1)
        #self.cuadrado=self.canvas1.create_rectangle(150,10,200,60, fill="red")
        self.boton1=ttk.Button(self.ventana1,text="generar",command=self.generar_rectangulo)
        self.boton1.grid(column=0,row=0)
        self.canvas1.tag_bind("move","<ButtonPress-1>",self.presion_boton)
        self.canvas1.tag_bind("move","<Button1-Motion>",self.mover)
        self.cuadrado_seleccionado=None
        self.ventana1.mainloop()
    def generar_rectangulo(self):
        bandera=0
        while bandera!=100:
            x1=random.randint(0,900)
            y1=random.randint(0,600)
            x2=x1+50
            y2=y1+50
            self.cuadrado=self.canvas1.create_rectangle(x1,y1,x2,y2, fill="red",tags="move")

            bandera=bandera+1
    def presion_boton(self,evento):
        cuadrado=self.canvas1.find_withtag(tk.CURRENT)
        self.cuadrado_seleccionado=(cuadrado,evento.x,evento.y)
    def mover(self,evento):
        x,y=evento.x,evento.y
        cuadrado,x1,y1=self.cuadrado_seleccionado
        self.canvas1.move(cuadrado,x-x1,y-y1)
        self.cuadrado_seleccionado= (cuadrado, x, y)
aplicacion=aplicacion()
