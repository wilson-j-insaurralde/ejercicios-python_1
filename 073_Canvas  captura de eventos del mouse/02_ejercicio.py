"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Confeccionar un programa que cree un objeto de la clase Canvas y nos permita dibujar a mano alzada dentro del mismo.
"""
import tkinter as tk 

class aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.canvas1=tk.Canvas(self.ventana1,width=600,height=400,background="black")
        self.canvas1.grid(column=0,row=1)
        self.canvas1.bind("<ButtonPress-1>",self.boton_presion)
        self.canvas1.bind("<Motion>",self.mover_mouse)
        self.canvas1.bind("<ButtonRelease-1>",self.boton_soltar)
        self.presionado=False
        self.ventana1.mainloop()

    def boton_presion(self,evento):
        self.presionado=True
        self.origenx=evento.x
        self.origeny=evento.y
    def mover_mouse(self,evento):
        if self.presionado:
            self.canvas1.create_line(self.origenx,self.origeny,evento.x,evento.y, fill="red")
            self.origenx=evento.x
            self.origeny=evento.y
    
    def boton_soltar(self,evento):
        self.presionado=False
aplicacion=aplicacion()