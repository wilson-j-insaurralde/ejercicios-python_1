"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Confeccionar una aplicación que muestre dos opciones en el menú de barra superior. La primer opción despliega un submenú que permita cambiar el color de fondo del formulario y la segunda permita cambiar el tamaño de formulario:
"""
import tkinter as tk 
class aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        menubar1=tk.Menu(self.ventana1)
        self.ventana1.config(menu=menubar1)
        opciones1=tk.Menu(menubar1)
        opciones1.add_command(label="Rojo",command=self.fijarrojo)
        opciones1.add_command(label="verde", command=self.fijarverde)
        opciones1.add_command(label="azul",command=self.fijarazul)
        menubar1.add_cascade(label="colores",menu=opciones1)
        opciones2=tk.Menu(menubar1)
        opciones2.add_command(label="640x480",command=self.ventanachica)
        opciones2.add_command(label="1024x800",command=self.ventanagrande)
        menubar1.add_cascade(label="tamaños",menu=opciones2)
        self.ventana1.mainloop()

    def fijarrojo(self):
        self.ventana1.configure(background="red")
    def fijarverde(self):
        self.ventana1.configure(background="green")
    def fijarazul(self):
        self.ventana1.configure(background="blue")
    def ventanachica(self):
        self.ventana1.geometry("640x400")
    def ventanagrande(self):
        self.ventana1.geometry("1024x800")
aplicacion=aplicacion()