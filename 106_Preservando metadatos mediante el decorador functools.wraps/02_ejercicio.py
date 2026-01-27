"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
La solución: functools.wraps
Este decorador copia los metadatos de la función original a la función envoltura.
"""

import functools

def mi_decorador(func):
    @functools.wraps(func)
    def envoltura(*args, **kwargs):
        """Función envoltorio"""
        print("Antes de la función...")
        resultado = func(*args, **kwargs)
        print("Después de la función...")
        return resultado
    return envoltura

@mi_decorador
def saludar():
    """Esta función imprime un saludo amigable."""
    print("¡Hola!")

print(saludar.__name__)  #  saludar
print(saludar.__doc__)   #  Esta función imprime un saludo amigable.


"""
@functools.wraps(func) es en realidad un decorador de decoradores.

Lo que hace internamente es:
Copiar atributos importantes (__name__, __doc__, __module__, __annotations__) desde la función original a la función envoltura.

Agregar un atributo especial __wrapped__ que apunta a la función original.

Esto asegura que la función decorada se comporte como la original en cuanto a metadatos.

Buenas prácticas
Siempre que crees un decorador que envuelva una función, usa @functools.wraps.
Esto lo hace más profesional, robusto y compatible con herramientas externas.

"""