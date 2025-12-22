"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""
"""
Confeccionar un programa que cree un objeto de la clase Canvas y luego dibuje una línea, un réctángulo y un óvalo, almacenar el Id de cada dibujo en un atributo.
Crear también 3 cuadrados y definir el parámetro tag con el mismo valor para cada uno de ellos.

Mediante cinco botones permitir: borrar la línea, borrar el rectángulo, borrar el óvalo, borrar todos los cuadrados y borrar todas las figuras contenidas en el objeto Canvas.
"""
import tkinter as tk 
from tkinter import ttk 

class aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.crear_botones()
        self.canvas1=tk.Canvas(self.ventana1,width=600,height=400,background="black")
        self.canvas1.grid(column=0,row=1)
        self.linea1=self.canvas1.create_line(0,0,100,50,fill="white")
        self.rectangulo=self.canvas1.create_rectangle(150,10,300,110,fill="white")
        self.ovalo=self.canvas1.create_oval(400,10,500,150,fill="red")
        self.canvas1.create_rectangle(100,300,150,350,fill="#aaaaaa",tag="cuadrado")
        self.canvas1.create_rectangle(200,300,250,350,fill="#555555",tag="cuadrado")
        self.canvas1.create_rectangle(300,300,350,350,fill="#cccccc",tag="cuadrado")
        self.canvas1.mainloop()

    def crear_botones(self):
        self.labelframe=ttk.LabelFrame(self.ventana1,text="opciones")
        self.labelframe.grid(column=0,row=0,sticky="w",padx=5,pady=5)
        self.boton1=ttk.Button(self.labelframe,text="borrar linea",command=self.borrar_linea)
        self.boton1.grid(column=0,row=0,padx=5,pady=5)
        self.boton2=ttk.Button(self.labelframe,text="borrar rectangulo",command=self.borrar_rectangulo)
        self.boton2.grid(column=1,row=0,padx=5,pady=5)
        self.boton3=ttk.Button(self.labelframe,text="borrar ovalo",command=self.borrar_ovalo)
        self.boton3.grid(column=2,row=0,padx=5,pady=5)
        self.boton4=ttk.Button(self.labelframe,text="borrar todos los cuadrados",command=self.borrar_cuadrados)
        self.boton4.grid(column=3,row=0,padx=5,pady=5)
        self.boton5=ttk.Button(self.labelframe,text="borrar todos",command=self.borrar_todos)
        self.boton5.grid(column=4,row=0,padx=5,pady=5)
    def borrar_linea(self):
        self.canvas1.delete(self.linea1)
    def borrar_rectangulo (self):
        self.canvas1.delete(self.rectangulo)
    def borrar_ovalo(self):
        self.canvas1.delete(self.ovalo)
    def borrar_cuadrados(self):
        self.canvas1.delete("cuadrado")
    def borrar_todos(self):
        self.canvas1.delete(tk.ALL)

aplicacion=aplicacion()