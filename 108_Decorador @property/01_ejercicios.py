"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Antes de explicar el decorador @property vamos a disponer un ejemplo y mostrar el tipo de problema que nos resolverá este decorador.

Problema
Plantear una clase dado.
"""

import random

class dado:
    def __init__(self):
        self.valor=1
        self.tirar()
    def tirar (self):
        self.valor=random.randint(1,6)
    def imprimir(self):
        print("El valor del dado es:", self.valor)

dado1=dado()
dado1.tirar()
dado1.imprimir()
dado1.valor=50
dado1.imprimir()

"""
En muchas situaciones queremos que un atributo no sea modificado desde fuera de la clase, es lógico que un dado solo puede almacenar valores entre 1 y 6.

Desde fuera de la clase estamos modificando por un valor que no puede tener un dado:

dado1.valor = 50
En el lenguaje Python los atributos de una clase siempre son públicos y accesibles desde fuera, veremos como mediante el decorador @property podemos tener una solución elegante a este problema.

"""