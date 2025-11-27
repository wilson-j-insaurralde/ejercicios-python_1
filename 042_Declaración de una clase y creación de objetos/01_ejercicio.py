"""
Implementaremos una clase llamada Persona que tendrá como atributo (variable) su nombre y dos métodos (funciones), uno de dichos métodos inicializará el atributo nombre y el siguiente método mostrará en la pantalla el contenido del mismo.
"""
class persona():
    def inicializar(self,nomb):
        self.nombre=nomb

    def imprimir(self):
        print("nombre: ",self.nombre)

persona1=persona()
persona1.inicializar("pepe")
persona1.imprimir()

persona2=persona()
persona2.inicializar("pepa")
persona2.imprimir()
