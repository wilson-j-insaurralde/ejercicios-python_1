"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Disponer dos objetos de la clase Button con las etiquetas: "varón" y "mujer", al presionarse mostrar en la barra de títulos de la ventana la etiqueta del botón presionado.
"""
import tkinter as tk
import sys
class ventana():
    def __init__(self):
        self.genero="nodefinido"
        self.ventana1=tk.Tk()
        self.ventana1.title("ventana1")
        
   

        self.boton1=tk.Button(self.ventana1,text="varon", command=self.varon)
        self.boton1.grid(column=0, row=1)

        self.boton2=tk.Button(self.ventana1,text="mujer", command=self.mujer)
        self.boton2.grid(column=0, row=2)
        self.ventana1.mainloop()
   
    def varon(self):
        self.genero="varon"
        self.ventana1.title(self.genero)
    def mujer (self):
        self.genero="mujer"
        self.ventana1.title(self.genero)

    
ventana1=ventana()