"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Confeccionar una clase que permita carga el nombre y la edad de una persona. Mostrar los datos cargados. Imprimir un mensaje si es mayor de edad (edad>=18)
"""
 
class persona():

    def carga(self,nombre,edad):
        self.nombre=nombre
        self.edad=edad

    def imprmir(self):
        print("nombre: ",self.nombre)
        print("edad: ", self.edad)
    def mayordeedad(self):
        if self.edad>18:
            print("es mayor de edad")
        else:
            print("es menor de edad.")

pibe1=persona()
pibe1.carga("pepe",23)
pibe1.imprmir()
pibe1.mayordeedad()

pibe2=persona()
pibe2.carga("pepa",11)
pibe2.imprmir()
pibe2.mayordeedad()
