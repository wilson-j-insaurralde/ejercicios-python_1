"""
Autor: Wilson J. Insaurralde
Email: wilson-insaurralde[arroba]hotmail[punto]com
Derechos de Autor (c) 2025 Wilson J. Insaurralde. Todos los derechos reservados.
"""

"""
Enunciado: Crear una función recursiva que reciba un número n e imprima la palabra "TUKI" esa cantidad de veces.

Pista: Si n es 0, no hacés nada. Si es mayor, imprimís y llamás a la función con n-1
"""

def imprimir_tuki(n):

    if n==0:
        return 
    else:
        imprimir_tuki(n-1)
        print("tuki",end="--")

imprimir=imprimir_tuki(4)