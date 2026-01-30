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

"""
Hemos creado el atributo _valor donde almacenamos el valor del dado.

¿Por qué usamos _valor en lugar de valor?

En Python no existe la encapsulación estricta (como private o protected en Java o C++).
En su lugar, se usa una convención de nombres:

atributo (sin _)
Se considera público. Se puede acceder libremente desde fuera de la clase.
_atributo (con un _ al inicio)
Se considera protegido/privado por convención.
Es una forma de decirle a otros programadores:
"Este atributo es interno, no deberías accederlo directamente; usá propiedades."

class Dado:
    def __init__(self):
        self._valor = 1   # atributo interno
Usamos _valor para indicar que es un atributo interno que no debería tocarse desde afuera.

En lugar de eso, exponemos una property llamada valor:

@property
def valor(self):
    return self._valor
Así, el usuario de la clase escribe dado1.valor como si accediera a un atributo, pero en realidad lo que está pasando es que se ejecuta el método valor().

print("Valor del dado",dado1.valor)
Esto permite ocultar la implementación interna y tener control.

¿Qué es @valor.setter?

    @valor.setter
    def valor(self, nuevo_valor):
        if nuevo_valor >=1 and nuevo_valor <= 6:
            self._valor = nuevo_valor
        else:            
            raise ValueError("Error: El valor del dado debe estar entre 1 y 6.")
En Python, cuando definís una propiedad con @property, por defecto esa propiedad es solo de lectura (o sea, podés acceder al valor pero no modificarlo), nos daría error:

dado1.valor = 3
Si querés permitir la escritura controlada de ese atributo, usás el decorador @<nombre>.setter, donde <nombre> debe coincidir con el de la propiedad:

    @property
    def valor(self):
        return self._valor

    @valor.setter
    def valor(self, nuevo_valor):
        if nuevo_valor >=1 and nuevo_valor <= 6:
            self._valor = nuevo_valor
        else:            
            raise ValueError("Error: El valor del dado debe estar entre 1 y 6.")
Con @valor.setter podemos validar que el dato a almacenar en el atributo sea válido, logramos tener una clase más robusta.

Debe quedar claro que la propiedad se llama valor y el atributo _valor.
"""
