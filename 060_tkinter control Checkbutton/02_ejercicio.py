"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Disponer un control Checkbutton que muestre el siguiente mensaje: ¿Está de acuerdo con los términos y condiciones?, además agregar un Button desactivo. Cuando se tilde el Checkbutton inmediatamente activar el botón.
"""
import tkinter as tk 

class aplicaccion():
    def __init__(self):
        self.ventana1=tk.Tk()
        self.seleccion1=tk.IntVar()
        self.check1=tk.Checkbutton(self.ventana1,text="¿Está de acuerdo con los términos y condiciones?",variable=self.seleccion1, command=self.cambiarestado)
        self.check1.grid(column=0,row=0)
        self.boton1=tk.Button(self.ventana1,text="entrar",state="disabled", command=self.ingresar)
        self.boton1.grid(column=0,row=1)
        self.ventana1.mainloop()
    def cambiarestado(self):
        if self.seleccion1.get()==1:
            self.boton1.configure(state="normal")
        if self.seleccion1.get()==0:
            self.boton1.configure(state="disabled")

    def ingresar (self):
        self.ventana1.title("ingresando...")

aplicaccion=aplicaccion()


