"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""
"""
Confeccionar un programa que que muestre un cuadrado dentro de un Canvas. Cuando se presione alguna de las teclas de flecha proceder a desplazar la figura 4 píxeles teniendo en cuenta la dirección de la tecla de flecha presionada.
"""
import tkinter as tk 

class aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.canvas1=tk.Canvas(self.ventana1,width=600,height=400,background="black")
        self.canvas1.grid(column=0,row=1)
        self.cuadrado=self.canvas1.create_rectangle(150,10,200,60, fill="red")
        self.ventana1.bind("<KeyPress>",self.presion_tecla)
        self.ventana1.mainloop()
    def presion_tecla(self,evento):
        if evento.keysym=="Right":
            self.canvas1.move(self.cuadrado,4,0)
        if evento.keysym=="Left":
            self.canvas1.move(self.cuadrado,-4,0)
        if evento.keysym=="Down":
            self.canvas1.move(self.cuadrado,0,4)
        if evento.keysym=="Up":
            self.canvas1.move(self.cuadrado,0,-4)
        
aplicacion=aplicacion()
