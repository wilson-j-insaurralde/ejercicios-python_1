"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Problema:
Desarrollar una aplicación visual con la librería tkinter que permita implementar los algoritmos de carga de artículos, consulta por código y listado completo.

Seguiremos trabajando con la tabla 'articulos' que creamos en el concepto anterior.

"""


import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import articulos

class aplicacionnashe():
    def __init__(self):
        self.articulo1=articulos.Articulos()
        self.ventana1=tk.Tk()
        self.ventana1.title("articulos")
        self.cuaderno1=ttk.Notebook(self.ventana1)
        self.carga_de_articulos()
        self.consulta_por_codigo()
        self.listado_completo()
        self.cuaderno1.grid(column=0,row=0,padx=10,pady=10)
        self.ventana1.mainloop()

    def carga_de_articulos(self):
        self.pagina1=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1,text="carga de articulos")
        self.labelframe1=ttk.LabelFrame(self.pagina1,text="articulo")
        self.labelframe1.grid(column=0,row=0,padx=10,pady=10)
        self.label1=ttk.Label(self.labelframe1,text="descripcion:")
        self.label1.grid(column=0,row=0,padx=4,pady=4)
        self.descripcion_carga=tk.StringVar()
        self.entry1=ttk.Entry(self.labelframe1,width=20,textvariable=self.descripcion_carga)
        self.entry1.grid(column=1,row=0,padx=4,pady=4)
        self.label2=ttk.Label(self.labelframe1,text="precio:")
        self.label2.grid(column=0,row=1,padx=4,pady=4)
        self.precio_carga=tk.StringVar()
        self.entry2=ttk.Entry(self.labelframe1,width=20,textvariable=self.precio_carga)
        self.entry2.grid(column=1,row=1,padx=4,pady=4)
        self.boton1=ttk.Button(self.labelframe1,text="confirmar",command=self.confirmar_carga)
        self.boton1.grid(column=1,row=2,padx=4,pady=4)

    def confirmar_carga(self):
        datos=(self.descripcion_carga.get(),self.precio_carga.get())
        self.articulo1.alta(datos)
        mb.showinfo("informacion","los datos fueron cargados")
        self.descripcion_carga.set("")
        self.precio_carga.set("")



    def consulta_por_codigo(self):
        self.pagina2=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2,text="consulta por codigo")
        self.labelframe2=ttk.LabelFrame(self.pagina2,text="articulo")
        self.labelframe2.grid(column=0,row=0,padx=10,pady=10)
        self.label3=ttk.Label(self.labelframe2,text="codigo:")
        self.label3.grid(column=0,row=0,padx=4,pady=4)
        self.codigo_consulta=tk.StringVar()
        self.entry3=ttk.Entry(self.labelframe2,width=20,textvariable=self.codigo_consulta)
        self.entry3.grid(column=1,row=0,padx=4,pady=4)
        self.label3=ttk.Label(self.labelframe2,text="descripcion:")
        self.label3.grid(column=0,row=1,padx=4,pady=4)
        self.descripcion_consulta=tk.StringVar()
        self.entry4=ttk.Entry(self.labelframe2,width=20,textvariable=self.descripcion_consulta)
        self.entry4.grid(column=1,row=1,padx=4,pady=4)
        self.label4=ttk.Label(self.labelframe2,text="precio")
        self.label4.grid(column=0,row=2,padx=4,pady=4)
        self.precio_consulta=tk.StringVar()
        self.entry4=ttk.Entry(self.labelframe2,width=20,textvariable=self.precio_consulta)
        self.entry4.grid(column=1,row=2,padx=4,pady=4)
        self.boton2=ttk.Button(self.labelframe2,text="consultar",command=self.consultar)
        self.boton2.grid(column=1,row=3,padx=4,pady=4)

    def consultar(self):
        datos=(self.codigo_consulta.get(),)
        repuesta=self.articulo1.consulta(datos)
        if len(repuesta)>0:
            self.descripcion_consulta.set(repuesta[0][0])
            self.precio_consulta.set(repuesta[0][1])
        else:
            self.descripcion_consulta.set("")
            self.precio_consulta.set("")
            mb.showinfo("informacion","no existe articulo con dicho codigo")


    def listado_completo(self):
        self.pagina3=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3,text="listado completo")
        self.labelframe3=ttk.LabelFrame(self.pagina3,text="articulo")
        self.labelframe3.grid(column=0,row=0,padx=10,pady=10)
        self.boton3=ttk.Button(self.labelframe3,text="listado completo",command=self.listar_completo)
        self.boton3.grid(column=0,row=0,padx=4,pady=4)
        self.scrolledtextlledtext=st.ScrolledText(self.labelframe3,width=30,height=10)
        self.scrolledtextlledtext.grid(column=0,row=1,padx=10,pady=10)


    def listar_completo(self):
        respuestas=self.articulo1.recuperar_todos()
        self.scrolledtextlledtext.delete("1.0",tk.END)
        for fila in respuestas:
            self.scrolledtextlledtext.insert(tk.END,"código:"+str(fila[0])+"\ndescripción:"+fila[1]+"\nprecio:"+str(fila[2])+"\n\n")
            


aplicacion=aplicacionnashe()