"""
Ingresar el nombre de usuario y clave en controles de tipo Entry. Si se ingresa las cadena (usuario: juan, clave="abc123") luego mostrar en el título de la ventana el mensaje "Correcto" en caso contrario mostrar el mensaje "Incorrecto".
Para mostrar '*' cuando se ingresa la clave debemos pasar en el parámetro 'show' el caracter a mostrar:
        self.entry2=tk.Entry(self.ventana1, width=30, textvariable=self.dato2, show="*")
"""
import tkinter as tk 

class usuario():
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk.Label(self.ventana1,text="usuario: ")
        self.label1.grid(column=0,row=0)
        self.usuario=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1,width=20,textvariable=self.usuario)
        self.entry1.grid(column=1,row=0)
        self.label2=tk.Label(self.ventana1,text="contraseña: ")
        self.label2.grid(column=0,row=1)
        self.contraseña=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1,width=20,textvariable=self.contraseña,show="*")
        self.entry2.grid(column=1,row=1)
        self.boton1=tk.Button(self.ventana1,text="ver ",command=self.verificar)
        self.boton1.grid(column=0,row=2)
        self.ventana1.mainloop()
    def verificar(self):
        usuario=str(self.usuario.get())
        contraseña=str(self.contraseña.get())
        if usuario=="juan" and contraseña=="abc123":
            self.ventana1.title("correcto")
        else:
            self.ventana1.title("incorrecto")

        
usuariopa=usuario()