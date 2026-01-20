"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Agregar dos pestañas al programa de administración de artículos que permitan borrar un artículo ingresando su código y otra opción que permita consultar y modificar la descripción y precio de un artículo.
"""
#es mas de lo mismo, la practica hace al maestro
import tkinter as tk 
from tkinter import ttk 
from tkinter import messagebox as mb
from tkinter import scrolledtext as st
import articulos2

class aplicaciontuki:
    def __init__(self):
        self.articulos=articulos2.tuki()
        self.ventana1=tk.Tk()

        self.cuaderno1=ttk.Notebook(self.ventana1)
        self.carga_de_articulos()
        self.consulta_por_codigo()
        self.listado_completo()
        self.borrado()
        self.modificar()
        self.cuaderno1.grid(column=0,row=0,padx=10,pady=10)
        self.ventana1.mainloop()

    def carga_de_articulos(self):
        self.pagina1=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina1,text="carga de articulos")
        self.labelframe1=ttk.LabelFrame(self.pagina1,text="articulos")
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

        self.boton1=ttk.Button(self.labelframe1,text="confirmar",command=self.cargar)
        self.boton1.grid(column=1,row=2,padx=4,pady=4)
    def cargar(self):
        datos=(self.descripcion_carga.get(),self.precio_carga.get())
        self.articulos.carga(datos)
        mb.showinfo("informacion","los datos fueron cargados")
        self.descripcion_carga.set("")
        self.precio_carga.set("")

    def consulta_por_codigo(self):
        self.pagina2=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina2,text="consulta por codigo")
        self.labelframe2=ttk.LabelFrame(self.pagina2,text="articulo")
        self.labelframe2.grid(column=0,row=0,padx=10,pady=10)
        self.label3=ttk.Label(self.labelframe2,text="codigo")
        self.label3.grid(column=0,row=0,padx=4,pady=4)

        self.codigo_consulta=tk.StringVar()
        self.entry3=ttk.Entry(self.labelframe2,width=20,textvariable=self.codigo_consulta)
        self.entry3.grid(column=1,row=0,padx=4,pady=4)
        self.label4=ttk.Label(self.labelframe2,text="descripcion")
        self.label4.grid(column=0,row=1,padx=4,pady=4)
        self.descripcion_consulta=tk.StringVar()
        self.entry3=ttk.Entry(self.labelframe2,width=20,textvariable=self.descripcion_consulta)
        self.entry3.grid(column=1,row=1,padx=4,pady=4)
        self.label5=ttk.Label(self.labelframe2,text="precio")
        self.label5.grid(column=0,row=2,padx=4,pady=4)

        self.precio_consulta=tk.StringVar()
        self.entry4=ttk.Entry(self.labelframe2,width=20,textvariable=self.precio_consulta)
        self.entry4.grid(column=1,row=2,padx=4,pady=4)
        self.boton2=ttk.Button(self.labelframe2,text="consultar",command=self.consultar)
        self.boton2.grid(column=1,row=3,padx=4,pady=4)
    def consultar(self):
        datos=(self.codigo_consulta.get(),)
        respuestas=self.articulos.consultar(datos)
        if len(respuestas)>0:
            self.descripcion_consulta.set(respuestas[0][0])
            self.precio_consulta.set(respuestas[0][1])
        else:
            mb.showinfo("informacion","no se encontro articulo con dicho codigo")
            self.descripcion_consulta.set("")
            self.precio_consulta.set("")

    def listado_completo(self):
        self.pagina3=ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina3,text="listado completo")
        self.labelframe3=ttk.LabelFrame(self.pagina3,text="articulo")
        self.labelframe3.grid(column=0,row=0,padx=10,pady=10)
        self.boton3=ttk.Button(self.labelframe3,text="listado completo",command=self.listar_completito)
        self.boton3.grid(column=0,row=0,padx=4,pady=4)
        self.scrolledtext=st.ScrolledText(self.labelframe3,width=30,height=10)
        self.scrolledtext.grid(column=0,row=1,padx=10,pady=10)

    def listar_completito(self):
        respuestas=self.articulos.recuperar_todos()
        self.scrolledtext.delete("1.0",tk.END)
        for fila in respuestas:
            self.scrolledtext.insert(tk.END,"código:"+str(fila[0])+"\ndescripción:"+fila[1]+"\nprecio:"+str(fila[2])+"\n\n")
            
    def borrado(self):
        self.pagina4 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina4, text="Borrado de artículos")
        self.labelframe1=ttk.LabelFrame(self.pagina4, text="Artículo")        
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigoborra=tk.StringVar()
        self.entryborra=ttk.Entry(self.labelframe1, textvariable=self.codigoborra)
        self.entryborra.grid(column=1, row=0, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Borrar", command=self.borrar)
        self.boton1.grid(column=1, row=1, padx=4, pady=4)

    def borrar(self):
        datos=(self.codigoborra.get(), )
        cantidad=self.articulos.baja(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se borró el artículo con dicho código")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")

    def modificar(self):
        self.pagina5 = ttk.Frame(self.cuaderno1)
        self.cuaderno1.add(self.pagina5, text="Modificar artículo")
        self.labelframe1=ttk.LabelFrame(self.pagina5, text="Artículo")
        self.labelframe1.grid(column=0, row=0, padx=5, pady=10)
        self.label1=ttk.Label(self.labelframe1, text="Código:")
        self.label1.grid(column=0, row=0, padx=4, pady=4)
        self.codigomod=tk.StringVar()
        self.entrycodigo=ttk.Entry(self.labelframe1, textvariable=self.codigomod)
        self.entrycodigo.grid(column=1, row=0, padx=4, pady=4)
        self.label2=ttk.Label(self.labelframe1, text="Descripción:")        
        self.label2.grid(column=0, row=1, padx=4, pady=4)
        self.descripcionmod=tk.StringVar()
        self.entrydescripcion=ttk.Entry(self.labelframe1, textvariable=self.descripcionmod)
        self.entrydescripcion.grid(column=1, row=1, padx=4, pady=4)
        self.label3=ttk.Label(self.labelframe1, text="Precio:")        
        self.label3.grid(column=0, row=2, padx=4, pady=4)
        self.preciomod=tk.StringVar()
        self.entryprecio=ttk.Entry(self.labelframe1, textvariable=self.preciomod)
        self.entryprecio.grid(column=1, row=2, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Consultar", command=self.consultar_mod)
        self.boton1.grid(column=1, row=3, padx=4, pady=4)
        self.boton1=ttk.Button(self.labelframe1, text="Modificar", command=self.modifica)
        self.boton1.grid(column=1, row=4, padx=4, pady=4)

    def modifica(self):
        datos=(self.descripcionmod.get(), self.preciomod.get(), self.codigomod.get())
        cantidad=self.articulos.modificacion(datos)
        if cantidad==1:
            mb.showinfo("Información", "Se modificó el artículo")
        else:
            mb.showinfo("Información", "No existe un artículo con dicho código")

    def consultar_mod(self):
        datos=(self.codigomod.get(), )
        respuesta=self.articulos.consultar(datos)
        if len(respuesta)>0:
            self.descripcionmod.set(respuesta[0][0])
            self.preciomod.set(respuesta[0][1])
        else:
            self.descripcionmod.set('')
            self.preciomod.set('')
            mb.showinfo("Información", "No existe un artículo con dicho código")

aplicacion=aplicaciontuki()
        