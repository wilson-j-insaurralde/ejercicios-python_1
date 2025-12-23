"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Se cuenta con dos archivos de tipo png con las imágenes de distintas cartas. Mostrarlas a cada una dentro de una componente de tipo Canvas y permitir moverlas dentro del control mediante el mouse.
"""
import tkinter as tk 

class aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.canvas1=tk.Canvas(self.ventana1,width=900,height=600,background="black")
        self.canvas1.grid(column=0,row=0)
        archi1=tk.PhotoImage(file="077_Canvas mover una figura/imagenes/carta1.png")
        archi2=tk.PhotoImage(file="077_Canvas mover una figura/imagenes/carta2.png")
        self.canvas1.create_image(30,100,image=archi1,anchor="nw",tags="movil")
        self.canvas1.create_image(400,100,image=archi2,anchor="nw",tags="movil")
        self.canvas1.tag_bind("movil","<ButtonPress-1>",self.presion_boton)
        self.canvas1.tag_bind("movil","<Button1-Motion>",self.mover)
        self.cartas_seleccionada=None
        self.ventana1.mainloop()
    def presion_boton(self,evento):
        carta=self.canvas1.find_withtag(tk.CURRENT)
        self.cartas_seleccionada=(carta,evento.x,evento.y)
        
    def mover(self,evento):
        x,y=evento.x,evento.y
        carta,x1,y1=self.cartas_seleccionada
        self.canvas1.move(carta,x-x1,y-y1)
        self.cartas_seleccionada = (carta, x, y)

aplicacion=aplicacion()
