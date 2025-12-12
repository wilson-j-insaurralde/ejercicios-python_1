"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Mostrar una ventana y en su interior tres controles de tipo Checkbutton cuyas etiquetas correspondan a distintos lenguajes de programación. Cuando se presione un botón mostrar en una Label la cantidad de Checkbutton que se encuentran chequeados.
"""
import tkinter as tk

class aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.seleccion=tk.IntVar()
        self.check1=tk.Checkbutton(self.ventana1,text="Phyton", variable=self.seleccion)
        self.check1.grid(column=0,row=0)   
        self.seleccion2=tk.IntVar()
        self.check2=tk.Checkbutton(self.ventana1,text="c++",variable=self.seleccion2) 
        self.check2.grid(column=0,row=1)
        self.seleccion3=tk.IntVar()
        self.check3=tk.Checkbutton(self.ventana1,text="java",variable=self.seleccion3)
        self.check3.grid(column=0,row=2)
        self.boton1=tk.Button(self.ventana1,text="verificar", command=self.verificar)
        self.boton1.grid(column=0,row=4)
        self.label=tk.Label(self.ventana1,text="cantidad: ")
        self.label.grid(column=0,row=5)
        self.ventana1.mainloop()

    def verificar(self):
        cant=0
        if self.seleccion.get()==1:
            cant+=1
        if self.seleccion2.get()==1:
            cant+=1
        if self.seleccion3.get()==1:
            cant+=1
        self.label.configure(text="cantidad: "+str(cant))
aplicacion=aplicacion()
        

