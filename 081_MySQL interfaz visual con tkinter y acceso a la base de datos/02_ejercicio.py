"""
Problema propuesto
Agregar dos pestañas al programa de administración de artículos que permitan borrar un artículo ingresando su código y otra opción que permita consultar y modificar la descripción y precio de un artículo.

"""

import tkinter as tk 
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import articulos2

class programapicantenashe:
    def __init__(self):
        self.articulos=articulos2.arcticulos()
        self.ventana1=tk.Tk()
        self.ventana1.title("mantenimiento de articulos")
        self.cuaderno1=ttk.Notebook(self.ventana1)
        self.carga_de_articulos()
        self.consultar_por_codigo()
        self.listado_completo()
        self.borrado_de_articulo()
        self.modificar_articulo()
        self.cuaderno1.grid(column=0,row=0,padx=10,pady=10)
        self.ventana1.mainloop()
    def carga_de_articulos(self):
        self.pagina1=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1,text="carga de articulos")
        self.labelframe1=ttk.LabelFrame(self.pagina1,text="articulos")
        self.labelframe1.grid(column=0,row=0,padx=10,pady=10)
        self.label1=ttk.Label(self.labelframe1,text="descripcion:")
        self.label1.grid(column=0,row=0,padx=4,pady=4)
        self.descripcion_entrada=tk.StringVar()
        self.entry1=ttk.Entry(self.labelframe1,width=20,textvariable=self.descripcion_entrada)
        self.entry1.grid(column=1,row=0,padx=4,pady=4)
        self.label2=ttk.Label(self.labelframe1,text="precio:")
        self.label2.grid(column=0,row=1,padx=4,pady=4)
        self.precio_entrada=tk.StringVar()
        self.entry2=ttk.Entry(self.labelframe1,width=20,textvariable=self.precio_entrada)
        self.entry2.grid(column=1,row=1,padx=4,pady=4)
        self.boton1=ttk.Button(self.labelframe1,text="confirmar",command=self.confirmar)
        self.boton1.grid(column=1,row=2,padx=4,pady=4)
        
    def confirmar(self):
        datos=(self.descripcion_entrada.get(),self.precio_entrada.get())
        self.articulos.alta(datos)
        mb.showinfo("Información", "Los datos fueron cargados")
        self.descripcion_entrada.set("")
        self.precio_entrada.set("")

    def consultar_por_codigo(self):
        self.pagina2=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2,text="consultar por codigo")
        self.labelframe2=ttk.LabelFrame(self.pagina2,text="articulo")
        self.labelframe2.grid(column=0,row=0,padx=10,pady=10)
        self.label3=ttk.Label(self.labelframe2,text="codigo:")
        self.label3.grid(column=0,row=0,padx=4,pady=4)
        self.codigo_articulo=tk.StringVar()
        self.entry3=ttk.Entry(self.labelframe2,width=20,textvariable=self.codigo_articulo)
        self.entry3.grid(column=1,row=0,padx=4,pady=4)
        self.label4=ttk.Label(self.labelframe2,text="descripcion:")
        self.label4.grid(column=0,row=1,padx=4,pady=4)
        self.descripcion_consulta=tk.StringVar()
        self.entry4=ttk.Entry(self.labelframe2,width=20,textvariable=self.descripcion_consulta)
        self.entry4.grid(column=1,row=1,padx=4,pady=4)
        self.label5=ttk.Label(self.labelframe2,text="precio:")
        self.label5.grid(column=0,row=2,padx=4,pady=4)
        self.precio_consulta=tk.StringVar()
        self.entry5=ttk.Entry(self.labelframe2,width=20,textvariable=self.precio_consulta)
        self.entry5.grid(column=1,row=2,padx=4,pady=4)
        self.boton2=ttk.Button(self.labelframe2,text="consultar",command=self.consultar)
        self.boton2.grid(column=1,row=3,padx=4,pady=4)

    def consultar(self):
        datos=(self.codigo_articulo.get(),)
        repuesta=self.articulos.consulta(datos)
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
        self.labelframe3=ttk.Labelframe(self.pagina3,text="articulo")
        self.labelframe3.grid(column=0,row=0,padx=10,pady=10)
        self.boton3=ttk.Button(self.labelframe3,text="listado completo",command=self.listar)
        self.boton3.grid(column=0,row=0,padx=4,pady=4)
        self.scrolledtext=st.ScrolledText(self.labelframe3,width=30,height=10)
        self.scrolledtext.grid(column=0,row=1,padx=10,pady=10)
    def listar(self):
        pass

    def borrado_de_articulo(self):
        self.pagina4=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4,text="borrado de articulos")
        self.labelframe4=ttk.Labelframe(self.pagina4,text="articulos")
        self.labelframe4.grid(column=0,row=0,padx=10,pady=10)
        self.label6=ttk.Label(self.labelframe4,text="codigo: ")
        self.label6.grid(column=0,row=0,padx=4,pady=4)
        self.codigo_borrar=tk.StringVar()
        self.entry6=ttk.Entry(self.labelframe4,width=20,textvariable=self.codigo_borrar)
        self.entry6.grid(column=1,row=0,padx=4,pady=4)
        self.boton4=ttk.Button(self.labelframe4,text="borrar",command=self.borrar)
        self.boton4.grid(column=1,row=1,padx=4,pady=4)
    def borrar(self):
        pass

    def modificar_articulo(self):
        self.pagina5=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5,text="modificar articulo")
        self.labelframe5=ttk.Labelframe(self.pagina5,text="articulo")
        self.labelframe5.grid(column=0,row=0,padx=10,pady=10)
        self.label7=ttk.Label(self.labelframe5,text="codigo")
        self.label7.grid(column=0,row=0,padx=4,pady=4)
        self.codigo_modificar=tk.StringVar()
        self.entry7=ttk.Entry(self.labelframe5,width=20,textvariable=self.codigo_modificar)
        self.entry7.grid(column=1,row=0,padx=4,pady=4)
        self.label8=ttk.Label(self.labelframe5,text="descripcion: ")
        self.label8.grid(column=0,row=1,padx=4,pady=4)
        self.descripcion_modificar=tk.StringVar()
        self.entry8=ttk.Entry(self.labelframe5,width=20,textvariable=self.descripcion_modificar)
        self.entry8.grid(column=1,row=1,padx=4,pady=4)
        self.label9=ttk.Label(self.labelframe5,text="precio")
        self.label9.grid(column=0,row=2,padx=4,pady=4)
        self.precio_modificar=tk.StringVar()
        self.entry9=ttk.Entry(self.labelframe5,width=20,textvariable=self.precio_modificar)
        self.entry9.grid(column=1,row=2,padx=4,pady=4)
        self.boton5=ttk.Button(self.labelframe5,text="consultar", command=self.consultar_modificar)
        self.boton5.grid(column=0,row=3,padx=4,pady=4)
        self.boton6=ttk.Button(self.labelframe5,text="modificar",command=self.modificar)
        self.boton6.grid(column=1,row=3,padx=4,pady=4)
    def consultar_modificar(self):
        pass
    def modificar(self):
        pass







programapicantenashe=programapicantenashe()      
        
