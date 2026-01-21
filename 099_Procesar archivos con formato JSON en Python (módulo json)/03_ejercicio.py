"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""
"""
Confeccionar una aplicación visual con tkinter que permita mostrar todos los artículos. Recuperar del servidor web llamando al recurso 'retornararticulos.php'.

Disponer dos botones para poder navegar entre los distintos registros recuperados.
"""


import tkinter as tk
from tkinter import ttk
from urllib import request
import json


class aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("esta es mi ventana")
        self.label1=ttk.Label(self.ventana1,text="codigo",width=25)
        self.label1.grid(column=0,row=0,padx=10,pady=10)
        self.label2=ttk.Label(self.ventana1,text="",width=25)
        self.label2.grid(column=1,row=0,padx=10,pady=10)

        self.label3=ttk.Label(self.ventana1,text="descripcion",width=25)
        self.label3.grid(column=0,row=1,padx=10,pady=10)
        self.label4=ttk.Label(self.ventana1,text="",width=25)
        self.label4.grid(column=1,row=1,padx=10,pady=10)

        self.label5=ttk.Label(self.ventana1,text="precio",width=25)
        self.label5.grid(column=0,row=2,padx=10,pady=10)
        self.label6=ttk.Label(self.ventana1,text="",width=25)
        self.label6.grid(column=1,row=2,padx=10,pady=10)

        self.boton1=ttk.Button(self.ventana1,text="anterior",command=self.anterior,width=25)
        self.boton1.grid(column=0,row=3,padx=10,pady=10)
        self.boton2=ttk.Button(self.ventana1,text="siguiente",command=self.siguiente,width=25)
        self.boton2.grid(column=1,row=3,padx=10,pady=10)
        self.articulos=[]
        self.recuperar_articulos()
        self.indice=0
        self.mostrar_articulo()
        self.ventana1.mainloop()

    def anterior(self):
        if self.indice>0:
            self.indice-=1
            self.mostrar_articulo()

    def siguiente(self):
        if self.indice<len(self.articulos)-1:
            self.indice+=1
            self.mostrar_articulo()

    def recuperar_articulos(self):
        pagina=request.urlopen("http://localhost/pythonya/retornararticulos.php")
        datos=pagina.read().decode("utf-8")
        self.articulos=json.loads(datos)

    def mostrar_articulo(self):
        if len(self.articulos)>0:
            self.label2.config(text=self.articulos[self.indice]['codigo'])
            self.label4.config(text=self.articulos[self.indice]['descripcion'])
            self.label6.config(text=self.articulos[self.indice]['precio'])

aplicacion=aplicacion()
