"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Declarar una clase llamada Familia. Definir como atributos el nombre del padre, madre y una lista con los nombres de los hijos.
Definir el método especial __str__ que retorne un string con el nombre del padre, la madre y de todos sus hijos.
"""
class familia:

    def __init__(self,padre,madre,hijos=[]):
        self.hijos=hijos
        self.padre=padre
        self.madre=madre
    def __str__(self):
        cadena=str(self.padre)+","+str(self.madre)

        for hi in self.hijos:
            cadena=cadena+ ","+str(hi)
        return cadena

familia1=familia("Pablo","Ana",["Pepe","Julio"])
familia2=familia("Jorge","Carla")
familia3=familia("Luis","Maria",["marcos"])

print(familia1)
print(familia2)
print(familia3)