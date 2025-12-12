"""
Disponer tres controles de tipo Radiobutton con las etiquetas 'Rojo', 'Verde' y 'Azul'. Cuando se presione un botón cambiar el color de fondo del formulario.
Si consideramos que la variable ventana1 es un objeto de la clase Tk, luego si queremos que el fondo sea de color rojo debemos llamar al método configure y en el parámetro bg indicar un string con el color a activar ("red", "green" o "blue"):
            self.ventana1.configure(bg="red")

"""
import tkinter as tk 
class aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.numero1=tk.IntVar()
        self.numero1.set(0)
        self.raid1=tk.Radiobutton(self.ventana1,text="rojo",variable=self.numero1,value=1)
        self.raid1.grid(column=0,row=0)
        self.raid2=tk.Radiobutton(self.ventana1,text="verde",variable=self.numero1,value=2)
        self.raid2.grid(column=1,row=0)
        self.raid3=tk.Radiobutton(self.ventana1,text="azul",variable=self.numero1,value=3)
        self.raid3.grid(column=2,row=0)

        self.boton1=tk.Button(self.ventana1,text="color",command=self.color_elegido)
        self.boton1.grid(column=1,row=1)

        self.ventana1.mainloop()

    def color_elegido(self):
        if self.numero1.get()==1:
            self.ventana1.configure(bg="red")
        if self.numero1.get()==2:
            self.ventana1.configure(bg="green")
        if self.numero1.get()==3:
            self.ventana1.configure(bg="blue")
            
aplicacion=aplicacion()

