"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Confeccionar una aplicación visual con tkinter que permita ingresar en un control de tipo 'Entry' la URL de un sitio web y al presionar un botón recuperar los datos y mostrarlos en un control de tipo 'ScrolledText':
"""

import tkinter as tk
from tkinter import ttk 
from tkinter import scrolledtext as st
from urllib import request
from urllib import error
from tkinter import messagebox as mb

class aplicacion: 
    def __init__(self):
        self.ventana1=tk.Tk()
        self.labelframe1=ttk.LabelFrame(self.ventana1,text="lector url")
        self.leer()
        self.labelframe1.grid(column=0,row=0,padx=10,pady=10)
        self.ventana1.mainloop()

    def leer(self):
        self.label1=ttk.Label(self.labelframe1,text="ingrese url del sitio web:")
        self.label1.grid(column=0,row=0,padx=4,pady=4)
        self.ruta=tk.StringVar()
        self.entry=ttk.Entry(self.labelframe1,width=40,textvariable=self.ruta)
        self.entry.grid(column=0,row=1,padx=4,pady=4)
        self.boton=ttk.Button(self.labelframe1,text="recuperar",command=self.recuperar)
        self.boton.grid(column=0,row=2,padx=4,pady=4)
        self.scrolledtext=st.ScrolledText(self.labelframe1,width=30,height=10)
        self.scrolledtext.grid(column=0,row=3,padx=10,pady=10)
    def recuperar(self):
        try:
            pagina=request.urlopen(self.ruta.get())
            datos=pagina.read().decode("utf-8")
            self.scrolledtext.delete(1.0,tk.END)
            self.scrolledtext.insert(tk.INSERT,datos)
        except error.HTTPError as err:
            mb.showinfo("Problemas", "No se puede acceder a dicho recurso")

aplicacion=aplicacion()