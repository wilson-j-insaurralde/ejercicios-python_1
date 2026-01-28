"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""
"""
En Python, podemos aplicar más de un decorador sobre una misma función.
Esto se llama encadenamiento de decoradores y es muy útil cuando queremos aplicar varias mejoras combinadas, como:

Medir el tiempo de ejecución.
Registrar llamadas en un log.
Validar permisos o datos.
Agregar trazas de depuración.
El orden de ejecución cuando apilamos decoradores:

@decorador1
@decorador2
def funcion():
    ...
Esto equivale a:

funcion = decorador1(decorador2(funcion))
Es decir, el decorador más cercano a la función se aplica primero, pero en tiempo de ejecución la llamada pasa primero por el decorador que quedó más arriba en la pila.

"""


def decorador_a(func):
    def envoltura(*args, **kwargs):
        print("Entrando en A")
        resultado = func(*args, **kwargs)
        print("Saliendo de A")
        return resultado
    return envoltura

def decorador_b(func):
    def envoltura(*args, **kwargs):
        print("Entrando en B")
        resultado = func(*args, **kwargs)
        print("Saliendo de B")
        return resultado
    return envoltura

@decorador_a
@decorador_b
def saludar():
    print("Hola mundo")

saludar()

"""
Cuando se ejecuta tenemos como salida:

Entrando en A
Entrando en B
Hola mundo
Saliendo de B
Saliendo de A
Primero se aplica decorador_b (el más cercano a la función).
Luego decorador_a envuelve todo.
En tiempo de ejecución, se entra primero en A ? luego en B ? función ? se sale de B ? se sale de A.
"""