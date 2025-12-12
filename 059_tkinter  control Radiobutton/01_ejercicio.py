"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Mostrar dos controles de tipo Radiobutton con las etiquetas "Varón" y "Mujer", cuando se presione un botón actualizar una Label con el Radiobutton seleccionado.
"""
import tkinter as tk    

class aplicacion():
    def __init__(self):
        self.ventana1=tk.Tk()
        self.seleccion=tk.IntVar()
        self.seleccion.set(2)
        self.radio1=tk.Radiobutton(self.ventana1,text="varon", variable=self.seleccion,value=1)
        self.radio1.grid(column=0, row=0)

        self.radio2=tk.Radiobutton(self.ventana1,text="mujer",variable=self.seleccion,value=2)
        self.radio2.grid(column=0,row=1)

        self.boton1=tk.Button(self.ventana1,text="mostrar seleccionado",command=self.mostrarseleccion)
        self.boton1.grid(column=0,row=2)
        self.label1=tk.Label(self.ventana1,text="opcion seleccionada")
        self.label1.grid(column=0,row=3)
        self.ventana1.mainloop()

    def mostrarseleccion(self):
        if self.seleccion.get()==1:
            self.label1.configure(text="varon")
        if self.seleccion.get()==2:
            self.label1.configure(text="mujer")

aplicacion=aplicacion()
            


       