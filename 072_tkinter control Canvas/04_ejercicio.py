"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""
"""
Implementar un gráfico estadístico de tipo "Barra Porcentual"
"""
import tkinter as tk 
from tkinter import ttk

class aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.generar_datos()
        self.canvas1=tk.Canvas(self.ventana1,width=600,height=400,background="black")
        self.canvas1.grid(column=0,row=1)
        self.ventana1.mainloop()
    def generar_datos(self):
        self.lbf1=ttk.LabelFrame(self.ventana1,text="Partidos politicos: ")
        self.lbf1.grid(column=0,row=0,sticky="w")
        self.label1=ttk.Label(self.lbf1,text="Partido A: ")
        self.label1.grid(column=0,row=0,padx=5,pady=5)
        self.dato1=tk.StringVar()
        self.entry1=ttk.Entry(self.lbf1,width=20,textvariable=self.dato1)
        self.entry1.grid(column=1,row=0,padx=5,pady=5)
        self.label2=ttk.Label(self.lbf1,text="Partido B:")
        self.label2.grid(column=0,row=1,padx=5,pady=5)
        self.dato2=tk.StringVar()
        self.entry2=ttk.Entry(self.lbf1,width=20,textvariable=self.dato2)
        self.entry2.grid(column=1,row=1,padx=5,pady=5)
        self.label3=ttk.Label(self.lbf1,text="Partido C:")
        self.label3.grid(column=0,row=2,padx=5,pady=5)
        self.dato3=tk.StringVar()
        self.entry3=ttk.Entry(self.lbf1,width=20,textvariable=self.dato3)
        self.entry3.grid(column=1,row=2,padx=5,pady=5)
        self.boton1=ttk.Button(self.lbf1,text="generar graficos",command=self.generar_graficos)
        self.boton1.grid(column=0,row=3,columnspan=2,sticky="we")
    def generar_graficos(self):
        self.canvas1.delete(tk.ALL)
        valor1=int(self.dato1.get())
        valor2=int(self.dato2.get())
        valor3=int(self.dato3.get())
        total=valor1+valor2+valor3
        num1=(valor1/total)*400
        num2=(valor2/total)*400
        num3=(valor3/total)*400
        porc1=valor1/total*100
        porc2=valor2/total*100
        porc3=valor3/total*100
        self.canvas1.create_rectangle(10,200,10+num1,260,fill="blue")
        self.canvas1.create_text(50, 220, text="{0:.2f}".format(porc1)+"%", fill="white", font="Arial")
        self.canvas1.create_rectangle(10+num1,200,10+num1+num2,260,fill="red")
        self.canvas1.create_text(50+num1, 220, text="{0:.2f}".format(porc2)+"%", fill="white", font="Arial")
        self.canvas1.create_rectangle(10+num1+num2,200,10+num1+num2+num3,260,fill="yellow")
        self.canvas1.create_text(50+num2+num1, 220, text="{0:.2f}".format(porc3)+"%", fill="white", font="Arial")


aplicacion=aplicacion()