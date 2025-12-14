"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Por defecto no aparece una barra de scroll si la cantidad de item supera el tamaño del cuadro del Listbox. Para que se muestre una barra de scroll la debemos crear y enlazar con el Listbox.
El mismo programa anterior pero con la barra de scroll queda:
papa-manzana-pera-sandia-naranja-melon-limon-kiwi-banana-uva-papaya-mandarina-frutilla
"""
import tkinter as tk 

class aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.scrol1=tk.Scrollbar(self.ventana1,orient="vertical")
        self.listbox1=tk.Listbox(self.ventana1,selectmode=tk.MULTIPLE,yscrollcommand=self.scrol1.set)
        self.listbox1.grid(column=0,row=0)
        self.scrol1.configure(command=self.listbox1.yview)
        self.scrol1.grid(column=1,row=0,sticky="NS")
        self.listbox1.insert(0,"Papa")
        self.listbox1.insert(1,"Manzana")
        self.listbox1.insert(2,"Pera")
        self.listbox1.insert(3,"Sandia")  
        self.listbox1.insert(4,"Naranja")
        self.listbox1.insert(5,"Melon")
        self.listbox1.insert(6,"Limon")
        self.listbox1.insert(7,"Kiwi")
        self.listbox1.insert(8,"Banana")
        self.listbox1.insert(9,"Uva")
        self.listbox1.insert(10,"Papaya")
        self.listbox1.insert(11,"Mandarina")
        self.listbox1.insert(12,"Frutilla")
        self.boton1=tk.Button(self.ventana1,text="recuperar",command=self.recuperar)
        self.boton1.grid(column=0,row=1)
        self.label1=tk.Label(self.ventana1,text="seleccionado")
        self.label1.grid(column=0,row=2)
        self.ventana1.mainloop()
      

    def recuperar(self):
        cadena=''
        if len(self.listbox1.curselection())!=0:
            for este in (self.listbox1.curselection()):
                cadena+=self.listbox1.get(este) +"\n"
        self.label1.configure(text=cadena)

aplicacion=aplicacion()