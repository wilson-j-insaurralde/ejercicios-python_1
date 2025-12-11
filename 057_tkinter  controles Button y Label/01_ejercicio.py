"""
Mostrar una ventana y en su interior dos botones y una label. La label muestra inicialmente el valor 1. Cada uno de los botones permiten incrementar o decrementar en uno el contenido de la label
"""
import tkinter as tk 

class aplicacion: 
    def __init__(self):
        self.valor=1
        self.ventana1=tk.Tk()
        self.ventana1.title("controles buton y label")
        self.label1=tk.Label(self.ventana1, text=self.valor)
        self.label1.grid(column=0,row=0)
        self.label1.configure(foreground="red")
        
        self.boton1=tk.Button(self.ventana1, text="Incrementar", command=self.incrementar)
        self.boton1.grid(column=0, row=1)

        self.boton2=tk.Button(self.ventana1, text="Decrementar", command=self.decrementar)
        self.boton2.grid(column=0, row=2)

        self.ventana1.mainloop()

    def incrementar(self):
        self.valor=self.valor+1
        self.label1.config(text=self.valor)

    def decrementar(self):
        self.valor=self.valor-1
        self.label1.config(text=self.valor)        


aplicacion1=aplicacion()


"""
Definimos un atributo en la clase Aplicacion y almacenamos el valor 1:
        self.valor=1
Creamos la ventana y le fijamos un título como hemos visto en el concepto anterior:
        self.ventana1=tk.Tk()
        self.ventana1.title("Controles Button y Label")
Ahora creamos un objeto de la clase Label y le pasamos como primer parámetro la referencia a la ventana donde debe aparecer la label y el parámetro text con el valor inicial de la Label:
        self.label1=tk.Label(self.ventana1, text=self.valor)
Para ubicar los controles visuales en la ventana veremos más adelante que hay diferentes Layout, por ahora en forma muy sencilla mediante la llamada al método grid indicaremos en los parámetros column y row la ubicación del mismo:

        self.label1.grid(column=0, row=0)
Para que el texto de la Label se muestre de color rojo llamamos al método configure y le pasamos en el parámetro foreground el string "red":

        self.label1.configure(foreground="red")
La creación de los dos botones es similar a la creación de la label, en el primer parámetro indicamos la referencia de la ventana donde se debe mostrar el botón, en el parámetro text indicamos el texto a mostrar dentro del botón y finalmente en el parámetro command pasamos la referencia del método que se ejecutará cuando el operador lo presione:

        self.boton1=tk.Button(self.ventana1, text="Incrementar", command=self.incrementar)
        self.boton1.grid(column=0, row=1)

        self.boton2=tk.Button(self.ventana1, text="Decrementar", command=self.decrementar)
        self.boton2.grid(column=0, row=2)
Para que los botones se encuentren abajo de la Label al llamar al método grid pasamos en el parámetro row los valores 1 y 2. Como todos los controles se encuentran en la misma columna pasamos en column el valor 0.

No olvidar a llamar al final del método __init__ al método mainloop():

self.ventana1.mainloop()
El método incrementar se ejecuta cuando el operador presiona el boton1 (dentro del mismo incrementamos en uno el atributo valor y actualizamos el contenido de la label1 llamando al método config y en el parámetro text el nuevo valor a mostrar):

    def incrementar(self):
        self.valor=self.valor+1
        self.label1.config(text=self.valor)
El algoritmo del método decrementar solo difiere en que decrementa en uno el atributo valor:

    def decrementar(self):
        self.valor=self.valor-1
        self.label1.config(text=self.valor)        
No olvidemos crear un objeto de la clase 'Aplicacion' en el bloque principal del programa:

aplicacion1=Aplicacion()

"""