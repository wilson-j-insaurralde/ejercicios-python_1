"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Imprimir los números de 1 a 5 en pantalla utilizando recursividad.
"""
def imprimir(x):
    if x>0:
        imprimir(x-1)
        print(x)

imprimir(5)   
