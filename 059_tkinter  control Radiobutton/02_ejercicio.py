"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Disponer dos controles de tipo Entry para el ingreso de enteros. Mediante dos controles Radiobutton permitir seleccionar si queremos sumarlos o restarlos. Al presionar un botón mostrar el resultado de la operación seleccionada.
"""
import tkinter as tk 
class aplicacion():
    def __init__(self):
        self.ventana1=tk.Tk()
        self.seleccion=tk.IntVar()
        self.seleccion.set(2)
        self.raidio1=tk.Radiobutton(self.ventana1,text="sumar",variable=self.seleccion,value=1)
        self.raidio1.grid(column=0,row=0)
        self.raidio2=tk.Radiobutton(self.ventana1,text="restar",variable=self.seleccion,value=2)
        self.raidio2.grid(column=1,row=0)
        
        self.numero1=tk.IntVar()
        self.entry1=tk.Entry(self.ventana1,width=20,textvariable=self.numero1)
        self.entry1.grid(column=1,row=2)
        self.label1=tk.Label(self.ventana1,text="ingrese el primer numero: ")
        self.label1.grid(column=0,row=2)

        self.numero2=tk.IntVar()
        self.entry2=tk.Entry(self.ventana1,width=20,textvariable=self.numero2)
        self.entry2.grid(column=1,row=3)
        self.label2=tk.Label(self.ventana1,text="ingrese el segundo numero: ")
        self.label2.grid(column=0,row=3)

        self.boton1=tk.Button(self.ventana1,text="aceptar",command=self.eleccion1)
        self.boton1.grid(column=1,row=4)
        self.label3=tk.Label(self.ventana1,text="resultado0")
        self.label3.grid(column=0, row=5)
        self.ventana1.mainloop()

    def eleccion1(self):
        num1=int(self.numero1.get())
        num2=int(self.numero2.get())
        if self.seleccion.get()==1:
            suma=num1+num2
            self.label3.config(text=suma)
        if self.seleccion.get()==2:
            resta=num1-num2
            self.label3.configure(text=resta)
aplicacion1=aplicacion()