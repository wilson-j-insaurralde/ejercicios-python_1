"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Solicitar el ingreso del nombre de una persona y seleccionar de un control Listbox un país. Al presionar un botón mostrar en la barra de la ventana el nombre ingresado y el país seleccionado.

"""
import tkinter as tk 
class aplicaccion: 
    def __init__(self):
        self.ventana1=tk.Tk()

        self.label1=tk.Label(self.ventana1,text="ingrese su nombre: ")
        self.label1.grid(column=0,row=0)
        
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1,width=20,textvariable=self.dato1)
        self.entry1.grid(column=1,row=0)
        self.label2=tk.Label(self.ventana1,text="seleccione su pais: ")
        self.label2.grid(column=0,row=1)
        self.scrol1=tk.Scrollbar(self.ventana1,orient="vertical")
        self.listbox1=tk.Listbox(self.ventana1,yscrollcommand=self.scrol1.set)
        self.listbox1.grid(column=1,row=2)
        self.scrol1.configure(command=self.listbox1.yview)
        self.scrol1.grid(column=2,row=2,sticky="NS")
        self.listbox1.insert(0,"argentina")
        self.listbox1.insert(1,"paraguay")
        self.listbox1.insert(2,"bolivia")
        self.listbox1.insert(3,"chile")
        self.listbox1.insert(4,"uruguay")
        self.listbox1.insert(5,"colombia")
        self.listbox1.insert(6,"peru")
        self.listbox1.insert(7,"brazil")
        self.listbox1.insert(8,"ecuador")
        self.listbox1.insert(9,"venezuela") 
        self.listbox1.insert(10,"españa")
        self.listbox1.insert(11,"inglaterra")
        self.listbox1.insert(12,"rusia")
        self.listbox1.insert(13,"nose")
        self.boton1=tk.Button(self.ventana1,text="seleccion",command=self.seleccion)
        self.boton1.grid(column=1,row=3)
        self.label3=tk.Label(self.ventana1,text=" ")
        self.label3.grid(column=0,row=4)
        



        self.ventana1.mainloop()
    def seleccion(self):
        nombre=str(self.dato1.get())
        if len(self.listbox1.curselection())!=0:
            indice_pais=self.listbox1.curselection()[0]
            pais_seleccionado=self.listbox1.get(indice_pais)
        self.label3.config(text=f"{nombre}---{pais_seleccionado}")
            



aplicaccion=aplicaccion()    