"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Disponer un Listbox con una serie de nombres de frutas. Permitir la selección de varias frutas. Cuando se presione un botón recuperar todas las frutas seleccionadas y mostrarlas en una Label.
"""
import tkinter as tk 

class aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.listbox1=tk.Listbox(self.ventana1,selectmode=tk.MULTIPLE)
        self.listbox1.grid(column=0,row=0)
        self.listbox1.insert(0,"Papa")    
        self.listbox1.insert(1,"Manzana")
        self.listbox1.insert(2,"pera")
        self.listbox1.insert(3,"Sandia")
        self.listbox1.insert(4,"Naranja")
        self.listbox1.insert(5,"melon")
        self.boton1=tk.Button(self.ventana1,text="recuperar", command=self.recuperar)
        self.boton1.grid(column=0,row=1)
        self.label1=tk.Label(self.ventana1,text="seleccionado: ")
        self.label1.grid(column=0,row=2)
        self.ventana1.mainloop()
    def recuperar(self):
        if len(self.listbox1.curselection())!=0:
            todas=''
            for posicion in self.listbox1.curselection():
                todas+=self.listbox1.get(posicion)+"\n"
            self.label1.configure(text=todas)

aplicacion=aplicacion()
