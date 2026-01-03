"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Problema:
Desarrollar una aplicación visual con la librería tkinter que permita implementar los algoritmos de carga de artículos, consulta por código y listado completo.
"""

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox as mb 
from tkinter import scrolledtext as st
import articulos

class FormularioArticulos():
    def __init__(self):
        self.articulo1=articulos.Articulos()
        self.ventana1=tk.Tk()
        self.ventana1.title("mantenimiento de articulos")
        self.cuaderno1=ttk.Notebook(self.ventana1)
        self.cargar_articulos1()
        self.consultar_por_codigo2()
        self.lista_completo3()
        self.cuaderno1.grid(column=0,row=0,padx=10,pady=10)
        self.ventana1.mainloop()
    def cargar_articulos1(self):
        self.pagina1=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1,text="carga de articulos")
        self.labelframe1=ttk.LabelFrame(self.pagina1,text="articulos")
        self.labelframe1.grid(column=0,row=0,padx=10,pady=10)
        self.label1=ttk.Label(self.labelframe1,text="descripcion:")
        self.label1.grid(column=0,row=0,padx=4,pady=4)
        self.descripcioncarga=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe1,width=20,textvariable=self.descripcioncarga)
        self.entrydescripcion.grid(column=1,row=0,padx=4,pady=4)
        self.label2=ttk.Label(self.labelframe1,text="precio:")
        self.label2.grid(column=0,row=1,padx=4,pady=4)
        self.preciocarga=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1,width=20,textvariable=self.preciocarga)
        self.entryprecio.grid(column=1,row=1,padx=4,pady=4)
        self.boton1=ttk.Button(self.labelframe1,text="confirmar",command=self.agregar)
        self.boton1.grid(column=1,row=2,padx=4,pady=4)
    def agregar(self):
        datos=(self.descripcioncarga.get(),self.preciocarga.get())
        self.articulo1.alta(datos)
        mb.showinfo("informacion","los datos fueron cargados")
        self.descripcioncarga.set("")
        self.preciocarga.set("")


    def consultar_por_codigo2(self):
        self.pagina2=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2,text="consulta por codigo")
        self.labelframe2=ttk.LabelFrame(self.pagina2,text="articulo")
        self.labelframe2.grid(column=0,row=0,padx=10,pady=10)
        self.label3=ttk.Label(self.labelframe2,text="codigo")
        self.label3.grid(column=0,row=0,padx=4,pady=4)
        self.codigocarga=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe2,width=20,textvariable=self.codigocarga)
        self.entrycodigo.grid(column=1,row=0,padx=4,pady=4)
        self.label4=ttk.Label(self.labelframe2,text="descripcion")
        self.label4.grid(column=0,row=1,padx=4,pady=4)
        self.descripcioncarga2=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe2,width=20,textvariable=self.descripcioncarga2)
        self.entrydescripcion.grid(column=1,row=1,padx=4,pady=4)
        self.label5=ttk.Label(self.labelframe2,text="precio")
        self.label5.grid(column=0,row=2,padx=4,pady=4)
        self.preciocarga2=tk.StringVar()
        self.entryprecio2=ttk.Entry(self.labelframe2,width=20,textvariable=self.preciocarga2)
        self.entryprecio2.grid(column=1,row=2,padx=4,pady=4)
        self.boton2=ttk.Button(self.labelframe2,text="consultar",command=self.consultar)
        self.boton2.grid(column=1,row=3,padx=4,pady=4)

    def consultar(self):
        datos=(self.codigocarga.get(),)
        repuesta=self.articulo1.consulta(datos)
        if len(repuesta)>0:
            self.descripcioncarga2.set(repuesta[0][0])
            self.preciocarga2.set(repuesta[0][1])
        else:
            self.descripcioncarga2.set("")
            self.preciocarga2.set("")
            mb.showinfo("informacion","no existe un articulo con dicho codigo")


    def lista_completo3(self):
        self.pagina3=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3,text="listado completo")
        self.labelframe3=ttk.LabelFrame(self.pagina3,text="articulo")
        self.labelframe3.grid(column=0,row=0,padx=10,pady=10)
        self.boton3=ttk.Button(self.labelframe3,text="listado completo",command=self.listado)
        self.boton3.grid(column=0,row=0,padx=4,pady=4)
        self.scrolledtex1=st.ScrolledText(self.labelframe3,width=30,height=10)
        self.scrolledtex1.grid(column=0,row=1,padx=10,pady=10)

    def listado(self):
        respuestas=self.articulo1.recuperar_todos()
        self.scrolledtex1.delete("1.0",tk.END)
        for fila in respuestas:
            self.scrolledtex1.insert(tk.END,"código:"+str(fila[0])+"\ndescripción:"+fila[1]+"\nprecio:"+str(fila[2])+"\n\n")



formularioarticulos=FormularioArticulos()