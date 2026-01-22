"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""


"""
El lenguaje Python permite definir una función dentro de otra función.

Cuando necesitamos una pequeña "función" que solo tiene sentido dentro del contexto de otra función, es aquí donde entran en juego las funciones anidadas.

Problema 1
Definir una función interna a otra función.

"""

def funcion_principal():
    def funcion_interna():
        print("hola desde la funcion interna.")

    funcion_interna()
    print("hola desde la funcion principal")

funcion_principal()