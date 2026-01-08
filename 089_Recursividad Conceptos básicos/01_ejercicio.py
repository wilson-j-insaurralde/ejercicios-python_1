"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Implementación de una función recursiva.
"""
def repetir():
    repetir()

repetir()


"""
La función repetir es recursiva porque dentro de la función se llama a sí misma.
Cuando ejecuta este programa se bloqueará y generará una excepción: "RecursionError: maximum recursion depth exceeded"

Analicemos como funciona:
Se llama la función repetir.
Hay que tener en cuenta que cada vez que se llama a una función se reservan un conjunto de bytes de la memoria que se liberarán cuando finalice su ejecución.
La primera línea de la función llama a la función repetir, es decir que se reservan más bytes nuevamente. Se ejecuta nuevamente una instancia de la función repetir y así sucesivamente hasta que la pila estática se colme y se cuelgue el programa.
"""