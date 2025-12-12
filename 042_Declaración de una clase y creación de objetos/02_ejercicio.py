"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Implementar una clase llamada Alumno que tenga como atributos su nombre y su nota. Definir los métodos para inicializar sus atributos, imprimirlos y mostrar un mensaje si está regular (nota mayor o igual a 4)

Definir dos objetos de la clase Alumno.
"""
class alumno():

    def inicializar(self,nombre,nota1):
        self.alumno=nombre
        self.nota=nota1

    def imprimir(self):
        print("nombre: ",self.alumno)
        print("nota",self.nota)

    def mostrar_estado(self):
        if self.nota>=4:
            print("regular")
        else: 
            print("libre")
alumno1=alumno()
alumno1.inicializar("pepe",2)
alumno1.imprimir()
alumno1.mostrar_estado()

alumno2=alumno()
alumno2.inicializar("pepa",3)
alumno2.imprimir()
alumno2.mostrar_estado()