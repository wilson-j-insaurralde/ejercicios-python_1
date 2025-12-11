"""
Mostrar los botones del 1 al 5. Cuando se presiona mostrar en una Label todos los botones presionados hasta ese momento.

"""
import tkinter as tk

class ventanoski():
    def __init__(self):
        self.ventana1=tk.Tk()
        self.ventana1.title("laventanoski")
        self.dato=""

        self.boton1=tk.Button(self.ventana1,text="boton 1", command=self.presion1)
        self.boton1.grid(column=0,row=1)
        
        self.boton2=tk.Button(self.ventana1,text="boton 2", command=self.presion2)
        self.boton2.grid(column=0,row=2)

        self.boton3=tk.Button(self.ventana1,text="boton 3", command=self.presion3)
        self.boton3.grid(column=0,row=3)

        self.boton4=tk.Button(self.ventana1,text="boton 4", command=self.presion4)
        self.boton4.grid(column=0,row=4)

        self.boton5=tk.Button(self.ventana1,text="boton 5", command=self.presion5)
        self.boton5.grid(column=0,row=5)

        self.label1=tk.Label(self.ventana1,text=self.dato)
        self.label1.grid(column=0,row=0)
        self.ventana1.mainloop()
    
    def presion1(self):
        self.dato=self.dato + "1"
        self.label1.configure(text=self.dato)
    def presion2(self):
        self.dato=self.dato + "2"
        self.label1.configure(text=self.dato)
    def presion3(self):
        self.dato=self.dato + "3"
        self.label1.configure(text=self.dato)
    def presion4 (self):
        self.dato=self.dato + "4"
        self.label1.configure(text=self.dato)
    def presion5(self):
        self.dato=self.dato + "5"
        self.label1.configure(text=self.dato)
  

ventana=ventanoski()