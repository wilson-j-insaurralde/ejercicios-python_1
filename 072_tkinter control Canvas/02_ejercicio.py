"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""
"""
Crear una aplicación que solicite el ingreso de tres valores por teclado que representan las cantidades de votos obtenidas por tres partidos políticos. Luego mostrar un gráfico de barras horizontales.
"""
import tkinter as tk
from tkinter import ttk
class aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.entrada_datos()
        self.canvas1=tk.Canvas(self.ventana1,width=600, height=400, background="black")
        
        self.canvas1.grid(column=0,row=1)
      
        self.ventana1.mainloop()
    

    def entrada_datos(self):
        self.lbf1=ttk.LabelFrame(self.ventana1,text="partidos politicos")
        self.lbf1.grid(column=0,row=0,sticky="w")
        self.labelA=ttk.Label(self.lbf1,text="Partido A: ")
        self.labelA.grid(column=0,row=0,padx=5,pady=5)
        self.dato1=tk.StringVar()
        self.entryA=ttk.Entry(self.lbf1,width=20,textvariable=self.dato1)
        self.entryA.grid(column=1,row=0,padx=5,pady=5)
        self.labelB=ttk.Label(self.lbf1,text="Partido B: ")
        self.labelB.grid(column=0,row=1,padx=5,pady=5)
        self.dato2=tk.StringVar()
        self.entryB=ttk.Entry(self.lbf1,width=20,textvariable=self.dato2)
        self.entryB.grid(column=1,row=1,padx=5,pady=5)
        self.labelC=ttk.Label(self.lbf1,text="Partido C")
        self.labelC.grid(column=0,row=2,padx=5,pady=5)
        self.dato3=tk.StringVar()
        self.entryC=ttk.Entry(self.lbf1,width=20,textvariable=self.dato3)
        self.entryC.grid(column=1,row=2,padx=5,pady=5)
        self.boton1=ttk.Button(self.lbf1,text="generar grafico",command=self.generar_grafico)
        self.boton1.grid(column=0,row=3,columnspan=2,padx=5,pady=5,sticky="we")
        self.entryA.focus()
        
    def generar_grafico(self):
        self.canvas1.delete(tk.ALL)
        valorA=int(self.dato1.get())
        valorB=int(self.dato2.get())
        valorC=int(self.dato3.get())
        if valorA>valorB and valorA>valorC:
            mayor=valorA
        else: 
            if valorB>valorC:
                mayor=valorB
            else:
                mayor=valorC
        
        largo1=(valorA/mayor)*400
        largo2=(valorB/mayor)*400
        largo3=(valorC/mayor)*400
        self.canvas1.create_rectangle(10,10,10+largo1,90,fill="red")
        self.canvas1.create_rectangle(10,120,10+largo2,200,fill="green")
        self.canvas1.create_rectangle(10,230,10+largo3,310,fill="yellow")
        self.canvas1.create_text(largo1+70, 50, text="partido A", fill="white", font="Arial")
        self.canvas1.create_text(largo2+70, 160, text="partido B", fill="white", font="Arial")
        self.canvas1.create_text(largo3+70, 270, text="partido C", fill="white", font="Arial")
            



aplicacion=aplicacion()  
