"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""
import tkinter as tk 

class aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        menubar1=tk.Menu(self.ventana1)
        self.ventana1.configure(menu=menubar1)
        opciones1=tk.Menu(menubar1)
        opciones1.add_command(label="rojo",command=self.fijarrojo)
        opciones1.add_command(label="verde", command=self.fijarverde)
        opciones1.add_separator()
        opciones1.add_command(label="azul",command=self.fijarazul)
        menubar1.add_cascade(label="colores", menu=opciones1)
        opciones2=tk.Menu(menubar1)
        opciones2.add_command(label="640x480",command=self.ventanachica)
        opciones2.add_command(label="1080x800",command=self.ventanagrande)
        submenu1=tk.Menu(menubar1)
        submenu1.add_command(label="1024x1024",command=self.tamano1)
        submenu1.add_command(label="1280x1024",command=self.tamano2)
        opciones2.add_cascade(label="otros tamaños", menu=submenu1)
        menubar1.add_cascade(label="tamaños",menu=opciones2)
        self.ventana1.mainloop()

    def fijarrojo(self):
        self.ventana1.configure(background="red")

    def fijarverde(self):
        self.ventana1.configure(background="green")

    def fijarazul(self):
        self.ventana1.configure(background="blue")

    def ventanachica(self):
        self.ventana1.geometry("640x480")

    def ventanagrande(self):
        self.ventana1.geometry("1024x620")

    def tamano1(self):
        self.ventana1.geometry("1024x1024")

    def tamano2(self):
        self.ventana1.geometry("1280x1024")

aplicacion1=aplicacion()

    