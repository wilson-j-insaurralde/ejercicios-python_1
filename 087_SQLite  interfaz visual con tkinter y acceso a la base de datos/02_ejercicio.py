
"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""Agregar dos pestañas al programa de administración de artículos que permitan borrar un artículo ingresando su código y otra opción que permita consultar y modificar la descripción y precio de un artículo."""

import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox as mb 
from tkinter import scrolledtext as st
import articulo2

class aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        articulo=articulo2.articuloss()
        self.cuaderno1=ttk.Notebook(self.ventana1)
        self.carga_de_articulos()
        self.consulta_por_codigo()
        self.listado_completo()
        self.borrado_de_articulos()
        self.modificar_articulos()
        self.cuaderno1.grid(column=0,row=0,padx=10,pady=10)
        self.ventana1.mainloop()
    def carga_de_articulos(self):
        self.pagina1=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1,text="carga de articulos")
        self.labelframe1=ttk.LabelFrame(self.pagina1,text="articulos")
        self.labelframe1.grid(column=0,row=0,padx=10,pady=10)
        self.label1=ttk.Label(self.labelframe1,text="descripcion")
        self.label1.grid(column=0,row=0,padx=4,pady=4)
        self.descripcion_carga=tk.StringVar()
        self.entry1=ttk.Entry(self.labelframe1,width=20,textvariable=self.descripcion_carga)
        self.entry1.grid(column=1,row=0,padx=4,pady=4)
        self.label2=ttk.Label(self.labelframe1,text="precio")
        self.label2.grid(column=0,row=1,padx=4,pady=4)
        self.precio_carga=tk.StringVar()
        self.entry2=ttk.Entry(self.labelframe1,width=20,textvariable=self.precio_carga)
        self.entry2.grid(column=1,row=1,padx=4,pady=4)
        self.boton1=ttk.Button(self.labelframe1,text="confirmar",command=self.carga)
        self.boton1.grid(column=1,row=2,padx=4,pady=4)
    def carga(self):
        pass

    def consulta_por_codigo(self):
        self.pagina2=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2,text="consultar por codigo")
        self.labelframe2=ttk.LabelFrame(self.pagina2,text="articulos")
        self.labelframe2.grid(column=0,row=0,padx=10,pady=10)
        self.label3=ttk.Label(self.labelframe2,text="codigo")
        self.label3.grid(column=0,row=0,padx=4,pady=4)
        self.codigo_consulta=tk.StringVar()
        self.entry3=ttk.Entry(self.labelframe2,width=20,textvariable=self.codigo_consulta)
        self.entry3.grid(column=1,row=0,padx=4,pady=4)
        self.label4=ttk.Label(self.labelframe2,text="descripcion")
        self.label4.grid(column=0,row=1,padx=4,pady=4)
        self.descripcion_consulta=tk.StringVar()
        self.entry4=ttk.Entry(self.labelframe2,width=20,textvariable=self.descripcion_consulta)
        self.entry4.grid(column=1,row=1,padx=4,pady=4)
        self.label5=ttk.Label(self.labelframe2,text="precio")
        self.label5.grid(column=0,row=2,padx=4,pady=4)
        self.precio_consulta=tk.StringVar()
        self.entry5=ttk.Entry(self.labelframe2,width=20,textvariable=self.precio_consulta)
        self.entry5.grid(column=1,row=2,padx=4,pady=4)
        self.boton2=ttk.Button(self.labelframe2,text="consultar",command=self.consulta)
        self.boton2.grid(column=1,row=3,padx=4,pady=4)
    def consulta(self):
        pass

    def listado_completo(self):
        self.pagina3=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3,text="listado completo")
        self.labelframe3=ttk.LabelFrame(self.pagina3,text="articulos")
        self.labelframe3.grid(column=0,row=0,padx=4,pady=4)
        self.boton3=ttk.Button(self.labelframe3,text="listado completo",command=self.listar)
        self.boton3.grid(column=0,row=0,padx=4,pady=4)
        self.scrolledtext=st.ScrolledText(self.labelframe3,width=30,height=20)
        self.scrolledtext.grid(column=0,row=1,padx=10,pady=10)
    def listar(self):
        pass
    def borrado_de_articulos(self):
        self.pagina4=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4,text="borrado de articulo")
        self.labelframe4=ttk.LabelFrame(self.pagina4,text="articulo")
        self.labelframe4.grid(column=0,row=0,padx=10,pady=10)
        self.label6=ttk.Label(self.labelframe4,text="codigo")
        self.label6.grid(column=0,row=0,padx=4,pady=4)
        self.codigo_borrar=tk.StringVar()
        self.entry6=ttk.Entry(self.labelframe4,width=20,textvariable=self.codigo_borrar)
        self.entry6.grid(column=1,row=0,padx=4,pady=4)
        self.boton4=ttk.Button(self.labelframe4,text="borrar",command=self.borrar)
        self.boton4.grid(column=1,row=1,padx=4,pady=4)
    def borrar(self):
        pass
    def modificar_articulos(self):
        self.pagina5=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5,text="modificar articulos")
        self.labelframe5=ttk.LabelFrame(self.pagina5,text="articulo")
        self.labelframe5.grid(column=0,row=0,padx=10,pady=10)
        self.label7=ttk.Label(self.labelframe5,text="codigo")
        self.label7.grid(column=0,row=0,padx=4,pady=4)
        self.codigo_modificar=tk.StringVar()
        self.entry7=ttk.Entry(self.labelframe5,width=20,textvariable=self.codigo_modificar)
        self.entry7.grid(column=1,row=0,padx=4,pady=4)
        self.label8=ttk.Label(self.labelframe5,text="descripcion")
        self.label8.grid(column=0,row=1,padx=4,pady=4)
        self.descripcion_modificar=tk.StringVar()
        self.entry8=ttk.Entry(self.labelframe5,width=20,textvariable=self.descripcion_modificar)
        self.entry8.grid(column=1,row=1,padx=4,pady=4)
        self.label9=ttk.Label(self.labelframe5,text="precio")
        self.label9.grid(column=0,row=2,padx=4,pady=4)
        self.precio_modificar=tk.StringVar()
        self.entry9=ttk.Entry(self.labelframe5,width=20,textvariable=self.precio_modificar)
        self.entry9.grid(column=1,row=2,padx=4,pady=4)
        self.boton5=ttk.Button(self.labelframe5,text="consultar",command=self.conulta_modificar)
        self.boton5.grid(column=0,row=3,padx=4,pady=4)
        self.boton6=ttk.Button(self.labelframe5,text="modificar",command=self.modificar_tuki)
        self.boton6.grid(column=1,row=3,padx=4,pady=4)
    def conulta_modificar(self):
        pass
    def modificar_tuki(self):
        pass
        

aplicatuki=aplicacion()
        