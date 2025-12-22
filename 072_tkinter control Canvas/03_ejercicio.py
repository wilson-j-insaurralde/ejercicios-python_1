"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Crear una aplicación que solicite el ingreso de tres valores por teclado que representan las cantidades de votos obtenidas por tres partidos políticos. Luego mostrar un gráfico de tartas:
"""
import tkinter as tk 
from tkinter import ttk

class aplicacion: 
    def __init__(self):
        self.ventana1=tk.Tk()
        self.entrada_datos()
        self.canvas1=tk.Canvas(self.ventana1,width=600,height=400,background="black")
        self.canvas1.grid(column=0,row=1,)
        self.ventana1.mainloop()

    def entrada_datos(self):
        self.lbf1=ttk.LabelFrame(self.ventana1,text="Partidos politicos")
        self.lbf1.grid(column=0,row=0,sticky="w")
        self.labelA=ttk.Label(self.lbf1,text="Partido A:")
        self.labelA.grid(column=0,row=0,padx=5,pady=5)
        self.dato1=tk.StringVar()
        self.entryA=ttk.Entry(self.lbf1,width=20,textvariable=self.dato1)
        self.entryA.grid(column=1,row=0,padx=5,pady=5)
        self.labelB=ttk.Label(self.lbf1,text="Partido B:")
        self.labelB.grid(column=0,row=1,padx=5,pady=5)
        self.dato2=tk.StringVar()
        self.entryB=ttk.Entry(self.lbf1,width=20,textvariable=self.dato2)
        self.entryB.grid(column=1,row=1,padx=5,pady=5)
        self.labelC=ttk.Label(self.lbf1,text="Partido C:")
        self.labelC.grid(column=0,row=2,padx=5,pady=5)
        self.dato3=tk.StringVar()
        self.entryC=ttk.Entry(self.lbf1,width=20,textvariable=self.dato3)
        self.entryC.grid(column=1,row=2,padx=5,pady=5)
        self.boton1=ttk.Button(self.lbf1,text="Generar grafico",command=self.generar_grafico)
        self.boton1.grid(column=0,row=3,columnspan=2,padx=5,pady=5,sticky="we")
        self.entryA.focus()

    def generar_grafico(self):
      self.canvas1.delete(tk.ALL)
      valor1=int(self.dato1.get())
      valor2=int(self.dato2.get())
      valor3=int(self.dato3.get())
      total=valor1+valor2+valor3
      grados1=(valor1/total)*360
      grados2=(valor2/total)*360
      grados3=(valor3/total)*360
      self.canvas1.create_arc(10,10,400,400,fill="red",start=0,extent=grados1)
      self.canvas1.create_arc(10,10,400,400,fill="blue",start=grados1,extent=grados2)
      self.canvas1.create_arc(10,10,400,400,fill="yellow",start=grados1+grados2,extent=grados3)
      self.canvas1.create_text(500, 50, text="partido A:"+str(valor1), fill="red", font="Arial")
      self.canvas1.create_text(500, 100, text="partido B:"+str(valor2), fill="blue", font="Arial")
      self.canvas1.create_text(500, 150, text="partido C:"+str(valor3), fill="yellow", font="Arial")


aplicacion=aplicacion()