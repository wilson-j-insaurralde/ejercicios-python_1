"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""


"""
Confeccionar un programa que cree un objeto de la clase Canvas y nos muestre en el título de la ventana la coordenada actual del mouse dentro del control Canvas y al presionar el botón izquierdo del mouse se dibuje un círculo en dicha posición.
"""
import tkinter as tk 

class aplicacion: 
    def __init__(self):
        self.ventana1=tk.Tk()
        self.canvas1=tk.Canvas(self.ventana1,width=600,height=400,background="black")
        self.canvas1.bind("<Motion>",self.mover_mouse)
        self.canvas1.bind("<Button-1>",self.presion_mouse)
        self.canvas1.grid(column=0,row=1)
        self.ventana1.mainloop()
    def presion_mouse(self,evento):
        self.canvas1.create_oval(evento.x-5,evento.y-5,evento.x+5,evento.y+5, fill="red")
    def mover_mouse(self,evento):
        self.ventana1.title(str(evento.x)+"-"+str(evento.y))

aplicacion=aplicacion()
