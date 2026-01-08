"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""
"""
Implementar una función recursiva que imprima en forma descendente de 5 a 1 de uno en uno.
"""

def imprimir(x):
    if x>0:
        print(x)
        imprimir(x-1)

imprimir(5)   