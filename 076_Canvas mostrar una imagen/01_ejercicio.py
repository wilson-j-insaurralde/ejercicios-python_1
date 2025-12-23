"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""Se cuenta con tres archivos de tipo png con las imágenes de distintas cartas. Mostrarlas a cada una dentro de una componente de tipo Canvas"""
import tkinter as tk 

class aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.canvas1=tk.Canvas(self.ventana1,width=900,height=600,background="black")
        self.canvas1.grid(column=0,row=0)
        archil=tk.PhotoImage(file="076_Canvas mostrar una imagen/imagenes/carta1.png")
        self.canvas1.create_image(30,100,image=archil,anchor="nw")
        archi2=tk.PhotoImage(file="076_Canvas mostrar una imagen/imagenes/carta2.png")
        self.canvas1.create_image(240,100,image=archi2,anchor="nw")
        archi3=tk.PhotoImage(file="076_Canvas mostrar una imagen/imagenes/carta3.png")
        self.canvas1.create_image(450,100,image=archi2,anchor="nw")

        
        self.ventana1.mainloop()

aplicacion=aplicacion()