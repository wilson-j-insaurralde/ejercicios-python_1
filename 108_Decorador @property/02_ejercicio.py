"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Problema
Plantear una clase dado. Ocultar el atributo que almacena el valor del dado y exponerlo a través de una propiedad.
"""

import random

class dado:
    def __init__(self):
        self.valor=1
    def tirar(self):
        self.valor=random.randint(1,6)

    @property
    def valor(self):
        return self._valor
    @valor.setter
    def valor(self,nuevo_valor):
        if nuevo_valor>=1 and nuevo_valor<=6:
            self._valor=nuevo_valor
        else:
            raise ValueError("Error: El valor del dado debe estar entre 1 y 6.")
dado1 = dado()
dado1.tirar()
print("Valor del dado",dado1.valor)
dado1.valor = 3
print("Valor del dado",dado1.valor)
dado1.valor = 50 # Esto genera un error


